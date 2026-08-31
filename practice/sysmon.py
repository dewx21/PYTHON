def to_gb(kb_string):
    return int(kb_string) / 1024 / 1024

try:
    with open("/proc/meminfo") as f:
        mem = {line.split(":")[0]: line.split()[1] for line in f}

    total = to_gb(mem['MemTotal'])
    available = to_gb(mem['MemAvailable'])
    used = total - available

    print(f"Total memory:     {total:.2f} GB")
    print(f"Used memory:      {used:.2f} GB")
    print(f"Available memory: {available:.2f} GB")
except FileNotFoundError:
    print("/proc/meminfo not found — are you on Linux?")
except PermissionError:
    print("No permission to read /proc/meminfo")