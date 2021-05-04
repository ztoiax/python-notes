#!/bin/python3
from socket import socket, SOCK_STREAM, AF_INET


def main():
    ip = '127.0.0.1'
    port = 6666

    server = socket(family=AF_INET, type=SOCK_STREAM)
    server.bind((ip, port))
    # 512队列大小
    server.listen(512)
    print("listen...")
    while True:
        client, addr = server.accept()
        print(str(addr) + ' connect')
        # 发送客户端的消息
        client.send('hello client'.encode('utf-8'))
        client.close()


if __name__ == '__main__':
    main()
