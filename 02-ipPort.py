#!/usr/bin/python
ip_port = '192.168.0.1:443'
elements = ip_port.split(":")
ip = elements[0]
port = elements[1]

print('ip is', ip, 'and the port is', port)

print('ip is', ip_port.split(":")[0], 'and the port is', ip_port.split(":")[1])
