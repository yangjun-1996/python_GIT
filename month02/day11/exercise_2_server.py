"""

练习2： 通过客户端向服务端发送问题，服务端返回对应的回答
得到答案打印出来，要求可以同时启动多个客户端
关键字与对应答案在文件chat.txt中
服务端：  小美

我: 你好啊
小美： 你好
"""
from socket import *
import re

filename = "./chat.txt"

# 将chat文件内容生成字典
def chat_dict():
    file = open(filename)
    list_ = []
    for line in file:
        # [(key,answer)]
        res = re.findall(r"(\S+)\s+(.+)",line)
        list_ += res
    file.close()
    return dict(list_) # 生成字典

# 通过问题获取答案
def answer(request):
    for key in chat:
        # 如果关键词在问题中就给答案
        if key in request:
            return chat[key]
    return "人家还小不知道啦！"


def main():
    # 创建tcp套接字
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    tcp_socket.bind(("0.0.0.0",8888))
    tcp_socket.listen(5)

    # 循环等待处理客户端
    while True:
        connfd,addr = tcp_socket.accept()
        # 来自客户端的提问
        data = connfd.recv(1024)
        # 获取答案
        result = answer(data.decode())
        connfd.send(result.encode())
        connfd.close()
    # 关闭
    tcp_socket.close()

if __name__ == '__main__':
    chat = chat_dict()
    main()
