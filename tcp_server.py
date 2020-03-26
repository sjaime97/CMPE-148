from socket import *
import sys

TCP_SERVER_PORT = 12345
TCP_SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
TCP_SERVER_SOCKET.bind(('', TCP_SERVER_PORT))
TCP_SERVER_SOCKET.listen(1)
print('Server is connected and waiting for client...')

def leap(user_int):
    year = list(map(int, user_int.split(" ")))
    tmp = []
    for i in range(0, len(year)):
        if(year[i] % 4 == 0 or year[i] % 100 == 0 or year[i] % 400 == 0):
             s1 = str(year[i]) + " is a leap year"
             tmp.append(s1)
        else:
            s2 = str(year[i]) + " is NOT a leap year"
            tmp.append(s2)
    return '\n'.join(tmp)
while True:
    conn, addr = TCP_SERVER_SOCKET.accept()
    while True:
        user = conn.recv(1024)
        try:
            if ((user != " ")):
                  data = leap(user)
                  conn.send(data.encode('utf-8'))
        except ValueError:
            data = "One or more items in file is not a year"
            conn.send(data.encode('utf-8'))
                       
TCP_SERVER_SOCKET.close()
