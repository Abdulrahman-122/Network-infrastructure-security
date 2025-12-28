import socket

def UDP_Scanner(host, ports, timeout=1):
    """Scan UDP ports on host, returns list of responding ports."""
    open_ports = []
    for port in ports:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.settimeout(timeout)
        try:
            client.sendto(b"Hello from Client", (host, port))
            data = client.recv(1024).decode(errors='ignore')
            open_ports.append(port)
        except socket.timeout:
            # No response usually means port is closed or filtered
            pass
        except Exception:
            pass
        finally:
            client.close()
    return open_ports


# host = "127.0.0.1"
# ports_to_scan = [53, 67, 123, 161]
# result = UDP_Scanner(host, ports_to_scan)
# print(f"Open or responding UDP ports on {host}: {result}")

# host = "127.0.0.1"
# ports = [80, 22, 443, 1]
# print('Check hosts now....', UDP_Scanner(host, ports))



