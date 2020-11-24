"""
同时创建多个子进程
"""
from multiprocessing import Process
from time import sleep
import os, sys


def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), "--", os.getpid())


def th2():
    sys.exit("睡觉进程结束了") # 终止
    sleep(2)
    print("睡觉")
    print(os.getppid(), "--", os.getpid())


def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(), "--", os.getpid())


# 循环创建进程
jobs = []
for th in [th1, th2, th3]:
    p = Process(target=th)
    jobs.append(p)  # 进程对象存起来
    p.start()

# 批量回收进程
[i.join() for i in jobs]
