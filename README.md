# SysMatrix - Linux System Monitor

**SysMatrix** is a lightweight, Python-based system administration tool designed for Linux environments. It monitors system health metrics (CPU, Memory, Disk), logs them to a local database, and performs security audits on user activity.

## Features
* **Real-time Collection:** Monitors system uptime, CPU load, and memory usage.
* **Data Persistence:** Uses SQLite (`data/sysmatrix.db`) to store historical metrics.
* **Security Auditing:** Tracks `sudo` users and recent login activity.
* **CLI Interface:** Simple command-line tools for administration.
* **Automation:** Designed to run via `cron` for background monitoring.

## Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/azanw/sysmatrix.git](https://github.com/azanw/sysmatrix.git)
    cd sysmatrix
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

**1. Collect Metrics (Run manually or via Cron)**
```bash
python3 sysmatrix.py collect
