from socket import *

tcp_soc = socket(AF_INET, SOCK_STREAM)

tcp_soc.connect(("0.0.0.0", 8888))
while True:
    tcp_soc.send(input("请输入：").encode())
    print(tcp_soc.recv(1024).decode())

tcp_soc.close()
