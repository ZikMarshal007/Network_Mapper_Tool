#!/usr/bin/env python3

import os
import sys
import ipaddress
import json
from rich.console import Console
from rich.table import Table

from discovery import scan_subnet
from scanner import scan_ports, grab_banner

console = Console()

def display_results(devices):
    table = Table(title="Live Hosts Discovered")

    table.add_column("IP Address", style="green")
    table.add_column("MAC Address", style="yellow")

    for device in devices:
        table.add_row(device["ip"], device["mac"])

    console.print(table)


def main():
    if os.geteuid() != 0:
        console.print("[red][!] Please run as root (sudo)[/red]")
        sys.exit()

    subnet = console.input("Enter subnet (example 192.168.1.0/24): ")

    try:
        ipaddress.ip_network(subnet, strict=False)
    except ValueError:
        console.print("[red][!] Invalid subnet format[/red]")
        sys.exit()

    devices = scan_subnet(subnet)

    common_ports = [21,22,23,25,53,80,110,139,143,443,445,3389]

    if devices:
        display_results(devices)

        for device in devices:
            ip = device["ip"]
            console.print(f"\nScanning ports on {ip}...")

            open_ports = scan_ports(ip, common_ports)
            device["open_ports"] = []

            for port in open_ports:
                banner = grab_banner(ip, port)

                device["open_ports"].append({
                    "port": port,
                    "service": banner
                })

                console.print(f"OPEN {port} | {banner}")

        with open("targets.json", "w") as f:
            json.dump(devices, f, indent=4)

        console.print("[green][+] Results saved to targets.json[/green]")

    else:
        console.print("[red][-] No live hosts found.[/red]")


if __name__ == "__main__":
    main()

