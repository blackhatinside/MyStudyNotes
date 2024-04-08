import socket

ADDR, PORT = "127.0.0.1", 5001

def createSocket(serverSocket = None):
	try:
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		serverSocket.settimeout(200.0)
	except socket.error as e:
		print("Error1: ", e)
	return serverSocket

if __name__ == '__main__':
	serverSocket = createSocket()
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
	serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	stopflag = False
	serverSocket.bind((ADDR, PORT))
	print("Server Listening...")
	while not stopflag:
		try:
			while True:
				fromclientdata, clientaddress = serverSocket.recvfrom(4096)
				fromclientdata = fromclientdata.decode()
				print("Client said: {}".format(fromclientdata))
				if fromclientdata.strip().lower() == "bye":
					serverSocket.sendto("Closing Connection...".encode('utf-8'), clientaddress)
					break
				toclientdata = fromclientdata
				serverSocket.sendto(toclientdata.encode('utf-8'), clientaddress)
				if toclientdata.strip().lower() == "bye":
					serverSocket.close()
					stopflag = True
					break
		except KeyboardInterrupt:
			print("Forced Exit...")
			break
