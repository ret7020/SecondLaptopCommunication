import socket
import json

PASSWORD = "123"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000)) 
sock.send(json.dumps({"password": PASSWORD, "cmd": 0, "url": "https://yandex.ru"}).encode("utf-8"))
sock.close() 