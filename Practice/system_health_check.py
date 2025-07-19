
import psutil
import time
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
log_file = os.path.join(log_dir, f"health_log_{timestamp}.txt")

cpu_usage = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

log_message = f"""
System Health Check - {time.strftime("%Y-%m-%d %H:%M:%S")}
------------------------------------------------------------
CPU Usage      : {cpu_usage}%
Memory Usage   : {memory.percent}% (Total: {memory.total // (1024 ** 2)} MB)
Disk Usage     : {disk.percent}% (Free: {disk.free // (1024 ** 3)} GB)

"""

with open(log_file, "w") as f:
    f.write(log_message)

print(log_message)
print(f"✅ Health check log saved to {log_file}")
