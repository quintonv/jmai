# JMCo Monthly AI Usage Report - Process Specification

## Purpose

This document describes how to build the monthly combined JMCo AI usage dataset from three vendor CSV exports:

1. ChatGPT Enterprise
2. Microsoft Copilot
3. CoCounsel

The goal is to generate one combined CSV with the same columns used by the existing Excel workbook. The resulting CSV can be pasted into the new monthly `Combined <Month> 26` worksheet.

This specification is intended to be usable to generate either a Python script or a PowerShell script on another machine.

---

## Required monthly input files

The script should accept a folder containing the three CSV exports. Filenames do **not** matter. Identify each file from its column headers.

### 1. ChatGPT export

Identify the ChatGPT CSV when the header contains at least:

- `User ID`
- `Email`
- `Credits`
- `Tokens`

Example fields seen in the current export:

- Rank
- User ID
- Name
- Email
- Credits
- Estimated costs
- Estimated cost currency
- Tokens
- Lines of code

### 2. Microsoft Copilot export

Identify the Copilot CSV when the header contains at least:

- `User Principal Name`
- `Prompts submitted for All Apps`
- `Active Usage Days for All Apps`

Useful fields:

- User Principal Name
- Display Name
- Prompts submitted for All Apps
- Active Usage Days for All Apps

### 3. CoCounsel export

Identify the CoCounsel CSV when the header contains at least:

- `email`
- `status`
- `new_conversations`
- `messages_sent`

Useful fields:

- name
- email
- status
- messages_sent

---

## Optional prior workbook input

To automatically carry forward employee metadata, the script should also accept the latest AI Usage Excel workbook.

The prior workbook is used only for fields that are not available in the three vendor CSV files:

- Job
- Org Level 1
- AI Champion?
- Claude (Pilot Team)
- Preferred report display name

If the prior workbook is not supplied, leave these metadata columns blank for manual completion.

### Metadata lookup rule

Match employees using normalized email address.

Normalize an email by:

1. Trim leading/trailing whitespace.
2. Convert to lowercase.

Search the `Combined ...` monthly worksheets from **newest to oldest** and keep the newest nonblank value for each metadata field.

Do not assume worksheet position alone is always chronological. Prefer parsing the month/year from sheet names such as:

- `Combined Sept 26`
- `Combined Aug 26`
- `Combined July 26`

If a person is genuinely new and has no prior metadata, leave Job, Org Level 1, AI Champion?, and Claude blank. These will be entered manually.

---

## Default excluded accounts

Exclude these service/admin accounts from the combined employee report:

- `admin-tmb@jmco.com`
- `internaladmin@jmco.com`

Make the exclusion list configurable.

---

## Merge / join logic

Build the master user list as the union of all normalized email addresses appearing in any of the three monthly exports.

Join all data by normalized email address.

For each employee, use the previous workbook display name if available. Otherwise use a source display name and convert it to the report style where practical:

`First Middle Last` -> `Last, First Middle`

Do not attempt risky name matching when email is available. Email is the primary key.

---

## Output column order

Generate the following 16 columns in exactly this order:

1. `Employee Name (Last Suffix, First MI)`
2. `Employee Email`
3. `Job`
4. `Org Level 1`
5. `AI Champion?`
6. `ChatGPT Access`
7. `ChatGPT Messages`
8. `ChatGPT Credits`
9. `Copilot Access`
10. `Copilot Prompts - All Apps`
11. `Copilot Active Usage Days`
12. `CoCounsel Access`
13. `CoCounsel Messages`
14. `Claude (Pilot Team)`
15. `Total Messages Across All AI Systems Reported`
16. `# AI Tools Used (of 3)`

---

## Column mapping and calculations

### Employee Name

Source priority:

1. Prior workbook display name
2. ChatGPT `Name`
3. Copilot `Display Name`
4. CoCounsel `name`

For a new employee, convert source names to the report's `Last, First` style when possible.

### Employee Email

Use the normalized lowercase email address.

### Job

Carry forward from the newest available prior `Combined ...` worksheet.

If no prior value exists, leave blank.

### Org Level 1

Carry forward from the newest available prior `Combined ...` worksheet.

If no prior value exists, leave blank.

### AI Champion?

Carry forward from the newest available prior `Combined ...` worksheet.

Use the existing value, normally `Yes` or blank.

### ChatGPT Access

Set to `Yes` when the employee appears in the monthly ChatGPT CSV.

