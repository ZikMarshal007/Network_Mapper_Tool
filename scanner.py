import socket

def scan_ports(ip, ports):
    open_ports = []

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)

            result = sock.connect_ex((ip, port))

            if result == 0:
                open_ports.append(port)

            sock.close()

        except:
            pass

    return open_ports


def grab_banner(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))

        banner = s.recv(1024).decode(errors="ignore").strip()

        s.close()
        return banner

    except:
        return ""
