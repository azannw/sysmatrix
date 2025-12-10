import subprocess

def get_sudo_users():
    result = subprocess.getoutput("getent group sudo")
    return result

def get_last_logins(n=5):
    cmd = f"last -n {n}"
    result = subprocess.getoutput(cmd)
    return result
