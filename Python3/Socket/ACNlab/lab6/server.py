import socket

ADDR, PORT = "127.0.0.1", 5001

def createSocket(serverSocket = None):
	try:
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serverSocket.settimeout(200.0)
		# serverSocket.setblocking(False)
	except socket.error as e:
		print("Error1: ", e)
	return serverSocket

if __name__ == '__main__':
	serverSocket = createSocket()
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	stopflag = False
	connectioncounter = 0
	serverSocket.bind((ADDR, PORT))
	serverSocket.listen(5)
	print("Server Listening...")
	while not stopflag:
		try:
			connection, address = serverSocket.accept()
			if connection:
				connectioncounter += 1
				print("Connection #{} started".format(connectioncounter))
			while True:
				fromclientdata = connection.recv(4096).decode()
				print("Client said: {}".format(fromclientdata))
				if fromclientdata.strip().lower() == "bye":
					connection.send("Closing Connection #{}...".format(connectioncounter).encode('utf-8'))
					connection.close()
					break
				toclientdata = input("Enter msg for client: ")
				connection.send(toclientdata.encode('utf-8'))
				if toclientdata.strip().lower() == "bye":
					serverSocket.close()
					stopflag = True
		except KeyboardInterrupt:
			print("Forced Exit...")
			break
