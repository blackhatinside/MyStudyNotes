import socket
import binascii

hostname = socket.gethostname()
hostaddr = socket.gethostbyname(hostname)

hexaaddr = binascii.hexlify(socket.inet_aton(hostaddr))
print("Hexaaddr: ", hexaaddr)

hostaddr = socket.inet_ntoa(binascii.unhexlify(hexaaddr))
print("Hostaddr: ", hostaddr)

for i in range(1, 1001):
	try:
		print("Port {}: {}".format(i, socket.getservbyport(i, "tcp")))
	except:
		continue
