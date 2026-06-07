import random
from datetime import datetime, timedelta

attackers = ["10.0.2.15", "192.168.1.100", "172.16.0.5"]
normal_users = ["alice", "bob"]
attack_user = "testuser"

lines = []
base_time = datetime(2026, 5, 24, 13, 40, 0)

for i in range(300):
    ip = random.choice(attackers)
    t = base_time + timedelta(seconds=i * 0.5)
    ts = t.strftime("%Y-%m-%dT%H:%M:%S.000000+00:00")
    pid = random.randint(3500, 3600)
    line = f"{ts} Ubuntu sshd[{pid}]: Failed password for {attack_user} from {ip} port {random.randint(30000,60000)} ssh2"
    lines.append(line)

for i in range(10):
    ip = "10.0.3.20"
    t = base_time + timedelta(minutes=5, seconds=i * 30)
    ts = t.strftime("%Y-%m-%dT%H:%M:%S.000000+00:00")
    user = random.choice(normal_users)
    line = f"{ts} Ubuntu sshd[9999]: Failed password for {user} from {ip} port 22 ssh2"
    lines.append(line)

random.shuffle(lines)

with open("sample_auth.log", "w") as f:
    f.write("\n".join(lines))

print(f"Generated {len(lines)} log entries in sample_auth.log")
