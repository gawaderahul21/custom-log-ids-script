---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/gawaderahul21/custom-log-ids-script

# Run on any auth.log file
python3 ids.py auth.log

# Or use the Bash wrapper
./run_ids.sh auth.log
```

---

## 🔍 Detection Logic

| Severity | Threshold | Meaning |
|----------|-----------|---------|
| LOW | 1-4 failed attempts | Possible mistype |
| MEDIUM | 5-19 failed attempts | Suspicious activity |
| HIGH | 20-49 failed attempts | Likely brute-force |
| CRITICAL | 50+ failed attempts | Active brute-force attack |

---

## 📊 Results on Real Attack Data

- **Log file:** auth.log (from live Hydra brute-force lab)
- **Total lines read:** 1283
- **Failed login events:** 274
- **Unique attacker IPs:** 1
- **Severity:** CRITICAL
- **Attacker IP:** 10.0.2.15
- **Accounts targeted:** testuser, vboxuser

### Screenshot: IDS Running
![IDS Running](screenshots/ids_running.png)

### Screenshot: Detection Report
![IDS Report](screenshots/ids_report.png)

---

## 📄 Resume Bullet Point

> **Custom Log IDS Script** — Built a Python intrusion detection tool that parses SSH auth logs using regex, detects brute-force patterns with threshold-based severity classification (MEDIUM/HIGH/CRITICAL), auto-generates timestamped reports, and includes a Bash automation wrapper. Detected 274 real Hydra brute-force attempts across 2 accounts with zero false negatives.
>
> *Tech: Python, Bash, Linux auth logs, Regex, Kali Linux, GitHub*

---

## 👤 Author
**Rahul Gawade**
Completed: June 2026
