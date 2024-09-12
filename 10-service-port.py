#!/usr/bin/python
import sys

if sys.argv[1] == '-proto':
	print('Port: 80')
	print('Name: HTTP')
	print('Transport layer protocol: tcp')
	print('Description: World Wide Web HTTP')
elif sys.argv[1] == '-p':
	print('Port: 22')
	print('Name: SSH')
	print('Transport layer protocol: tcp')
	print('Description: The Secure Shell (SSH) Protocol')
