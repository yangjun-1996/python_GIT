"""
with 语句
"""
# 打开文件 =》 file=open("myfile")
with open("myfile") as file:
    data = file.read()
    print(data)

# 语句块结束自动 销毁 file对象
