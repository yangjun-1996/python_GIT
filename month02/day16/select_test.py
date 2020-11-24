"""
select IO 多路复用方法处理
"""
from socket import *
from select import select

# 准备几个IO对象
tcp_socket = socket()
tcp_socket.bind(("0.0.0.0",8888))
tcp_socket.listen(5)

udp_socket = socket(AF_INET,SOCK_DGRAM)

file = open("my.log","rb")

# 监控IO
print("开始监控IO啦")
rs,ws,xs = select([file,udp_socket],[file,udp_socket,tcp_socket],[])
print("rlist:",rs)
print("wlist:",ws)
print("xlist:",xs)

# 处理IO行为

