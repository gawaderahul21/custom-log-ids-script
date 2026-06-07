import re
import sys
import os
from collections import defaultdict
from datetime import datetime

THRESHOLD_MEDIUM = 5
THRESHOLD_HIGH = 20
THRESHOLD_CRITICAL = 50
LOG_FILE = sys.argv[1] if len(sys.argv) > 1 else "auth.log"

print("=" * 60)
print("   CUSTOM LOG IDS — SSH Brute-Force Detector")
print("=" * 60)
print(f"[*] Reading log file: {LOG_FILE}")
print(f"[*] Thresholds: MEDIUM={THRESHOLD_MEDIUM} | HIGH={THRESHOLD_HIGH} | CRITICAL={THRESHOLD_CRITICAL}")
print()

if not os.path.exists(LOG_FILE):
    print(f"[ERROR] Log file '{LOG_FILE}' not found!")
    sys.exit(1)

failed_attempts = defaultdict(list)
total_lines = 0
matched_lines = 0

with open(LOG_FILE, "r", errors="ignore") as f:
    for line in f:
        total_lines += 1
        if "Failed password" in line:
            ip_match = re.search(r"from (\d+\.\d+\.\d+\.\d+)", line)
            user_match = re.search(r"Failed password for (\S+) from", line)
            if ip_match:
                ip = ip_match.group(1)
                user = user_match.group(1) if user_match else "unknown"
                failed_attempts[ip].append({
                    "user": user,
                    "line": line.strip()
                })
                matched_lines += 1

print(f"[*] Total log lines read : {total_lines}")
print(f"[*] Failed login entries : {matched_lines}")
print(f"[*] Unique attacker IPs  : {len(failed_attempts)}")
print()

alerts = []
for ip, attempts in failed_attempts.items():
    count = len(attempts)
    users = list(set(a["user"] for a in attempts))

    if count >= THRESHOLD_CRITICAL:
        severity = "CRITICAL"
    elif count >= THRESHOLD_HIGH:
        severity = "HIGH"
    elif count >= THRESHOLD_MEDIUM:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    alerts.append({
        "ip": ip,
        "count": count,
        "severity": severity,
        "users_targeted": users
    })

alerts.sort(key=lambda x: x["count"], reverse=True)

print("-" * 60)
print("   DETECTION RESULTS")
print("-" * 60)

for alert in alerts:
    sev = alert["severity"]
    marker = {"CRITICAL": "[!!!]", "HIGH": "[!! ]", "MEDIUM": "[ ! ]", "LOW": "[   ]"}.get(sev, "[ ? ]")
    print(f"{marker} {sev:<8} | IP: {alert['ip']:<15} | Attempts: {alert['count']:<5} | Users: {', '.join(alert['users_targeted'])}")

print()
print("-" * 60)

critical = [a for a in alerts if a["severity"] == "CRITICAL"]
high     = [a for a in alerts if a["severity"] == "HIGH"]
medium   = [a for a in alerts if a["severity"] == "MEDIUM"]
low      = [a for a in alerts if a["severity"] == "LOW"]

print(f"[SUMMARY] CRITICAL: {len(critical)} | HIGH: {len(high)} | MEDIUM: {len(medium)} | LOW: {len(low)}")
print()

report_file = "ids_report.txt"
with open(report_file, "w") as r:
    r.write("=" * 60 + "\n")
    r.write("   CUSTOM IDS REPORT\n")
    r.write(f"   Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    r.write(f"   Log file : {LOG_FILE}\n")
    r.write("=" * 60 + "\n\n")
    r.write(f"Total log lines    : {total_lines}\n")
    r.write(f"Failed login events: {matched_lines}\n")
    r.write(f"Unique attacker IPs: {len(failed_attempts)}\n\n")
    r.write("ALERTS:\n")
    r.write("-" * 60 + "\n")
    for alert in alerts:
        r.write(f"[{alert['severity']}] IP: {alert['ip']} | Attempts: {alert['count']} | Users targeted: {', '.join(alert['users_targeted'])}\n")
    r.write("\n")
    r.write(f"SUMMARY: CRITICAL={len(critical)} HIGH={len(high)} MEDIUM={len(medium)} LOW={len(low)}\n")

print(f"[*] Report saved to: {report_file}")
print("=" * 60)
