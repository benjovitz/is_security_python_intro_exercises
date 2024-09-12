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


def route_finder(route):
    route = route.split()
    route = route[1]
    if route == "/":
        html = open("index.html", "r").read()
        html_with_header = http_header_ok + html
        return (html, html_with_header) 
    route = route[1::].lower()
    try:
        html = open(f"{route}.html", "r").read()
        html_with_header = http_header_ok + html
        return (html, html_with_header) 
    except:
        return (html_not_found, http_header_not_found + html_not_found)

def add_log_entry(request, payload, full_response):
     log_file = open("log.txt", "a")
     request = request.split()
     ip = request[4].split(":")
     full_response = full_response.split()
     log_entry = f'{ip[0]} - - [{datetime.datetime.now()}] "{request[0]} {request[1]} {request[2]}" {full_response[1]} {len(payload)} \r\n'
     log_file.write(log_entry)
     log_file.close()

while True:
    conn_socket, client_address = server_socket.accept()
    request = conn_socket.recv(2048).decode().upper()
    response = route_finder(request)
    add_log_entry(request, response[0], response[1])
    conn_socket.send(response[1].encode())
    conn_socket.close()
server_socket.close()
