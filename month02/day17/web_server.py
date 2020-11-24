"""
web server 程序

完成一个类，提供给使用者
使用者可以通过这个类 快速方便的搭建一个web服务展示自己的网页
"""
from socket import *
from select import select

class WebServer:
    def __init__(self, *, host="0.0.0.0", port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        # 将关注的IO存入列表
        self.rlist = []
        self.wlist = []
        self.xlist = []
        # 准备工作
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        self.sock = socket()
        self.sock.setblocking(False)

    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    # 连接客户端
    def connect(self,sockfd):
        connfd, addr = sockfd.accept()
        print("Connect from", addr)
        # 连接一个客户端就多监控一个
        connfd.setblocking(False)
        self.rlist.append(connfd)

    # 启动网络服务 --> IO 并发模型
    def start(self):
        self.sock.listen(5)
        self.rlist.append(self.sock) # 初始
        # 循环监控关注的IO
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            # 对监控的套接字就绪情况分情况讨论
            for r in rs:
                if r is self.sock:
                    self.connect(r)
                else:
                    # 某个浏览器发送http请求
                    self.handle(r)

    # 具体处理客户端请求
    def handle(self,connfd):
        request = connfd.recv(1024 * 10)
        print(request.decode())




if __name__ == '__main__':
    # 使用者怎么用？

    # 用户自己决定    地址 ip port  网页
    httpd = WebServer(host="0.0.0.0",port=8000,html="./static")

    # 启动服务
    httpd.start()