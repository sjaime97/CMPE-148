from socket import *
import sys
UDP_SERVER_PORT = 12345
UDP_SERVER_SOCKET = socket(AF_INET, SOCK_DGRAM) #Creates the UDP IP Socket
UDP_SERVER_SOCKET.bind(('', UDP_SERVER_PORT)) #binding IP to the port 
print("Server is waiting for client to connect...")

def leap(user_int):
    #creating a map within a list so each year
    #can be converted into an int 
    enter = list(map(int, user_int.split(" "))) 
    tmp = []
    for i in range(0, len(enter)):
        if(enter[i] % 4 == 0 or enter[i] % 100 == 0 or enter[i] % 400 == 0):
                s1 = str(enter[i]) + " is a leap year"
                tmp.append(s1)
        else:
            s2 = str(enter[i]) + " is NOT a leap year"
            tmp.append(s2)
    return '\n'.join(tmp)

while True:
    conn, addr = UDP_SERVER_SOCKET.recvfrom(2048)
    user = conn.decode('utf-8')
    try:
        if ((user != " ")):
              data = leap(user)
              UDP_SERVER_SOCKET.sendto(data.encode('utf-8'), addr)
    except ValueError:
        data = "One or more items in file is not a year"
        UDP_SERVER_SOCKET.sendto(data.encode('utf-8'), addr)

UDP_SERVER_SOCKET.close()
