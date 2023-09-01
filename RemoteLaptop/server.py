import socket
from Xlib import X, display

display = display.Display()
screen = display.screen()
root = screen.root

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(("0.0.0.0", 9999))
    s.listen()
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        x, y = data.decode("utf-8").split(",")
        print(x, y)
        root.warp_pointer(x, y)
        display.sync()
