"""
消息队列使用
"""

from multiprocessing import Process,Queue

#　创建消息队列
q = Queue(3)

def request():
    name = "Abby"
    passwd = "xxxxx"
    #　存入消息队列
    q.put(name)
    q.put(passwd)

def handle():
    #　获取消息队列消息
    print(q.get())
    print(q.get())

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()

