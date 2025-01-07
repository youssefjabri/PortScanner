# Python Port Scanner

This python script performs a **port scanning operation** to detect open ports on a target mpachine. it uses python's `socket` library for connection attempts and `ThreadPoolExecutor` for faster scanning through multithreading.

---


## How to use

1. install python
2. run the script
   
   ```
   py port_scanner.py
   ```
4. **Provide Input**  
   - Enter the target IP address (e.g., `111.222.3.4`).
   - Enter the port range in `start-end` format (e.g., `1-1000`).

---

## Example usage

### input:
```
Enter the target IP: 111.222.3.4
Enter the port range (e.g., 1-1000): 22-80
```

### output:
```
Scanning 192.168.1.1 for open ports in the range 22-80...

[+] Port 22 is open.
[+] Port 80 is open.

Scan completed.
Open Ports Found:
[+] Port 22 is open.
[+] Port 80 is open.
```

---

## Code explanation

1. **`scan_port(ip, port)`**  
   - attempts to connect to the specified ip and port.
   - if the connection succeeds, the port is reported as open.

2. **`scan_ports(ip, ports)`**  
   - accepts a list of ports and uses a thread pool to scan them concurrently.
   - collects and prints open ports.

3. **main logic**  
   - accepts user input for the target ip and port range.
   - iterates through the specified ports and displays results.
