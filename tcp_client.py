from socket import *
import sys
TCP_SERVER_NAME = ''
TCP_SERVER_PORT= 12345
CLIENT_SOCKET = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCKET.connect((TCP_SERVER_NAME, TCP_SERVER_PORT))

while True:
    leap = raw_input('Enter file or enter to exit: ')
    if (leap != ""):
        with open(leap, 'r') as f:
            leap = f.read(1024).decode('utf-8')
    else:
        sys.exit()
    CLIENT_SOCKET.send(leap.encode('utf-8'))
    data = CLIENT_SOCKET.recv(1024).decode('utf-8')
    print(data)
        
CLIENT_SOCKET.close()
