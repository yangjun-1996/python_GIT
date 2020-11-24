"""
event 同步互斥方法示例
"""
from threading import Thread ,Event

msg = None # 线程通信
e = Event() # event对象

# 线程函数
def 杨子荣():
    print("杨子荣前来拜山头")
    global msg
    msg = "天王盖地虎"
    e.set() # 通知可以进行判断

t = Thread(target=杨子荣)
t.start()

print("说对口令就是自己人")
e.wait() # 等待通知
if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神你是对的人")
else:
    print("打死他....无情啊....")

t.join()







