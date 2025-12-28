import socket

def ICMP_PING_IP(ip, timeout=1):
    """Send an ICMP echo request (ping) to check if host is alive."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
        sock.settimeout(timeout)
        # ICMP echo request packet (type=8, code=0)
        packet = b'\x08\x00\xf7\xff'  # simple fixed packet, can be improved
        sock.sendto(packet, (ip, 1))
        sock.recvfrom(1024)
        sock.close()
        return True
    except socket.timeout:
        return False
    except PermissionError:
        print("Error: ICMP requires root/administrator privileges.")
        return False
    except Exception as e:
        print(f"ICMP error: {e}")
        return False

# while True:
#     print("***Enter your IP you want to send ICMP_packet to ***")
#     ip = input("Enter ip?")
#     result = ICMP_PING_IP(ip)
#     if result == True:
#         print("Host is alive")

#     else:
#         print("Host is dead")

#     quit = input("Enter q to quit>")
#     if quit == "q":
#         break
