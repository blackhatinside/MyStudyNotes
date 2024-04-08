import socket

def createSocket(serverSocket = None):
	try:
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		serverSocket.settimeout(200.0)
	except socket.error as e:
		print("Error1: ", e)
	return serverSocket

serverSocket = createSocket()
print("Socket Timeout: {} seconds".format(serverSocket.gettimeout()))
