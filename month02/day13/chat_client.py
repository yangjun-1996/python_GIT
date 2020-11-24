"""
聊天室 客户端代码
"""

from socket import *
from multiprocessing import Process

# 服务器地址
ADDR = ("127.0.0.1",8888)

# 启动函数
def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)

    # 进入聊天室
    while True:
        name = input("请输入昵称:")
        msg = "LOGIN "+name
        udp_socket.sendto(msg.encode(),ADDR) # 发请求
        result,addr = udp_socket.recvfrom(128) # 收结果
        # OK 表示成功
        if result == b"OK":
            print("您已进入聊天室")
            break
        else:
            print("该用户已存在")


if __name__ == '__main__':
    main()