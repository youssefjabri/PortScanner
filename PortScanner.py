import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            s.connect((ip, port))
            return f"[+] Port {port} is open."
    except:
        return None

def scan_ports(ip, ports):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda port: scan_port(ip, port), ports)
        for result in results:
            if result:
                print(result)
                open_ports.append(result)
    return open_ports

if __name__ == "__main__":
    target_ip = input("Enter the target IP: ").strip()
    port_range = input("Enter the port range (e.g., 1-1000): ").strip()

    try:
        start_port, end_port = map(int, port_range.split("-"))
        ports_to_scan = range(start_port, end_port + 1)
        
        print(f"Scanning {target_ip} for open ports in the range {start_port}-{end_port}...\n")
        results = scan_ports(target_ip, ports_to_scan)
        print("\nScan completed.")
        if results:
            print(f"Open Ports Found:\n" + "\n".join(results))
        else:
            print("No open ports found.")
    except ValueError:
        print("Invalid port range. Please enter in the format: start-end")