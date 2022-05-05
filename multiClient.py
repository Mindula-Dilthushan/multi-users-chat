# project name   : multi users chat application
# project author : mindula dilthushan
# author email   : minduladilthushan1@gmail.com

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1001
try:
    client.connect((host, port))
except socket.error as e:
    print(str(e))

print('you connected to server...!')

while True:

    # user input data --------------------------------------------
    cl_msg = input("Enter message for server : ")
    client.send(cl_msg.encode('UTF-8'))

    # shutdown server --------------------------------------------
    if cl_msg == 'tata':
        break

    cl_msg = client.recv(1024)
    print("Server : ", cl_msg.decode('UTF-8'))

client.close()
