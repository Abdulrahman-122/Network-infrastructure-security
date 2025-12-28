from ICMP_PING import ICMP_PING_IP
from run_parallel import run_parallel
from generate_ips import ips

def discover_hosts(subnet):
    """Discover alive hosts in the subnet using ICMP ping in parallel."""
    all_ips = ips(subnet)
    results = run_parallel(ICMP_PING_IP, all_ips)
    alive_hosts = [ip for ip, alive in results if alive]
    return alive_hosts
