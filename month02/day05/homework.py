"""
练习： 使用log.txt文本完成
编写一个程序，输入一个接口名称，得到该接口运行信息中的
address is 地址值

提示: 每段之间有空行，每段是一个接口运行信息的描述
      每段的第一个单词是接口名称

思路: 先确定段落，再匹配目标 地址值
"""
import re

# 每段文字的提供者  生成器
def get_info():
    file = open("log.txt", 'r')
    # 每次while 循环得到一段内容
    while True:
        data = "" # 存储一段内容
        for line in file:
            # 如果一行内容 是 \n说明这是空行
            if line == "\n":
                break
            data += line

        # 将这段文字 以yield的方式提供出去
        if data:
            yield data
        else:
            file.close()
            return


# 确定段落 匹配地址 port：要找的接口名
def main(port):
    for info in get_info():
        # 获取这段的首个单词
        obj = re.match(r"\S+",info)
        if port == obj.group():
            # 找到目标段，开始匹配address
            pattern = r"([0-9a-f]{4}\.){2}[0-9a-f]{4}"
            obj = re.search(pattern,info)
            return obj.group()

print(main("TenGig"))








