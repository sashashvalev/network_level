import socket

d = {}
print("input str")
value = str(input())
while value != '':

	sock = socket.socket()
	sock.connect(('127.0.0.2', 9090))
	sock.send(value.encode())

	key = sock.recv(1024)
	sock.close()
	d[key] = value
	for key in d:
        print(key, ' ', d[key])

	print("input str")
	value = str(input())