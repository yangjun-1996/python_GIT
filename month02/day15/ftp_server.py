"""
ftp 服务端模型
"""

from socket import *
from threading import Thread
import sys

# 服务端地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

FTP = "/home/tarena/FTP/" # 文件库

class FTPServer(Thread):
    def __init__(self,connfd):
        self.connfd = connfd
        super().__init__(daemon=True) # 使用父类

    def do_list(self):
        pass

    def do_get(self):
        pass

    # 客户端处理函数
    def run(self):
        # 循环接收请求，调用不同的方法处理
        while True:
            data = self.connfd.recv(1024).decode()
            #　解析请求
            tmp = data.split(' ')
            # 分情况讨论
            if tmp[0] == "LIST":
                self.do_list()
            elif tmp[0] == "GET":
                pass
            elif tmp[0] == "PUT":
                pass
            elif tmp[0] == "EXIT":
                pass
        self.connfd.close()  # 函数结束 即分支线程结束

# 启动函数
def main():
    # tcp套接字
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("Listen the port %d..." % PORT)

    # 循环处理客户端连接
    while True:
        try:
            connfd, addr = sock.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            sock.close()
            sys.exit("服务退出！")

        # 处理客户端事务
        t = FTPServer(connfd)
        t.start()


if __name__ == '__main__':
    main()  # 启动服务
