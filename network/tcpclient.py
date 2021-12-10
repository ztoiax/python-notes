#!/bin/python3
from socket import socket


def main(ip, port, msg):
    client = socket()
    client.connect((ip, port))

    # 发送消息给服务器
    client.send(msg)
    # 接受服务器的消息
    print('server: ' + client.recv(1024).decode('utf-8'))

    client.close()


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 6666
    msg = b"I'm a client"
    main(ip, port, msg)
