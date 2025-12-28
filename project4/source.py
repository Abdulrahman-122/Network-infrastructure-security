from ICMP_PING import ICMP_PING_IP
from Host_Discovery import discover_hosts
from Banner_grabber import Banner_grap
from generate_ips import ips
from udp_scanner import UDP_Scanner
from output import save_result
from tcp_scan import tcp_ping

def main():
    subnet = input("Enter the subnet you want to scan (e.g. 192.168.1.0/24): ")
    num_ports = int(input("Enter the number of ports you want to check: "))
    ports_num = []
    for i in range(num_ports):
        port = int(input(f"Enter port number {i+1}: "))
        ports_num.append(port)

    # Option 1: Discover active hosts in subnet
    print("Discovering active hosts in the subnet...")
    active_hosts = discover_hosts(subnet)
    print(f"Found {len(active_hosts)} active hosts.")

    # Option 2: Or just generate IPs (uncomment if you want to skip discovery)
    # active_hosts = ips(subnet)

    scan_results = []
    for host in active_hosts:
        print(f"\nScanning host {host}...")
        icmp_result = ICMP_PING_IP(host)
        udp_result = UDP_Scanner(host, ports_num)
        banner_result = Banner_grap(host, ports_num)
        scan_results.append({
            "Host": host,
            "ICMP_alive": icmp_result,
            "UDP_open_ports": udp_result,
            "Banner_grab": banner_result
        })

    save_result(scan_results)
    print("\nScan complete. Results saved to 'result.json'.")

main()