import socket
hostname = socket.gethostname()
hostaddr = socket.gethostbyname(hostname)
hostdata = socket.gethostbyaddr(hostaddr)

print("Hostname: ", hostname)
print("Hostaddr: ", hostaddr)
print("Hostdata: ", hostdata)
