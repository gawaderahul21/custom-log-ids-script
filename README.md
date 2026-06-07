# Custom Log IDS Script

A Python-based Intrusion Detection System that parses SSH auth logs and detects brute-force attacks using threshold-based severity classification.

## Project Overview

Built a custom IDS tool from scratch in Python with no third-party SIEM needed. The script reads Linux SSH authentication logs, identifies brute-force patterns, classifies severity, and auto-generates timestamped reports.

Tested on real attack data from a live Hydra brute-force lab — 274 genuine failed SSH login attempts detected with zero false negatives.

## Tools and Technologies

- Python 3 — Main IDS script logic
- Bash — Automation wrapper script
- Regex — Log parsing and IP extraction
- Linux auth.log — SSH authentication log source
- Kali Linux — Development and testing platform

## Project Files

- ids.py — Main IDS detection script
- generate_logs.py — Synthetic log generator for testing
- run_ids.sh — Bash automation wrapper
- ids_report.txt — Sample detection report output
- screenshots/ — Project evidence screenshots

## How to Run

Clone the repo:
git clone https://github.com/gawaderahul21/custom-log-ids-script

Run on any auth.log file:
python3 ids.py auth.log

Or use the Bash wrapper:
./run_ids.sh auth.log

## Detection Logic

- LOW: 1 to 4 failed attempts — Possible mistype
- MEDIUM: 5 to 19 failed attempts — Suspicious activity
- HIGH: 20 to 49 failed attempts — Likely brute-force
- CRITICAL: 50 or more failed attempts — Active brute-force attack

## Results on Real Attack Data

- Log file: auth.log from live Hydra brute-force lab
- Total lines read: 1283
- Failed login events: 274
- Unique attacker IPs: 1
- Severity: CRITICAL
- Attacker IP: 10.0.2.15
- Accounts targeted: testuser, vboxuser

## Screenshots

IDS Running on real auth.log:
![IDS Running](screenshots/ids_running.png)

Detection Report saved automatically:
![IDS Report](screenshots/ids_report.png)

Project file structure:
![Project Files](screenshots/project_files.png)

## Resume Bullet Point

Custom Log IDS Script — Built a Python intrusion detection tool that parses SSH auth logs using regex, detects brute-force patterns with threshold-based severity classification (MEDIUM/HIGH/CRITICAL), auto-generates timestamped reports, and includes a Bash automation wrapper. Detected 274 real Hydra brute-force attempts across 2 accounts with zero false negatives.

Tech: Python, Bash, Linux auth logs, Regex, Kali Linux, GitHub

## Author

Rahul Gawade
Completed: June 2026
