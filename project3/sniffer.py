import socket
import struct
from datetime import datetime
from parser import TCP_parser

sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
print("Packet sniffer started.....")

while True:
    raw_data, addr = sniffer.recvfrom(65535)
    IP_S, IP_D, P = TCP_parser(raw_data)
    log_line = f"{datetime.now()}|{IP_S}|{IP_D}|{P}\n"
    print(log_line.strip())
    with open("logs.txt", "a") as log:
        log.write(log_line)
