Network Mapper Tool — Documentation
Overview

This is a Python-based network mapping tool built during a cybersecurity bootcamp.
Its purpose is to discover live hosts on a network, scan open ports, and identify running services (banner grabbing).

It produces a JSON file (targets.json) that contains all discovered hosts, their IPs, MAC addresses, and open ports with service information.

The tool was built in a modular way and runs from the terminal.

Features

Host Discovery

Scans a subnet (e.g., 192.168.1.0/24) for live hosts using ARP requests.

Displays live hosts in a clean table with IP and MAC addresses.

Port Scanning

Scans common ports (21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3389) on each host.

Detects which ports are open.

Service Detection (Banner Grabbing)

Connects to each open port and reads any banner the service sends.

Helps identify the type and version of services (e.g., OpenSSH, Apache, FTP).

JSON Export

Saves all scan results in targets.json.

Each device entry contains:

{
  "ip": "192.168.1.1",
  "mac": "00:11:22:33:44:55",
  "open_ports": [
      {"port": 22, "service": "OpenSSH_8.9"},
      {"port": 80, "service": "Apache"}
  ]
}


Clean CLI Output

Uses rich library to display tables and colored messages.

Folder Structure
network_mapper/
│
├── mapper.py       # Main controller
├── discovery.py    # Host discovery functions
├── scanner.py      # Port scanning and banner grabbing functions
├── utils.py        # (Optional helpers)
├── targets.json    # Output file


For the bootcamp MVP, all code can run in mapper.py.

How It Works — Step by Step

Root Check

The tool checks if it’s run with sudo (root) because ARP scanning requires root permissions.

If not, it exits with a message.

Subnet Input & Validation

The user enters a subnet (e.g., 192.168.1.0/24).

The tool validates the format to prevent crashes.

Host Discovery

Sends ARP requests to all hosts in the subnet.

Receives responses and builds a list of live hosts.

Port Scanning

Loops through each host and checks a list of common TCP ports.

Uses socket connections to detect open ports.

Banner Grabbing

For each open port, connects and reads the first message sent by the service.

Saves this information to JSON.

Results Display & Export

Shows live hosts and their open ports in a formatted table.

Saves everything to targets.json for further use.

How to Run

Open terminal in the project folder:

cd network_mapper


Run the tool as root:

sudo python3 mapper.py


Enter the subnet when prompted:

Enter subnet (example 192.168.1.0/24): 192.168.1.0/24


Wait for results. You will see live hosts and open ports with banners.

The results are also saved in targets.json.

Libraries Used

scapy → For ARP scanning

socket → For TCP connections (port scanning & banner grabbing)

ipaddress → For subnet validation

rich → For CLI table and colored output

json → For saving scan results

Notes & Tips

Run with sudo or root privileges.

If no open ports are detected, check if your target hosts have firewalls.

The tool can be extended with multi-threading, UDP scanning, OS detection, or different scan profiles.                                                                                                                                                                                   