import socket
import json
from Xlib import display

display = display.Display()
screen = display.screen()
root = screen.root

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    client.bind(("", 37020))
    while True:
        data, addr = client.recvfrom(1024)
        data = json.loads(data.decode("utf-8"))
        if data["action"] == "cursor":
            x, y = data["x"], data["y"]
            root.warp_pointer(x, y)
            display.sync()
