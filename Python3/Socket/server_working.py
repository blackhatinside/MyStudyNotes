import socket
import binascii

ADDR = "127.0.0.1" 
PORT = 5001

def createSocket():
	try:
		# for ipv4 AF_INET, for tcp SOCK_STREAM, for udp SOCK_DGRAM
		serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# False (0.0) non-blocking state, True (None) blocking state
		# serversocket.setblocking(False)
		# time in seconds, if 0.0 then non-blocking, if None then blocking
		serversocket.settimeout(200.0)
		# modify buffer size in bytes
		serversocket.setsockopt(socket.SOL_SOCKET, {
			socket.SO_SNDBUF: 4096,
			socket.SO_RCVBUF: 2048,
			socket.SO_REUSEADDR: 1
		})
		# reuse socket address
		serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	except socket.error as e:
		print("Error: ", e)
	finally:
		# socket.socket object
		return serversocket

if __name__ == '__main__':

	# str - hostname
	hostname = socket.gethostname()		# for local machine
	hostname = "www.google.com"		# for remote machine
	print("Hostname: ", hostname)

	# str - hostname to ipv4
	hostaddr = socket.gethostbyname(hostname)
	print("Hostaddr: ", hostaddr)

	# tup - (hostname, aliaslist, ipaddrlist)
	hostdata = socket.gethostbyaddr(hostaddr)
	print("Hostdata: ", hostdata)

	# binstr - hostaddr to binary string to hexadec
	hexaaddr = binascii.hexlify(socket.inet_aton(hostaddr))
	print("Hexaaddr: ", hexaaddr)

	# str - hexadec to binary string to hostaddr
	hostaddr = socket.inet_ntoa(binascii.unhexlify(hexaaddr))
	print("Hostaddr: ", hostaddr)

	for i in range(1, 101):
		try:
			# str - protocol; "tcp" - connection oriented, "udp" - connection less
			print("TCP: ", i, socket.getservbyport(i, "tcp"))
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
				# tup - (connection, clientaddress), where connection is a socket object
				connection, address = serversocket.accept()
				if connection:
					connectioncounter += 1
				print("Connection {} made to {}".format(connectioncounter, address))
				while True:
					# recvfrom: tuple - (bytes, clientaddress); recv: string - bytes
					fromclientdata = connection.recv(2048).decode()
					print("Client said: ", fromclientdata)
					if fromclientdata.strip().lower() == "bye":
						connection.send("Closing Connection #{}...".format(connectioncounter).encode('utf-8'))
						connection.close()
						break
					else:
						toclientdata = input("Enter msg for Client: ")
						# sendall: send large bytestream; send: send limited bytes
						connection.send(toclientdata.encode('utf-8'))
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
# tcp - send, sendall, recv
# udp - sendto, recvfrom