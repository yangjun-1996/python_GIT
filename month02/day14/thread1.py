"""
线程 创建示例
"""

import threading
from time import sleep
import os

a = 1 # 全局变量

# 线程执行函数
def music():
    global a
    print("a = ", a)
    a = 10000
    for i in range(3):
        sleep(2)
        print(os.getpid(),"播放： 葫芦娃")

# 创建线程
t = threading.Thread(target=music)
# 启动线程
t.start()

# 主线程继续执行
for i in range(4):
    sleep(1)
    print(os.getpid(),"播放：eight")


# 等待回收线程
t.join()
print("a:",a) # 10000