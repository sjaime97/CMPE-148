from socket import *
import sys
UDP_SERVER_PORT = 12345
UDP_SERVER_NAME = ''
s = socket(AF_INET, SOCK_DGRAM) #creating the client socket 
SERVER_ADDRESS = (UDP_SERVER_NAME, UDP_SERVER_PORT) ##creates the UDP server address

while True:
    leap = raw_input('Enter file or hit enter to exit: ')
    if (leap != ""):
        with open(leap, 'r') as f:
            leap = f.read()
    else:
        sys.exit()
    s.sendto(leap.encode('utf-8'), SERVER_ADDRESS)
    data, addr = s.recvfrom(2048)
    data = data.decode('utf-8')
    print(data)
        
s.close()
