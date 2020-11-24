"""
线程属性示例
"""
from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target=fun,name = "Tedu")

t.setDaemon(True) # 该分支线程随主线程结束

t.start()

t.setName("tarena")
print("线程名:",t.getName())
print("is alive:",t.is_alive())
