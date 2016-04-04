#!/usr/bin/python
import os
import sys
import socket

def returnBanner(ip, port):
    try:
        socket.setdefaulttimeout(3)
        soc = socket.socket()
        soc.connect((ip,port))
        banner = soc.recv(1024)
        return banner
    except Exception as e:
        print("[-] Error " + str(e))
        
def main():
    banner = returnBanner("192.168.1.1", 80)
    print(banner)
    
if __name__ == '__main__':
    main()