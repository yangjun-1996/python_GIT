"""
基于 select 的 IO并发模型
select_server.py
重点代码！！！
"""

from socket import *
from select import select

# 创建全局变量
HOST = "0.0.0.0"
PORT = 8800
ADDR = (HOST, PORT)

# 创建套接字
sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)

# IO多路复用往往与非阻塞IO一起使用，防止传输过程的卡顿
sockfd.setblocking(False)

# 将关注的IO存入列表
rlist = [sockfd]  # 初始
wlist = []
xlist = []

# 循环监控关注的IO
while True:
    rs, ws, xs = select(rlist, wlist, xlist)
    # 对监控的套接字就绪情况分情况讨论
    for r in rs:
        if r is sockfd:
            connfd, addr = r.accept()
            print("Connect from", addr)
            # 连接一个客户端就多监控一个
            connfd.setblocking(False)
            rlist.append(connfd)
        else:
            # 某个客户端连接套接字就绪
            data = r.recv(1024).decode()
            # 客户端退出
            if not data:
                rlist.remove(r)  # 删除监控
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            wlist.append(r)  # 存入写列表

    for w in ws:
        w.send(b"OK")  # 回复消息
        wlist.remove(w)  # 删除
