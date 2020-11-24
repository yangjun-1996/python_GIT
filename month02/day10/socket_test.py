"""
套接字函数使用
"""
import socket

# 创建一个udp套接字
udp_sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

# 用网络IP地址   客户端访问使用：172.40.0.84
udp_sock.bind(("172.40.0.84",8888))

# 本地测试IP地址  127.0.0.1 == localhost
# 客户端访问使用：127.0.0.1
# udp_sock.bind(("127.0.0.1",8888))

# 0.0.0.0 == 172.40.0.84 + 127.0.0.1
# 客户端在其他主机上访问使用：172.40.0.84
# 客户端在本地主机上访问使用：127.0.0.1
# udp_sock.bind(("0.0.0.0",8888))


