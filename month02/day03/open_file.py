"""
open 打开文件示例
"""

# 读方式打开  默认 “r”
# file = open("3.txt",'r')

# 写方式 文件不存在创建 存在情况
# file = open("myfile",'w')

# 写方式 文件不存在创建 存在继续写
file = open("myfile",'a')

# 读写操作


# 文件对象关闭，不能操作文件
file.close()



