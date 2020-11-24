"""
文件偏移量
r,w 打开文件偏移量在开头
a 打开在结尾
"""
file = open("myfile",'w+')

file.write("先帝创业未半")
file.flush()

print(file.tell()) # 文件偏移量大小 18 字节

# 从开头算起向后移动6个字节
file.seek(6,0)
data = file.read()
print(data)

file.close()

