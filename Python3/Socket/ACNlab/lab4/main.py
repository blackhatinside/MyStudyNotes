import socket
import ntplib
import time

TIME1970 = 2208988800
DATA = '\x1b' + 47 * '\0'
NTPserver = "uk.pool.ntp.org"
NTPport = 123

def createSocket(serverSocket = None):
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.settimeout(200.0)  # setblocking(False)
    except socket.error as e:
        print("Error1: ", e)
    return serverSocket

def getNTPtime(NTPserver, NTPtime = None):
	try:
		client = ntplib.NTPClient()
		response = client.request(NTPserver, timeout = 5.0, version = 3)
		NTPtime = time.ctime(response.tx_time)
	except Exception as e:
		print("Error2: ", e)
	return NTPtime

def getsntpTime(NTPserver, NTPport, SNTPtime = None):
	try:
		clientSocket = createSocket()
		clientSocket.connect((NTPserver, NTPport))
		clientSocket.sendall(DATA.encode('utf-8'))  # clientSocket.sendto(data, address)
		responsedata, address = clientSocket.recvfrom(1024)
		SNTPtime = struct.unpack('!12I', responsedata)[10]
		SNTPtime -= TIME1970
		clientSocket.close()
	except Exception as e:
		print("Error3: ", e)
	return time.ctime(SNTPtime)

print("NTP time: ", getNTPtime(NTPserver))
print("SNTP time: ", getsntpTime(NTPserver, NTPport))
print("My Date of Birth: ", time.ctime(966101590))
