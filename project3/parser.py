import socket
import struct

def TCP_parser(raw_data):
    """A function used to serve sniffer to parse TCP packets from traffic"""
    
    
    IP_h_tuple = raw_data[:20]

    IP_h_ordered = struct.unpack("!BBHHHBBH4s4s", IP_h_tuple)

    ip_source = socket.inet_ntoa(IP_h_ordered[8])

    ip_destination = socket.inet_ntoa(IP_h_ordered[9])

    protocol = IP_h_ordered[6]

    return ip_source, ip_destination, protocol
