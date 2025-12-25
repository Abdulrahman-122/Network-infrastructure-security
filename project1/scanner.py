import socket


def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    return result == 0


def main():
    target = input("Target IP or hostname:")
    print(f"scanning {target}")
    for port in range(1, 1025):
        if scan_port(target, port):
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")


if __name__ == "__main__":
    main()
