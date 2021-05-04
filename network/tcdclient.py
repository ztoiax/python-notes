#!/bin/python3
from socket import socket


def main():
    ip = '127.0.0.1'
    port = 6666

    client = socket()
    client.connect((ip, port))
    print(client.recv(1024).decode('utf-8'))
    client.close()


if __name__ == '__main__':
    main()
