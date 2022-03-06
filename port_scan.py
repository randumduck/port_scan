#!/usr/bin/python3
import sys
import socket

host = sys.argv[1]
s = socket.socket()

def scan(port):
    try:
        s.connect((host,port))
        return True
    except:
        return False
for i in range(20,30):  #change the range value to check for different ports
    if scan(i):
        print("Port {} is open".format(i))
    else:
        print("Port {} is closed".format(i))
