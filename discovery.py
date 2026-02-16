from scapy.all import ARP, Ether, srp
from rich.console import Console

console = Console()

def scan_subnet(subnet):
    console.print(f"[bold cyan][+] Scanning subnet {subnet}[/bold cyan]\n")

    arp = ARP(pdst=subnet)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=False)[0]

    devices = []

    for sent, received in result:
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc
        })

    return devices
