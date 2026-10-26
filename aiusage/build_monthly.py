#!/usr/bin/env python3
"""Build the monthly combined JMCo AI usage CSV.

Drop the latest ChatGPT / Copilot / CoCounsel CSV exports (and keep
"AI Usage.xlsx" for carrying metadata forward) in this folder, then run:

    python build_monthly.py

Output: combined-<MM>.csv in the same folder. See AI_USAGE_REPORT_PROCESS.md.
Only the standard library is required; openpyxl is used (if installed) to read
Job / Org Level 1 / AI Champion? / Claude / display names from the workbook.
"""
import argparse
import csv
import math
import re
import sys
from datetime import datetime
from pathlib import Path

CREDITS_PER_MESSAGE = 5.14
EXCLUDED = {"admin-tmb@jmco.com", "internaladmin@jmco.com"}

COLUMNS = [
    "Employee Name (Last Suffix, First MI)", "Employee Email", "Job", "Org Level 1",
    "AI Champion?", "ChatGPT Access", "ChatGPT Messages", "ChatGPT Credits",
    "Copilot Access", "Copilot Prompts - All Apps", "Copilot Active Usage Days",
    "CoCounsel Access", "CoCounsel Messages", "Claude (Pilot Team)",
    "Total Messages Across All AI Systems Reported", "# AI Tools Used (of 3)",
]
META_FIELDS = ["Job", "Org Level 1", "AI Champion?", "Claude (Pilot Team)"]

SIGNATURES = {
    "ChatGPT": {"User ID", "Email", "Credits", "Tokens"},
    "Copilot": {"User Principal Name", "Prompts submitted for All Apps",
                "Active Usage Days for All Apps"},
    "CoCounsel": {"email", "status", "new_conversations", "messages_sent"},
}
MONTHS = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]


def norm_email(s):
    return (s or "").strip().lower()


def num(s):
    """Parse a numeric CSV cell; None when blank/invalid."""
    try:
        return float(str(s).strip().replace(",", ""))
    except ValueError:
        return None


def fmt(n):
    if n is None:
        return ""
    n = round(float(n), 2)
    return str(int(n)) if n.is_integer() else str(n)


