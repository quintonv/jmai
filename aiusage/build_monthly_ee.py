#!/usr/bin/env python3
"""Build the monthly usage CSV in the updated 14-column layout.

The Active Employee report is the master list. Name, Job and Org come from it;
AI Champion? and Claude (Pilot Team) are carried from the prior report.

    python build_monthly_ee.py <folder> --ee active-ee-10.xlsx --prior prior-usage-report-09.xlsx

ChatGPT Messages is filled from Tokens until the conversion rule is confirmed.
"""
import argparse
import csv
import sys
from pathlib import Path

import openpyxl

from build_monthly import detect, norm_email, num, fmt, read_csv

COLUMNS = [
    "Employee Name (Last Suffix, First MI)", "Employee Email", "Job", "Org Level 1",
    "AI Champion?", "ChatGPT Access", "ChatGPT Messages", "Copilot Access",
    "Copilot Prompts - All Apps", "Copilot Active Usage Days", "CoCounsel Access",
    "CoCounsel Messages", "Claude (Pilot Team)",
    "Total Messages Across All AI Systems Reported",
]


def sheet_rows(path, sheet=None):
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb[sheet] if sheet else wb.worksheets[0]
    header, out = None, []
    for row in ws.iter_rows(values_only=True):
        cells = ["" if c is None else str(c).strip() for c in row]
        if header is None:
            if "Employee Email" in cells:
                header = {h: i for i, h in enumerate(cells)}
            continue
        if cells[header["Employee Email"]]:
            out.append({h: cells[i] for h, i in header.items()})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder", type=Path)
    ap.add_argument("--ee", required=True, help="Active employee report (xlsx), in folder")
    ap.add_argument("--prior", required=True, help="Prior month report (xlsx), in folder")
    ap.add_argument("--output", type=Path)
    ap.add_argument("--exclude", nargs="*", default=["admin-tmb@jmco.com", "internaladmin@jmco.com"])
    a = ap.parse_args()
    folder = a.folder.resolve()

    files = detect(folder)
    for k, p in files.items():
        print(f"Detected {k}: {p.name}")
    g = {norm_email(r["Email"]): r for r in read_csv(files["ChatGPT"]) if norm_email(r["Email"])}
    c = {norm_email(r["User Principal Name"]): r for r in read_csv(files["Copilot"]) if norm_email(r["User Principal Name"])}
    k = {norm_email(r["email"]): r for r in read_csv(files["CoCounsel"]) if norm_email(r["email"])}

    ee = {norm_email(r["Employee Email"]): r for r in sheet_rows(folder / a.ee)}
    prior = {norm_email(r["Employee Email"]): r for r in sheet_rows(folder / a.prior)}

    rows = []
    for email, e in ee.items():
        gr, cr, kr = g.get(email), c.get(email), k.get(email)
        p = prior.get(email, {})
        gpt = num(gr["Tokens"]) if gr else None
        prompts = num(cr["Prompts submitted for All Apps"]) if cr else None
        days = num(cr["Active Usage Days for All Apps"]) if cr else None
        co = num(kr["messages_sent"]) if kr else None
        total = sum(v or 0 for v in (gpt, prompts, co))
        rows.append([
            e[COLUMNS[0]], email, e["Job"], e["Org Level 1"], p.get("AI Champion?", ""),
            "Yes" if gr else "", fmt(gpt), "Yes" if cr else "", fmt(prompts), fmt(days),
            "Yes" if kr else "", fmt(co), p.get("Claude (Pilot Team)", ""), total,
        ])

    rows.sort(key=lambda r: (-(num(r[6]) or 0), r[0].lower()))
    # Total as a formula so it recalculates when the ChatGPT column is replaced.
    # Written for CSV row n+2 (header on row 1); copy-paste in Excel shifts the references.
    for i, r in enumerate(rows):
        n = i + 2
        r[13] = f"=SUM(G{n},I{n},L{n})"

    out = a.output or folder / "combined-10.csv"
    with open(out, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f)
        w.writerow(COLUMNS)
        w.writerows(rows)

    excluded = {norm_email(x) for x in a.exclude}
    used = (set(g) | set(c) | set(k)) - excluded
    dropped = sorted(used - set(ee))
    new_unknown = sorted(e for e in dropped if e not in prior)
    print(f"\nRows written: {len(rows)} (EE employees: {len(ee)})")
    print(f"Output: {out}")
    print(f"\nHad usage but not on EE report, dropped ({len(dropped)}):")
    for e in dropped:
        print(" -", e, "(in prior report)" if e in prior else "(NOT in prior report: possible new contractor)")
    print(f"\nPossible new contractors (unknown to EE and prior report): {new_unknown or 'none'}")
    miss = [r[1] for r in rows if not r[2] or not r[3]]
    print(f"EE rows missing Job/Org: {miss or 'none'}")


if __name__ == "__main__":
    main()
