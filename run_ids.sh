#!/bin/bash
echo "[*] Starting IDS scan at $(date)"
echo "[*] Log file: $1"
python3 ids.py $1
echo "[*] Scan complete. Report saved."
mv ids_report.txt "ids_report_$(date +%Y%m%d_%H%M%S).txt"
echo "[*] Report renamed with timestamp."
