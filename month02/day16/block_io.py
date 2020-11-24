"""
非阻塞IO演示
"""
from socket import *
import time

log = open("my.log",'a') # 日志

# 创建tcp套接字
sockfd = socket()
sockfd.bind(("0.0.0.0",8888))
sockfd.listen(5)

# 设置套接字对象为非阻塞
# sockfd.setblocking(False)

# 设置超时
sockfd.settimeout(3)

# 循环连接
while True:
    try:
        print("Waiting for connect")
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except BlockingIOError as e:
        time.sleep(2)
        msg = "%s : %s\n"%(time.ctime(),e)
        log.write(msg)
    except timeout as e:
        msg = "%s : %s\n" % (time.ctime(), e)
        log.write(msg)
    else:
        # 需要先连接再操作的IO
        data = connfd.recv(1024)
        print(data.decode())

