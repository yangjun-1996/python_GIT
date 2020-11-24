"""
文件读操作示例
1.open后每次读取都向下读取
2.读到文件结尾再次读取会得到空字符串/字节串
"""

# 打开文件
file = open("myfile","r")

# 读取文件内容
# data = file.read() # 不加参数表示读取文件全部内容
# print(data)

# 循环读取内容，打印出来，直到文件结尾结束
# while True:
#     data1 = file.read(5)
#     # data1 为空跳出循环
#     if not data1:
#         break
#     print(data1,end="")

# 按行读取
# line = file.readline(5)
# print(line)
# line = file.readline()
# print(line)

# 读取多行，形成与一个列表
# lines = file.readlines(16)
# print(lines)

# 迭代每次取一行
for line in file:
    print(line)



# 关闭文件
file.close()


