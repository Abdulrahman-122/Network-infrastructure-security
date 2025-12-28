import socket

def Banner_grap(ip, ports):
    """Grab banner from TCP ports that are open."""
    banners = {}
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((ip, port))
            message = sock.recv(1024).decode(errors="ignore")
            banners[port] = message.strip()
            sock.close()
        except Exception:
            banners[port] = None
    return banners



# print(Banner_grap("192.168.1.5", [22, 80, 443, 3306, 8080]))
