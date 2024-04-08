import socket
hostname = socket.gethostname()
hostaddr = socket.gethosbyname(hostname)
hostdata = socket.gethostbyaddr(hostaddr)

print("Hostname: ", hostname)
print("Hostaddr: ", hostaddr)
print("Hostdata: ", hostdata)
