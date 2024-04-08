import socket, server

try:
	clientsocket = server.createSocket()
	clientsocket.connect((server.ADDR, server.PORT))
	fromserverdata = toserverdata = ""
	while True:
		if "bye" in (fromserverdata.strip().lower(), toserverdata.strip().lower()):
			print("Ending Connection...")
			clientsocket.close()
			break
		toserverdata = input("Enter msg for Server: ")
		clientsocket.send(toserverdata.encode('utf-8'))
		fromserverdata = clientsocket.recv(2048).decode()
		print("Server said: ", fromserverdata)
except KeyboardInterrupt:
	print("Forced Exit(Closing Client... ): ")
except Exception as e2:
	print("Error2: ", e2)
