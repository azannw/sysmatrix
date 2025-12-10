import time
import collector


def security_report():
    report = []
    report.append("=== SysMatrix Security Report ===")
    report.append(f"Generated at: {time.ctime()}")
    report.append("")

    # sudo group
    sudo_users = collector.get_sudo_users()
    report.append("=== Sudo Users ===")
    report.append(sudo_users)
    report.append("")

    # last logins
    last_logins = collector.get_last_logins(5)
    report.append("=== Recent Login Activity ===")
    report.append(last_logins)
    report.append("")

    return "\n".join(report)


if __name__ == "__main__":
    print(security_report())
