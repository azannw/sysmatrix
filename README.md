# SysMatrix - Linux System Monitor

SysMatrix is a command-line tool designed to monitor Linux system resources and perform basic security audits. It collects CPU, memory, and disk usage metrics, stores them in a local SQLite database, and checks for privileged user activity.

I built this tool to automate the tracking of server health and to provide quick visibility into system status without needing complex monitoring infrastructure.

## Features

- **Resource Monitoring:** Captures CPU load, memory usage, and disk space in real-time.
- **History Tracking:** Saves all metrics to a local SQLite database for historical analysis.
- **Security Auditing:** Lists users with sudo privileges and displays recent login history.
- **CLI Interface:** Simple command-line arguments to trigger different functions.
- **Cron Ready:** Designed to be scheduled via crontab for continuous background monitoring.

## Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/azanw/sysmatrix.git](https://github.com/azanw/sysmatrix.git)
   cd sysmatrix
