# project name   : multi users chat application
# project author : mindula dilthushan
# author email   : minduladilthushan1@gmail.com

import socket
import os
from _thread import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 1001
thred = 0

try:
    server.bind((host, port))
except socket.error as e:
    print(str(e))

server.listen(5)

print('waiting for a client...!')


def client_connection(connection):
    while True:
        ser_msg = client.recv(2048).decode('UTF-8')
        print(clientAddress, ":", ser_msg)

        # shutdown server --------------------------------------------
        if ser_msg == 'tata':
            break


while True:
    client, clientAddress = server.accept()
    print('connected : ', clientAddress[0], str(clientAddress[1]))

    start_new_thread(client_connection, (client,))
    thred += 1

    print("Client ID : " + str(thred))

server.close()