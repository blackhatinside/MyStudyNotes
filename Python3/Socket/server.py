import socket
import binascii

ADDR, PORT = "127.0.0.1", 5001

def createSocket():
	try:
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4 - socket.AF_INET, udp - SOCK_DGRAM
		serversocket.settimeout(200.0)	# 0.0 - non-blocking, None - blocking
		# serversocket.setblocking(False)
		serversocket.setsockopt(socket.SOL_SOCKET, {
			socket.SO_SNDBUF: 4096,	# bytes
			socket.SO_RCVBUF: 2048,
			socket.SO_REUSEADDR: 1 # reuse socket address
		})
	except socket.error as e:
		print("Error: ", e)
	finally:
		return serversocket	# socket.socket object

if __name__ == '__main__':
	hostname = socket.gethostname()				# for local machine; # for remote machine - "www.google.com"
	print("Hostname: ", hostname)
	hostaddr = socket.gethostbyname(hostname)	# str - hostname to ipv4
	print("Hostaddr: ", hostaddr)
	hostdata = socket.gethostbyaddr(hostaddr)	# tup - (hostname, aliaslist, ipaddrlist)
	print("Hostdata: ", hostdata)
	hexaaddr = binascii.hexlify(socket.inet_aton(hostaddr))	# str to binstr(bytes) to hexadec(bytes)
	print("Hexaaddr: ", hexaaddr)
	hostaddr = socket.inet_ntoa(binascii.unhexlify(hexaaddr))	# hexadec to binstr to str
	print("Hostaddr: ", hostaddr)

	for i in range(1, 101):
		try:
			print("TCP: ", i, socket.getservbyport(i, "tcp"))	# str - protocol; "tcp", "udp"
		except:
			continue

	try:
		serversocket = createSocket()
		# url = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(hostname)
		serversocket.bind((ADDR, PORT))
		serversocket.listen(2)	# 2 -  no. of unaccepted connections to allow
		print("Started Server. Listening on {}...".format((ADDR, PORT)))
		connectioncounter = 0
		stopflag = False
		while not stopflag:
			try:
				# accept: (connection <==> socket.socket object, clientaddress)
				connection, address = serversocket.accept()
				if connection:
					connectioncounter += 1
				print("Connection {} made to {}".format(connectioncounter, address))
				while True:
					# recvfrom: (bytes, clientaddress); recv: bytesstring
					fromclientdata = connection.recv(2048).decode()
					print("Client said: ", fromclientdata)
					if fromclientdata.strip().lower() == "bye":
						connection.send("Closing Connection #{}...".format(connectioncounter).encode('utf-8'))
						connection.close()
						break
					else:
						toclientdata = input("Enter msg for Client: ")
						connection.send(toclientdata.encode('utf-8'))	# sendall(large bytes); send(limited bytes)
						if toclientdata.strip().lower() == "bye":
							print("Closing Server...")
							stopflag = True
							break
			except Exception as e2:
				print("Forced Exit(Closing Server... ): ", e2)
				break
		serversocket.close()
	except Exception as e1:
		print("Error1: ", e1)

# server - socket(), bind(), listen() [TCP], accept() [TCP]
# client - socket(), connect() [TCP], sendall(), recv()
