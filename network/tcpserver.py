#!/bin/python3
from socket import socket, SOCK_STREAM, AF_INET


def main(ip, port):
    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind((ip, port))
    # 512队列大小
    server.listen(512)
    print("listen...")

    while True:
        # 有连接就输出信息
        client, addr = server.accept()
        print(str(addr) + ' connect')

        # 接受客户端的消息
        msg = client.recv(1024).decode('utf-8')
        print("received message: %s" % msg)

        # 发送消息给客户端
        client.send(b"hello client")
        client.close()


if __name__ == '__main__':
    ip = '127.0.0.1'
    port = 6666
    main(ip, port)
