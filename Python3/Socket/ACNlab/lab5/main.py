import socket

def createSocket(serverSocket = None):
	try:
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serverSocket.settimeout(200.0)
		serverSocket.setblocking(False)
	except socket.error as e:
		print("Error1: ", e)
	return serverSocket

serverSocket = createSocket()
print("Old Send Buffer Size: {}".format(serverSocket.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)))
print("Old Receive Buffer Size: {}".format(serverSocket.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)))
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 4096)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 4096)
print("New Send Buffer Size: {}".format(serverSocket.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)))
print("New Receive Buffer Size: {}".format(serverSocket.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)))
