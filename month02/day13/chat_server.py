"""
Author: Levi
Email: lvze@tedu.cn
Time: 2020-11-17
Env: Python 3.6
socket and Process exercise
"""
from socket import *

# 服务器地址
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

# 存储用户信息  {name:address}
user = {}

# 处理进入聊天室
def login(udp_socket,name,address):
    if name in user:
        udp_socket.sendto(b"FAIL",address)
    else:
        udp_socket.sendto(b"OK", address)
        # 通知其他人
        msg = "欢迎 %s 进入聊天室"%name
        for i in user:
            udp_socket.sendto(msg.encode(),user[i])
        # 存储用户
        user[name] = address
        print(user)

# 搭建基本结构，启动函数
def main():
    # UDP套接字
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(ADDR)
    # 循环接收请求,处理请求  (模型结构：一处接收，分情况讨论)
    while True:
        data,addr = udp_socket.recvfrom(1024)
        tmp = data.decode().split(" ") # 解析
        # 分情况讨论具体干什么
        if tmp[0] == "LOGIN":
            # tmp--> [LOGIN,name]
            login(udp_socket,tmp[1],addr)
        elif tmp[0] == "CHAT":
            pass
        elif tmp[0] == 'EXIT':
            pass

if __name__ == '__main__':
    main()
