"""
线程演示示例 2
线程函数传参  创建多个线程
"""
from threading import Thread
from time import sleep

# 含有参数的线程函数
def fun(sec,name):
    print("含有参数的线程函数")
    sleep(sec)
    print("%s 线程执行完毕"%name)

jobs = [] # 存储线程对象
for i in range(5):
    t = Thread(target=fun,args=(2,"tedu-%d"%i))
    jobs.append(t)
    t.start() # 启动线程

# 循环回收
for i in jobs:
    i.join()