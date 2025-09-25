import socket

def scan_ports(target_ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[Python] Port {port} is open.")
            open_ports.append(port)
        s.close()
    return open_ports

if __name__ == "__main__":
    target_ip = "127.0.0.1"
    start_port = 20
    end_port = 100
    scan_ports(target_ip, start_port, end_port)

# ================================
#  SCAN COMPLÉMENTAIRE AVEC NMAP
# ================================
try:
    import nmap

    def scan_with_nmap(target, port_range="20-100"):
        scanner = nmap.PortScanner()
        print(f"\n[+] Scanning {target} ports {port_range} with Nmap...")
        scanner.scan(target, port_range)

        for host in scanner.all_hosts():
            print(f"Host: {host}")
            for proto in scanner[host].all_protocols():
                ports = scanner[host][proto].keys()
                for port in sorted(ports):
                    state = scanner[host][proto][port]['state']
                    print(f"  [Nmap] Port {port} : {state}")

    if __name__ == "__main__":
        # Appel complémentaire de Nmap
        scan_with_nmap(target_ip, "20-100")

except ImportError:
    print("\n[!] Le module 'nmap' n'est pas installé. Pour l’utiliser, fais : pip install python-nmap")
