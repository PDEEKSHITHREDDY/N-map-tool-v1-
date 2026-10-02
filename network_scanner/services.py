import socket

def get_service(port):
    try:
        return socket.getservbyport(port)
    except:
        return "Unknown"


def grab_banner(target, port):
    try:
        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((target, port))
        sock.send(b"HELLO\r\n")
        banner = sock.recv(1024).decode(errors="ignore")
        sock.close()
        return banner.strip()
    except:
        return ""