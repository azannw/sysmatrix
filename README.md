# SysMatrix Linux System Monitor

SysMatrix is a command line tool that monitors Linux system resources and performs basic security audits. It collects CPU, memory, and disk usage metrics, stores them in a local SQLite database, and checks for privileged user activity.

The goal is to provide quick insight into system health without installing large monitoring stacks.

## Features

- Resource monitoring for CPU load, memory usage, and disk space
- History tracking through a local SQLite database
- Security auditing of sudo users and recent login history
- Simple command line interface
- Supports cron scheduling for automatic monitoring

## Installation

Clone the repository:

```bash
git clone [https://github.com/azanw/sysmatrix.git](https://github.com/azanw/sysmatrix.git)
cd sysmatrix
````

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## How to Use

The tool is controlled through `sysmatrix.py`. A typical workflow is to collect data and later view it.

### 1\. Collect metrics

Captures the current system status and saves it into the database.

```bash
python3 sysmatrix.py collect
```

### 2\. View history

Shows the last recorded entries in a readable table. This helps track usage over time.

```bash
python3 sysmatrix.py view
```

### 3\. Security report

Displays sudo users and recent login activity.

```bash
python3 sysmatrix.py security
```

## Automation

To run the collector in the background every minute, open the crontab:

```bash
crontab -e
```

Then add:

```bash
* * * * * cd /path/to/sysmatrix && /usr/bin/python3 sysmatrix.py collect >> sysmatrix.log 2>&1
```

This keeps your history updated automatically.

## Project Structure

```text
sysmatrix.py     Main entry point and CLI handler
collector.py     Collects system metrics using psutil
storage.py       Handles SQLite database logic
reports.py       Produces security reports and formatted views
data/            Stores the SQLite database
```

```
