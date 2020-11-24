"""
自定义线程类
"""
from threading import Thread
import time

class MyThread(Thread):
    def __init__(self,song):
        self.song = song
        super().__init__()

    def run(self):
        for i in range(3):
            print("playig %s:%s"%(self.song,time.ctime()))
            time.sleep(2)

t = MyThread("凉凉")
t.start() # run作为线程执行
t.join()
