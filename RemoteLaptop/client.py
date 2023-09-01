import socket
import subprocess
import time
import json

COEFF = 1.5
SERV = "192.168.1.11"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SERV, 9999))
    while True:
        x, y = list(map(lambda c: int(int(c) / 1.5), subprocess.check_output(["hyprctl", "cursorpos"]).decode("utf-8").strip().split(", ")))
        payload = f"{x},{y}".encode("utf-8")
        print(payload)
        s.sendall(payload)
        time.sleep(0.01)




