"""
tcp 套接字循环模型 1
重点代码 ！！！
"""
from socket import *
import time

# 创建tcp套接字
tcp_socket = socket(AF_INET,SOCK_STREAM)

# 绑定地址
tcp_socket.bind(("0.0.0.0",8888))

# 设置监听套接字
tcp_socket.listen(5)

# 循环等待处理客户端连接
while True:
    print("Waiting for connect...")
    connfd,addr = tcp_socket.accept()
    print("Connect from",addr)

    # 循环收发数据
    while True:
        data = connfd.recv(5)
        # data 为空表示客户端close 断开
        if not data:
            break

        # 接收到## 表示客户端退出
        # if data == b"##":
        #     break
        print("Receive:",data.decode())
        connfd.send(b"Thanks#") # 人为设置消息边界
        # time.sleep(0.1) # 延迟发送

    connfd.close()

# 关闭
tcp_socket.close()


