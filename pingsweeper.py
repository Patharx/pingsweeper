import subprocess
import socket
import datetime
import platform
from concurrent.futures import ThreadPoolExecutor, as_completed

def ping_host(ip):
    """
    Sends a single ping to an IP address and returns whether it's alive.
    
    We use subprocess to run the system's built-in ping command.
    subprocess lets Python run command line programs — like typing 
    a command in PowerShell but from inside your Python script!
    
    Windows ping: ping -n 1 -w 500 [ip]
    Linux ping:   ping -c 1 -w 1 [ip]
    -n 1 / -c 1 = send only 1 ping packet
    -w 500 / -w 1 = wait max 500ms for response
    """
    # Detect if we're on Windows or Linux/Mac
    # platform.system() returns "Windows", "Linux", or "Darwin" (Mac)
    system = platform.system().lower()
    
    if system == "windows":
        command = ["ping", "-n", "1", "-w", "500", ip]
    else:
        command = ["ping", "-c", "1", "-w", "1", ip]
    
    try:
        # subprocess.run() executes the command
        # stdout=subprocess.DEVNULL hides the ping output — we only care about success/fail
        # stderr=subprocess.DEVNULL hides any error messages too
        result = subprocess.run(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        # returncode 0 means success (host responded)
        # anything else means no response
        return ip, result.returncode == 0
    
    except subprocess.SubprocessError:
        return ip, False

def get_hostname(ip):
    """
    Tries to get the hostname of an IP address.
    This is called 'reverse DNS lookup' — converting an IP back to a name.
    For example 192.168.1.1 might resolve to 'router.home'
    """
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return "Unknown"

def sweep_network(network_base, start, end):
    """
    Sweeps a range of IP addresses to find live hosts.
    
    network_base = '192.168.1' (the first three parts of the IP)
    start/end = range of last numbers to scan (e.g. 1 to 254)
    
    We use ThreadPoolExecutor for multithreading —
    instead of pinging one host at a time (slow!),
    we ping many hosts simultaneously (fast!)
    Threading means running multiple tasks at the same time.
    """
    print("\n" + "=" * 55)
    print("🧙 GANDALF'S NETWORK PING SWEEPER")
    print("=" * 55)
    print(f"🔍 Scanning network: {network_base}.{start} - {network_base}.{end}")
    print(f"⏰ Started at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📡 Sending pings across the network...")
    print("-" * 55)

    # Build list of all IPs to scan
    targets = [f"{network_base}.{i}" for i in range(start, end + 1)]
    
    live_hosts = []
    scanned = 0
    total = len(targets)

    # ThreadPoolExecutor runs up to 50 pings simultaneously
    # This makes the scan ~50x faster than doing them one at a time!
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Submit all ping jobs at once
        futures = {executor.submit(ping_host, ip): ip for ip in targets}
        
        # Process results as they complete
        for future in as_completed(futures):
            ip, is_alive = future.result()
            scanned += 1
            
            # Show progress
            print(f"Progress: {scanned}/{total} hosts scanned...", end="\r")
            
            if is_alive:
                # Try to get the hostname of live hosts
                hostname = get_hostname(ip)
                live_hosts.append((ip, hostname))
                print(f"✅ {ip:16} — {hostname:30}          ")

    # Sort results by IP address for clean output
    live_hosts.sort(key=lambda x: list(map(int, x[0].split('.'))))

    # Print summary
    print("\n" + "=" * 55)
    print(f"✅ Scan complete!")
    print(f"⏰ Finished at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📋 Live hosts found: {len(live_hosts)}/{total}")
    print("-" * 55)

    if live_hosts:
        print(f"\n{'IP Address':<18} {'Hostname':<30}")
        print("-" * 55)
        for ip, hostname in live_hosts:
            print(f"{ip:<18} {hostname:<30}")
    else:
        print("No live hosts found in this range.")

    print("=" * 55)

    # Gandalf's verdict
    gandalf_reactions = [
        f"🧙 'I have surveyed the land — {len(live_hosts)} souls stir in this network!'",
        f"🧙 'Like the Eagles surveying Middle-earth — {len(live_hosts)} hosts stand ready!'",
        f"🧙 'The network reveals its secrets — {len(live_hosts)} living hosts discovered!'",
    ]
    
    import random
    print(f"\n{random.choice(gandalf_reactions)}\n")

def get_local_network():
    """
    Automatically detects your local network address.
    So you don't have to know your IP — the tool figures it out!
    """
    try:
        # Connect to a public DNS server to determine local IP
        # We don't actually send data — just use it to find our IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        local_ip = sock.getsockname()[0]
        sock.close()
        # Return just the network portion (first three octets)
        # e.g. '192.168.1.105' becomes '192.168.1'
        return ".".join(local_ip.split(".")[:3])
    except:
        return "192.168.1"

def main():
    print("🧙 GANDALF'S NETWORK PING SWEEPER")
    print("=" * 55)
    print("*gazes across the network like the Eye of Sauron*")
    print("Let us see who stirs in this digital Middle-earth...\n")

    # Auto detect local network
    detected_network = get_local_network()
    print(f"🔎 Detected local network: {detected_network}.x")

    network = input(f"Enter network base (press Enter for {detected_network}): ").strip()
    if not network:
        network = detected_network

    start = input("Start host (press Enter for 1): ").strip()
    start = int(start) if start else 1

    end = input("End host (press Enter for 254): ").strip()
    end = int(end) if end else 254

    sweep_network(network, start, end)

if __name__ == "__main__":
    main()