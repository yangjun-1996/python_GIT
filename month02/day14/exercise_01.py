"""
练习1： 模拟一个售票系统
现在有500张票  T1--T500  将票放入列表
创建10个线程 记为 w1 -- w10 模拟10个买票机器
10个线程同时买票知道所有票卖完为止
票按照顺序卖出，每张票出票时间为0.1秒

打印 w5----T203 表示票卖出
"""
from threading import Thread
from time import sleep

# 500张票
ticket = ["T%d" % x for x in range(1, 501)]

# 线程函数干什么 ->买票过程
def sell(w):
    while ticket:
        # pop弹出一项
        print("%s --- %s"%(w,ticket.pop(0)))
        sleep(0.1)


jobs = []
# 循环创建多线程
for i in range(1,11):
    t = Thread(target=sell,args=("w%d"%i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]






