import socket  # used for network between two end points
import struct  # to handle data into a readable format
from datetime import datetime  # we need it for logs

sniffer = socket.socket(
    socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP
)  # sock_RAw -> Give access to packet bytes
# AF_INET -> IPV4
# IPROTO_TCP -> uses Tcp protocol

print("Packet sniffer(collecting) started....")

while True:
    raw_data, addr = sniffer.recvfrom(
        65535
    )  # this allow for 65535 bytes -> so we can receive any traffic as this size is huge
    ip_header = raw_data[
        :20
    ]  # extract the first 20 bytes (ip-header) this is the real ip header length (4 bytes * minimum length(5))
    h_ip = struct.unpack(
        "!BBHHHBBH4s4s", ip_header
    )  # unpack the ip_header(tuble) into the format we put into the "BBHHHBBH4s4s" thid put them together instead of being in a tuble

    src_ip = socket.inet_ntoa(
        h_ip[8]
    )  # convert binary data(packets) into dotted decimal format (human readable format)

    dst_ip = socket.inet_ntoa(h_ip[9])  # extract the destination ip from packet

    protocol =h_ip[
        6
    ]  # this is the number of protocol in packet (TCP) as we just receive TCP not any other ptotocols
    log_line = f"{datetime.now()}|{src_ip}|{dst_ip}|{protocol}\n"  # this prints out the logs to be appeared once socket found any packet
    print(log_line.strip())  # clean the logs by removing any white spaces
    with open("logs.txt", "a") as log:
        log.write(log_line)


socket.close()
