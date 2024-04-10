import socket

ADDR, PORT = "127.0.0.1", 5001

def createSocket(serverSocket = None):
    try:
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.settimeout(200.0)
    except socket.error as e:
        print("Error1: ", e)
    return serverSocket

connectioncounter = 0
hostname = socket.gethostname()
hostaddr = socket.gethostbyname(hostname)
serverSocket = createSocket()
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serverSocket.bind((ADDR, PORT))
serverSocket.listen(5)
print("Server is listening...")
while True:
    try:
        connection, address = serverSocket.accept()
        htmlcode = """
          <html>
              <title>
                  Socket Programming
              </title>
              <body>
                  <h1">
                      Hello {} ({})
                  </h1>
                  <p>
                      You visited this page <span style="color:red;"> {}</span> times :) 
                  </p>
              </body>
            </html>
            """.format(hostname, hostaddr, connectioncounter)
        urlcode = 'HTTP/1.0 200 OK\nContent-Type: text/html\n\n{}'.format(htmlcode).encode()
        connection.send(urlcode)
        connection.close()
        connectioncounter += 1
    except Exception as e:
        print("Error1: ", e)
    except KeyboardInterrupt:
        print("Forced Exit...")
        break
