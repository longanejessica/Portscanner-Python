import socket
import sys

# BANNER LIB
from colorama import Fore, Style, init
init(autoreset=True)


# BANNER CALL CODE PARAMETERS
colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def print_rainbow_banner():
    banner_lines = [
        "   ██▓███   ▒█████   ██▀███  ▄▄▄█████▓     ██████  ▄████▄   ▄▄▄       ███▄    █  ███▄    █ ▓█████  ██▀███     ▓█████  ███▄    █  ██░ ██  ▄▄▄       ███▄    █  ▄████▄  ▓█████ ▓█████▄ ",
        "  ▓██░  ██▒▒██▒  ██▒▓██ ▒ ██▒▓  ██▒ ▓▒   ▒██    ▒ ▒██▀ ▀█  ▒████▄     ██ ▀█   █  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒   ▓█   ▀  ██ ▀█   █ ▓██░ ██▒▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▓█   ▀ ▒██▀ ██▌",
        "  ▓██░ ██▓▒▒██░  ██▒▓██ ░▄█ ▒▒ ▓██░ ▒░   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██  ▀█ ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒   ▒███   ▓██  ▀█ ██▒▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒███   ░██   █▌",
        "  ▒██▄█▓▒ ▒▒██   ██░▒██▀▀█▄  ░ ▓██▓ ░      ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▓██▒  ▐▌██▒▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄     ▒▓█  ▄ ▓██▒  ▐▌██▒░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒▓█  ▄ ░▓█▄   ▌",
        "  ▒██▒ ░  ░░ ████▓▒░░██▓ ▒██▒  ▒██▒ ░    ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██░   ▓██░▒██░   ▓██░░▒████▒░██▓ ▒██▒   ░▒████▒▒██░   ▓██░░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░░▒████▒░▒████▓ ",
        "  ▒▓▒░ ░  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░  ▒ ░░      ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░   ░░ ▒░ ░░ ▒░   ▒ ▒  ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░░ ▒░ ░ ▒▒▓  ▒ ",
        "  ░▒ ░       ░ ▒ ▒░   ░▒ ░ ▒░    ░       ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░ ░░   ░ ▒░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░    ░ ░  ░░ ░░   ░ ▒░ ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒    ░ ░  ░ ░ ▒  ▒ ",
        "  ░░       ░ ░ ░ ▒    ░░   ░   ░         ░  ░  ░  ░          ░   ▒      ░   ░ ░    ░   ░ ░    ░     ░░   ░       ░      ░   ░ ░  ░  ░░ ░  ░   ▒      ░   ░ ░ ░           ░    ░ ░  ░ ",
        "              ░ ░     ░                       ░  ░ ░            ░  ░         ░          ░    ░  ░   ░           ░  ░         ░  ░  ░  ░      ░  ░         ░ ░ ░         ░  ░   ░    ",
        "                                                 ░                                                                                                          ░                ░"
    ]

    for i, line in enumerate(banner_lines):
        print(colors[i % len(colors)] + Style.BRIGHT + line)

# ----------------BANNER CALL----------------
print_rainbow_banner()

#----------------PASSWORD PARAMETERS ----------------
SECRET_PASSWORD = "mysecretpassword" 

print(Fore.RED + f"--- Access Required ---")
entered_password = input(Fore.CYAN + "Enter password: ").strip()

if entered_password != SECRET_PASSWORD:
    print(Fore.RED + "[ACCESS DENIED] Incorrect password. Exiting.")
    sys.exit(1)
else:
    print(Fore.GREEN + "[ACCESS GRANTED] Password correct. Proceeding.")

#----------------LOG FILE----------------

LOG_FILE = "enhanced_port_scanner.log"

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(message + "\n")

#---------------- IP VALIDATION----------------
def validate_ip(ip_str):
    try:
        socket.inet_aton(ip_str)
        msg = Fore.GREEN + f"[OK] Valid IP address: {ip_str}"
        print(msg)
        log(msg)
        return True
    except socket.error:
        msg = Fore.RED + f"[ERROR] Invalid IP address: {ip_str}"
        print(msg)
        log(msg)
        return False
#----------------PORT VALIDATION----------------

def validate_ports(start_port, end_port):
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        print(Fore.RED + "[ERROR] Ports must be between 1 and 65535.")
        log(Fore.RED + "[ERROR] Invalid port range.")
        sys.exit(1)
    if start_port > end_port:
        print(Fore.RED + "[ERROR] Start port must be less than or equal to end port.")
        log(Fore.RED + "[ERROR] Start port is greater than end port.")
        sys.exit(1)
    msg = f"[OK] Valid port range: {start_port}-{end_port}"
    print(msg)
    log(msg)
#----------------PORT SCANNING ----------------
def scan_port(host, port, timeout=1):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        s.connect((host, port))
        msg = Fore.GREEN + f"[OPEN] Port {port} is open on {host}"
        print(msg)
        log(msg)
        s.close()
        return True
    except socket.gaierror:
        msg = Fore.RED + f"[ERROR] Failed to resolve host: {host}"
        print(msg)
        log(msg)
    except socket.timeout:
        msg = Fore.YELLOW + f"[TIMEOUT] Connection to port {port} timed out."
        print(msg)
        log(msg)
    except socket.error as err:
        msg = Fore.RED + f"[SOCKET ERROR] Port {port}: {err}"
        print(msg)
        log(msg)
    except Exception as e:
        msg = f"[EXCEPTION] Port {port}: {e}"
        print(msg)
        log(msg)
    return False

def scan_host(host, start_port, end_port):
    header = Fore.GREEN + f"\n--- Scanning {host} from port {start_port} to {end_port} ---"
    print(header)
    log(header)
    for port in range(start_port, end_port + 1):
        scan_port(host, port)

host = input(Fore.CYAN + f"Enter IP address to scan: ").strip()
if not validate_ip(host):
    sys.exit(1)

try:
    start = int(input(Fore.CYAN + f"Enter start port: "))
    end = int(input(Fore.CYAN + f"Enter end port: "))
    validate_ports(start, end)
    scan_host(host, start, end)
except ValueError:
    msg = Fore.RED + f"[ERROR] Please enter valid numbers for ports."
    print(msg)
    log(msg)
    sys.exit(1)