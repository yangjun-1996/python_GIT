"""
字节串的定义处理

空字节串 bool判断为False，字节串也能拼接

所有的字符串都能转换为字节串   是的
所有的字节串都能转换为字符串   不是
"""
# 定义一个字节串变量 bytes
b = b"hello world"
print(type(b))

# 非英文字符定义为字节串 需要使用encode()转换
s = "你好"
b1 = s.encode()
print(b1)

# 将字节串转换回字符串
print(b'\xe4\xbd\xa1\xe3\xf5\xbd'.decode())
