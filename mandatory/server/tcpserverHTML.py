#!/usr/bin/python3

from socket import *
import sys
import datetime
server_port = sys.argv[1] or 3000
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_socket.bind(('', int(server_port)))
server_socket.listen(1)
print("The server is ready to receive")

http_header_ok = open("http-ok.txt", "r").read()
http_header_not_found = open("http-notfound.txt", "r").read()
html_not_found = open("not-found.html", "r").read()

html_not_found = http_header_not_found + html_not_found

def route_finder(route):
    route = route.split()
    route = route[1]
    if route == "/":
        html = open("index.html", "r").read()
        html = http_header_ok + html
        return html
    route = route[1::].lower()
    try:
        html = open(f"{route}.html", "r").read()
        html = http_header_ok + html
        return html
    except:
        return html_not_found

def add_log_entry(route, response):
     log_file = open("log.txt", "a")
     route = route.split()
     ip = route[4].split(":")
     log_entry = f"{ip[0]} - - [{datetime.datetime.now()}]"

while True:
    conn_socket, client_address = server_socket.accept()
    route = conn_socket.recv(2048).decode().upper()
    route = route_finder(route)
    conn_socket.send(route.encode())
    #print("connection received from {}, and {} is sent back".format(client_address[1], route))
    conn_socket.close()
server_socket.close()
