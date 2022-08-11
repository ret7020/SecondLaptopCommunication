import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
sock.bind(('', 55000)) 
sock.listen(10) 
print('Server is running, please, press ctrl+c to stop')
try:
    while True:
        conn, addr = sock.accept() 
        data = conn.recv(1024)
except KeyboardInterrupt:
    conn.close() 
