"""
线程锁 示例
"""
from threading import Thread, Lock


lock = Lock() # 创建锁对象

a = b = 0

# 线程函数
def value():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print("a = %d,b = %d" % (a, b))
        lock.release() # 解锁

t = Thread(target=value)
t.start()

while True:
    with lock: # 上锁
        a += 1
        b += 1
               # 语句块结束解锁

t.join()