import subprocess

def ping_scan(network_prefix, start=1, end=254):
    output = []
    output.append(f"Scanning network {network_prefix}.{start}-{end}...")

    active_ips = []

    for i in range(start, end + 1):
        ip = f"{network_prefix}.{i}"

        try:
            response = subprocess.call(
                ['ping', '-c', '1', '-W', '1', ip],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            if response == 0:
                line = f"[+] {ip} is UP"
                output.append(line)
                active_ips.append(ip)

        except Exception:
            pass

    output.append(f"\nScan Complete. Found {len(active_ips)} active hosts.")

    return "\n".join(output), active_ips
