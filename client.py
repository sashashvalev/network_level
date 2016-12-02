import socket

print("vvod s")
s = str(input())
while s != '':

	sock = socket.socket()
	sock.connect(('127.0.0.2', 9090))
	sock.send(s.encode())

	data = sock.recv(1024)
	sock.close()

	print (data)

	s = str(input())
