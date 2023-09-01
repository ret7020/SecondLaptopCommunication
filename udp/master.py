import socket
import subprocess
import json

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    server.settimeout(0.2)
    server.bind(("", 44444))
    message = b"your very important message"
    while True:
        x, y = list(map(lambda c: int(int(c) / 1.5), subprocess.check_output(["hyprctl", "cursorpos"]).decode("utf-8").strip().split(", ")))
        payload = json.dumps(
            {"action": "cursor", "x": x, "y": y}
        )
        server.sendto(payload.encode("utf-8"), ("192.168.1.11", 37020))
