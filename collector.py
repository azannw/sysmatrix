import psutil
import time
import os

def collect_metrics():
    data = {}
    data["timestamp"] = int(time.time())
    data["cpu_percent"] = psutil.cpu_percent(interval=1)
    data["memory_percent"] = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/")
    data["disk_percent"] = disk.percent

    # uptime estimate (seconds since boot)
    data["uptime_seconds"] = int(time.time() - psutil.boot_time())

    return data

import subprocess

def get_sudo_users():
    result = subprocess.getoutput("getent group sudo")
    return result

def get_last_logins(n=5):
    cmd = f"last -n {n}"
    result = subprocess.getoutput(cmd)
    return result




if __name__ == "__main__":
    print(collect_metrics())
