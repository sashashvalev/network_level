import socket
import hashlib

d = {}

sock = socket.socket()
sock.bind(('127.0.0.2', 9090))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:', addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    value = data
    hash = hashlib.md5()
    hash.update(data)
    key = hash
    d[key] = value
    print(d[key])
    conn.send(hash.digest())

conn.close()