"""
ftp文件服务客户端
"""

from socket import *

# 服务器地址
ADDR = ("0.0.0.0",8888)

# 客户端发起请求的功能 --》 风格与服务端保持统一
class FTPClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd

    def do_list(self):
        pass

    def do_get(self,filename):
        pass

# 连接网络
def main():
    sock = socket()
    sock.connect(ADDR)

    ftp = FTPClient(sock) # 实例化对象用于调用方法

    while True:
        print("======== 命令选项 =========")
        print("****     list        ****")
        print("****   get file      ****")
        print("****   put file      ****")
        print("****     exit        ****")
        print("===========================")

        cmd = input("请输入命令：") # 选择功能
        if cmd == "list":
            ftp.do_list()
        elif cmd[:3] == "get":
            pass

if __name__ == '__main__':
    main()
