import socket, server

try:
	clientsocket = server.createSocket()
	fromserverdata = toserverdata = ""
	while True:
		if "bye" in (fromserverdata.strip().lower(), toserverdata.strip().lower()):
			print("Ending Connection...")
			clientsocket.close()
			break
		toserverdata = input("Enter msg for Server: ")
		clientsocket.sendto(toserverdata.encode('utf-8'), (server.ADDR, server.PORT))
		fromserverdata, serveraddress = clientsocket.recvfrom(2048)
		fromserverdata = fromserverdata.decode()
		print("Server said: ", fromserverdata)
except KeyboardInterrupt:
	print("Forced Exit(Closing Client... ): ")
except Exception as e2:
	print("Error2: ", e2)
