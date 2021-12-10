#!/bin/python3
import socket


def main(ip, port, msg):
    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    # 发送消息给服务器
    sock.sendto(msg, (ip, port))

    # 接受服务器的消息
    print(sock.recvfrom(1024))


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 5005
    msg = b"I'm a client"
    main(ip, port, msg)
