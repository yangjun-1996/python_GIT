"""
练习2： 用两个分支线程分别打印 A-Z 和 1-52
两个线程启动后 打印顺序为  12A34B56C....5152Z

提示： 一个程序中不一定用一个锁
"""
from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release()

def print_chr():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_chr)

lock2.acquire() # 先把lock2锁住

t1.start()
t2.start()
t1.join()
t2.join()
