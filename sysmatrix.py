import argparse
import time
import collector
import storage
import reports

def main():
    parser = argparse.ArgumentParser(description="SysMatrix monitoring tool")
    parser.add_argument("command", choices=["collect", "security", "view"], help="Action to perform")
    args = parser.parse_args()

    if args.command == "collect":
        storage.init_db()
        data = collector.collect_metrics()
        storage.save_sample(data)
        print(f"Sample saved: CPU {data['cpu_percent']}% | MEM {data['memory_percent']}%")

        # Simple Alerting System
        if data['cpu_percent'] > 80:
            print("WARNING: High CPU Usage detected!")
        if data['memory_percent'] > 90:
            print("WARNING: High Memory Usage detected!")

    elif args.command == "security":
        print(reports.security_report())

    elif args.command == "view":
        history = storage.fetch_history()
        print("\n=== SysMatrix Recent History (Last 10) ===")
        print(f"{'Time':<25} {'CPU%':<8} {'Mem%':<8} {'Disk%':<8}")
        print("-" * 55)
        for row in history:
            # Row structure: id, timestamp, cpu, mem, disk, uptime
            ts = time.ctime(row[1])
            print(f"{ts:<25} {row[2]:<8} {row[3]:<8} {row[4]:<8}")
        print("-" * 55)

if __name__ == "__main__":
    main()
