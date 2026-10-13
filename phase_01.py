
import subprocess
import ctypes
import sys

def run_as_admin():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(
            None,
            "runas",
            sys.executable,
            subprocess.list2cmdline(sys.argv),
            None,
            1
        )
        sys.exit()

run_as_admin()
title="NETWORK ANALYZER | PHASE 01 (LOCAL NETWORK SCANNER)"
print(title)
print("-"*len(title))

print("Running....")

clear_data = "arp -d *"
mapper = "arp -a"

subprocess.run(clear_data, shell=True)

total_ips = 254

for i in range(1, total_ips + 1):
    ip = f"192.168.1.{i}"

    subprocess.run(
        ["ping", "-n", "1", "-w", "500", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    percentage = (i / total_ips) * 100
    bar_length = 20
    filled = int(bar_length * i / total_ips)
    bar = "#" * filled + "-" * (bar_length - filled)

    print(
        f"\rScanning: [{bar}] {percentage:.1f}% "
        f"({i}/{total_ips})",
        end="",
        flush=True
    )

print("\n")
subprocess.run(mapper, shell=True)

print("\nScan completed.")
input("\nPress Enter to exit.")