Otherwise leave blank.

### ChatGPT Credits

Direct mapping from ChatGPT CSV field:

`Credits`

Keep decimals if the export contains decimals.

### ChatGPT Messages

The current ChatGPT leaderboard CSV does **not** contain a message-count field.

Older workbook months such as June and July contained a direct `ChatGPT Messages` metric and a separate `ChatGPT Tool Message` metric. Beginning with the August-style export, the workbook instead contains `ChatGPT Credits`.

The August workbook values show a very consistent relationship of approximately:

`ChatGPT Messages = ROUND(ChatGPT Credits / 5.14)`

Examples from August:

- 5,710 credits -> 1,111 messages
- 5,665 credits -> 1,102 messages
- 5,061 credits -> 985 messages
- 4,784 credits -> 931 messages
- 2,070 credits -> 403 messages

Therefore the current working rule should be:

`ChatGPT Messages = ROUND(Credits / 5.14)`

### Important ChatGPT rate note

The ChatGPT export also has an `Estimated costs` field. In the current export:

`Estimated Cost = Credits * $0.04`

The `$0.04` value is therefore the **cost per credit**, not the message conversion rate.

The `5.14 credits per message` rule is inferred from the August workbook values because there is no visible Excel formula stored for those August ChatGPT message values. For safety, implement `5.14` as a configurable parameter such as:

- Python: `credits_per_message = 5.14`
- PowerShell: `$CreditsPerMessage = 5.14`

Then calculate:

`messages = round(credits / credits_per_message)`

If JMCo later provides an official message-conversion rule, replace this parameter rather than rewriting the script.

### Copilot Access

Set to `Yes` when the employee appears in the monthly Copilot CSV.

Otherwise leave blank.

### Copilot Prompts - All Apps

Direct mapping from:

`Prompts submitted for All Apps`

### Copilot Active Usage Days

Direct mapping from:

`Active Usage Days for All Apps`

### CoCounsel Access

Set to `Yes` when the employee appears in the monthly CoCounsel CSV, including users whose status is invited/active but who may have zero or blank messages.

Otherwise leave blank.

### CoCounsel Messages

Direct mapping from:

`messages_sent`

If the field is blank, keep it blank in the source-specific column. Treat it as zero only when calculating totals.

### Claude (Pilot Team)

Carry forward from the newest available prior `Combined ...` worksheet.

If no prior value exists, leave blank.

### Total Messages Across All AI Systems Reported

Calculate:

`ChatGPT Messages + Copilot Prompts - All Apps + CoCounsel Messages`

Treat blanks as zero for this calculation.

Equivalent Excel formula for row 5:

`=SUM(G5,J5,M5)`

### # AI Tools Used (of 3)

Count a tool only when there was positive usage during the month. Access alone does not count as tool usage.

Rules:

- ChatGPT counts as 1 if ChatGPT Credits > 0 (or derived ChatGPT Messages > 0).
- Copilot counts as 1 if Copilot Prompts - All Apps > 0.
- CoCounsel counts as 1 if CoCounsel Messages > 0.

Maximum value is 3.

Equivalent Excel logic:

`COUNTIF(ChatGPT Messages, ">0") + COUNTIF(Copilot Prompts, ">0") + COUNTIF(CoCounsel Messages, ">0")`

For a generated CSV, calculate the numeric value directly.

---

## Sorting

Sort the final output by:

1. `Total Messages Across All AI Systems Reported` descending
2. Employee Name ascending as a stable tie breaker

The existing monthly workbook is effectively presented from highest usage to lowest usage.

---

## Low-usage red rows in Excel

The August workbook uses a light red row fill for employees with fewer than 10 total messages/prompts.

Rule:

`Total Messages < 10`

A CSV cannot store row colors, so a CSV-only script should simply sort the rows correctly. The red fill can be applied later in Excel.

If generating XLSX directly, apply the existing light-red fill to the entire row when total messages are 0 through 9.

---

## Handling new employees

A new employee is someone present in one or more current-month CSVs but not found in previous `Combined ...` worksheets.

For a new employee:

- Populate name and email from the current exports.
- Populate all current usage fields normally.
- Leave Job blank.
- Leave Org Level 1 blank.
- Leave AI Champion? blank.
- Leave Claude (Pilot Team) blank.

At the end of the script, print a list of new employees requiring metadata completion.

Example console output:

```text
New employees needing Job / Org metadata:
- Smith, Jane - jane.smith@jmco.com
- Doe, John - john.doe@jmco.com
```

