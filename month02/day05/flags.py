"""
功能扩展演示
"""
import re

s = """Hello 
北京
"""
# 让^ $匹配每行开头结尾位置
result = re.findall(r"^\w+",s,flags=re.M|re.I)
print(result)

# 让 . 可以匹配换行
# result = re.findall(r".+",s,flags=re.S)
# print(result)

# 忽略字母的大小写
# result = re.findall(r"[a-z]+",s,flags=re.I)
# print(result)

# 让元字符只匹配 ascii码
# result = re.findall(r"\w+",s,flags=re.A)
# print(result)

