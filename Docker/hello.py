import socket

print("Hello World")
fuxuandi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

fuxuandi.bind(('0.0.0.0', 3000))
fuxuandi.listen(5)


while True:
	try:
		(conn, address) = fuxuandi.accept() 
		conn.sendall("".decode("utf-8"))
	except:
		break
