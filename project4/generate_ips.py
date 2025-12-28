import ipaddress

def ips(subnet):
    """Generate list of all usable IP addresses in the subnet."""
    network = ipaddress.ip_network(subnet, strict=False)
    return [str(ip) for ip in network.hosts()]


# print(ips("192.1.1.0/30"))
# hosts -> return list of hosts into this subnet  execlude (broadcast,network address from the return )
# ipaddress.ip_network -> this make Network object (contain on Networkadd, broadcast address,prefix_length)
# print(ips("192.1.1.0/24"))
