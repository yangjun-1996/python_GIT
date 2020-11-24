"""
文件写操示例
"""

# 打开文件
# file = open("myfile", 'wb') # 清空原来内容
file = open("myfile", 'a') # 追加

# 写入内容 写的数据类型与打开方式呼应
# file.write(b"hello,si gui\n")
# n = file.write("哎呀,干啥\n".encode())
# print(n)

# 写入列表中的每一项
data = ["今天天气\n","怎么样\n"]
file.writelines(data)



# 关闭
file.close()
