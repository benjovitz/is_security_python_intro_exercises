#!/usr/bin/python3

from socket import *
server_port = input("enter port: ")
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(('', int(server_port)))
server_socket.listen(1)
print("The server is ready to receive")

while True:
    conn_socket, client_address = server_socket.accept()
    modified_message = conn_socket.recv(2048).decode().upper()
    conn_socket.send(modified_message.encode())
    print("connection received from {}, and {} is sent back".format(client_address[1],modified_message))
    print("ip address:", client_address[0])
    conn_socket.close()
server_socket.close()
