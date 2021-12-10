#!/bin/python3
import socket


def main(ip, port):

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    sock.bind((ip, port))

    print("listen...")
    while True:
        # 接受客户端消息
        msg, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print("received message: %s" % msg)

        # 发送消息给客户端
        sock.sendto(b'hello client', addr)


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 5005
    main(ip, port)