def read_csv(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def detect(folder):
    """Return {type: Path}, choosing the newest file for each CSV type."""
    found = {k: [] for k in SIGNATURES}
    for p in sorted(folder.glob("*.csv")):
        if p.name.lower().startswith("combined-"):
            continue
        with open(p, newline="", encoding="utf-8-sig") as f:
            header = set(next(csv.reader(f), []))
        for kind, sig in SIGNATURES.items():
            if sig <= header:
                found[kind].append(p)
    missing = [k for k, v in found.items() if not v]
    if missing:
        sys.exit(f"ERROR: could not identify a CSV for: {', '.join(missing)} in {folder}")
    result = {}
    for kind, paths in found.items():
        paths.sort(key=lambda p: p.stat().st_mtime)
        result[kind] = paths[-1]
        if len(paths) > 1:
            print(f"Note: {len(paths)} {kind} CSVs found, using newest: {paths[-1].name}")
    return result


def flip_name(name):
    """'First Middle Last' -> 'Last, First Middle' (leave alone if already flipped)."""
    name = (name or "").strip()
    if not name or "," in name:
        return name
    parts = name.split()
    if len(parts) < 2:
        return name
    return f"{parts[-1]}, {' '.join(parts[:-1])}"


def sheet_sort_key(title):
    m = re.match(r"combined\s+([a-z]+)\.?\s+(\d{2,4})", title.strip(), re.I)
    if not m or m.group(1)[:3].lower() not in MONTHS:
        return None
    year = int(m.group(2))
    year += 2000 if year < 100 else 0
    return (year, MONTHS.index(m.group(1)[:3].lower()))


def load_metadata(xlsx):
    """email -> {name, Job, Org Level 1, ...}, newest nonblank value wins."""
    try:
        import openpyxl
    except ImportError:
        print("WARNING: openpyxl not installed (pip install openpyxl); "
              "metadata will be left blank.")
        return {}
    wb = openpyxl.load_workbook(xlsx, read_only=True, data_only=True)
    sheets = [(sheet_sort_key(ws.title), ws) for ws in wb.worksheets]
    sheets = sorted((s for s in sheets if s[0]), key=lambda s: s[0], reverse=True)
    meta = {}
    for _, ws in sheets:
        header = None
        for row in ws.iter_rows(values_only=True):
            cells = ["" if c is None else str(c).strip() for c in row]
            if header is None:
                if "Employee Email" in cells:
                    header = {h: i for i, h in enumerate(cells)}
                continue
            email = norm_email(cells[header["Employee Email"]])
            if not email:
                continue
            rec = meta.setdefault(email, {})
            name = cells[header[COLUMNS[0]]] if COLUMNS[0] in header else ""
            if name and not rec.get("name"):
                rec["name"] = name
            for field in META_FIELDS:
                if field in header and cells[header[field]] and not rec.get(field):
                    rec[field] = cells[header[field]]
    print(f"Loaded metadata for {len(meta)} employees from {xlsx.name}")
    return meta


def output_suffix(files):
    """Month number shared by the filenames (e.g. chatgpt-09.csv), else today's."""
    nums = {m.group(1) for p in files for m in [re.search(r"(\d{2})(?=\.csv$)", p.name)] if m}
    return nums.pop() if len(nums) == 1 else datetime.now().strftime("%m")


def main():
    here = Path(__file__).resolve().parent
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("folder", nargs="?", default=here, type=Path, help="folder with the CSVs")
    ap.add_argument("--workbook", type=Path, help="prior workbook (default: AI Usage.xlsx in folder)")
    ap.add_argument("--output", type=Path, help="output CSV path")
    ap.add_argument("--credits-per-message", type=float, default=CREDITS_PER_MESSAGE)
    ap.add_argument("--exclude", nargs="*", default=sorted(EXCLUDED), help="emails to exclude")
    args = ap.parse_args()

    folder = args.folder.resolve()
    files = detect(folder)
    for kind, p in files.items():
        print(f"Detected {kind}: {p.name}")

    chatgpt = {norm_email(r["Email"]): r for r in read_csv(files["ChatGPT"]) if norm_email(r["Email"])}
    copilot = {norm_email(r["User Principal Name"]): r for r in read_csv(files["Copilot"])
               if norm_email(r["User Principal Name"])}
    cocounsel = {norm_email(r["email"]): r for r in read_csv(files["CoCounsel"]) if norm_email(r["email"])}

    xlsx = args.workbook or folder / "AI Usage.xlsx"
    meta = load_metadata(xlsx) if xlsx.exists() else {}
    if not meta:
        print("No prior workbook metadata available; Job/Org/Champion/Claude left blank.")

    excluded = {norm_email(e) for e in args.exclude}
    emails = (set(chatgpt) | set(copilot) | set(cocounsel)) - excluded

    rows, new_people = [], []
    for email in emails:
        g, c, k, m = chatgpt.get(email), copilot.get(email), cocounsel.get(email), meta.get(email, {})

        name = m.get("name") or flip_name(
            (g or {}).get("Name") or (c or {}).get("Display Name") or (k or {}).get("name") or email)

        credits = num(g["Credits"]) if g else None
        gpt_msgs = math.floor(credits / args.credits_per_message + 0.5) if credits is not None else None
        prompts = num(c["Prompts submitted for All Apps"]) if c else None
        days = num(c["Active Usage Days for All Apps"]) if c else None
        co_msgs = num(k["messages_sent"]) if k else None

        total = sum(v or 0 for v in (gpt_msgs, prompts, co_msgs))
        tools = sum(1 for v in (credits, prompts, co_msgs) if v and v > 0)

        if not m:
            new_people.append((name, email))
        rows.append([
            name, email, m.get("Job", ""), m.get("Org Level 1", ""), m.get("AI Champion?", ""),
            "Yes" if g else "", fmt(gpt_msgs), fmt(credits),
            "Yes" if c else "", fmt(prompts), fmt(days),
            "Yes" if k else "", fmt(co_msgs), m.get("Claude (Pilot Team)", ""),
            fmt(total), tools,
        ])

    rows.sort(key=lambda r: (-int(r[14]), r[0].lower()))

    out = args.output or folder / f"combined-{output_suffix(files.values())}.csv"
    with open(out, "w", newline="", encoding="utf-8-sig") as f:  # BOM so Excel opens it cleanly
        w = csv.writer(f)
        w.writerow(COLUMNS)
        w.writerows(rows)

    print(f"\nUnique employees: {len(rows)}")
    print(f"ChatGPT users:   {len(chatgpt)}")
    print(f"Copilot users:   {len(copilot)}")
    print(f"CoCounsel users: {len(cocounsel)}")
    print(f"New employees missing metadata: {len(new_people)}")
    print(f"Output: {out}")
    if new_people:
        print("\nNew employees needing Job / Org metadata:")
        for name, email in sorted(new_people):
            print(f"- {name} - {email}")


if __name__ == "__main__":
    main()