---

## Validation / safety checks

The script should stop with a clear error if:

- It cannot identify all three required CSV types.
- More than one CSV of the same type is detected in the input folder.
- A required identifying header has changed unexpectedly.

The script should print which files it detected, for example:

```text
Detected ChatGPT: chatgpt-10.csv
Detected Copilot: copilot-10.csv
Detected CoCounsel: cocounsel-10.csv
```

Also report:

- Number of unique employees generated
- Number of ChatGPT users
- Number of Copilot users
- Number of CoCounsel users
- Number of new employees with missing metadata
- Output file path

---

## Recommended CSV-only monthly workflow

This is the simplest option on a machine where code execution is allowed.

1. Export the monthly ChatGPT CSV.
2. Export the monthly Copilot CSV.
3. Export the monthly CoCounsel CSV.
4. Place the three CSVs in one folder.
5. Optionally place/provide the latest `AI Usage.xlsx` workbook so metadata can be carried forward.
6. Run the generated Python or PowerShell script.
7. The script produces a combined CSV with the 16 columns above.
8. Open the monthly Excel workbook.
9. Paste the generated rows into the new `Combined <Month> 26` sheet starting below the header row.
10. Fill Job/Org fields for any new employees printed by the script.
11. Apply the red low-usage formatting to rows where Total Messages < 10 if desired.
12. Save the workbook; this becomes the prior workbook for the next month.

---

## Recommended implementation notes

### Python

A CSV-only implementation can use only the Python standard library (`csv`) if prior Excel metadata is not needed.

If reading the prior `.xlsx` directly, use `openpyxl`.

### PowerShell

A CSV-only implementation can use built-in:

- `Import-Csv`
- `Export-Csv`

If reading the prior `.xlsx`, do **not** assume Excel COM automation is available on a locked-down machine. On a machine with desktop Excel installed and COM allowed, it can work, but it is not portable.

For maximum portability, another option is to maintain a small employee metadata CSV containing:

- Employee Email
- Employee Name
- Job
- Org Level 1
- AI Champion?
- Claude (Pilot Team)

Then the monthly PowerShell process can operate entirely on CSV files with no Excel dependency.

---

## Pseudocode

```text
load all CSV files in input folder

for each CSV:
    inspect headers
    detect as ChatGPT, Copilot, or CoCounsel

normalize all email addresses to lowercase

load prior employee metadata if provided

all_emails = union(
    ChatGPT emails,
    Copilot emails,
    CoCounsel emails
)

remove excluded admin/service accounts

for each email in all_emails:
    get ChatGPT record if present
    get Copilot record if present
    get CoCounsel record if present
    get prior metadata if present

    chatgpt_access = Yes if ChatGPT record exists else blank
    credits = ChatGPT.Credits if present
    chatgpt_messages = round(credits / 5.14) if credits exists else blank

    copilot_access = Yes if Copilot record exists else blank
    copilot_prompts = Copilot[Prompts submitted for All Apps]
    copilot_days = Copilot[Active Usage Days for All Apps]

    cocounsel_access = Yes if CoCounsel record exists else blank
    cocounsel_messages = CoCounsel.messages_sent

    total_messages =
        numeric(chatgpt_messages, 0) +
        numeric(copilot_prompts, 0) +
        numeric(cocounsel_messages, 0)

    tools_used = 0
    if credits > 0: tools_used += 1
    if copilot_prompts > 0: tools_used += 1
    if cocounsel_messages > 0: tools_used += 1

    output 16-column record

sort output by total_messages descending, name ascending
export combined CSV
print new employees missing prior metadata
```

---

## Current known assumptions

1. Email is the stable employee identifier across all three vendor exports.
2. ChatGPT Access means presence in the ChatGPT monthly export.
3. Copilot Access means presence in the Copilot monthly export.
4. CoCounsel Access means presence in the CoCounsel monthly export.
5. ChatGPT Messages for the current export format are estimated using `ROUND(Credits / 5.14)` based on the August workbook relationship.
6. `$0.04` in the ChatGPT export is cost per credit, not messages per credit.
7. Total Messages is ChatGPT Messages + Copilot prompts + CoCounsel messages.
8. AI Tools Used counts positive monthly usage, not merely licensed/access status.
9. New employee metadata is intentionally left blank for manual completion.
10. Low usage is defined as Total Messages < 10 for the red-row convention used in August.

