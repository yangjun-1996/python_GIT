"""
练习2： 编写一个函数，参数传入一个单词，返回这个
单词的对应解释
"""

def query_word(word):
    file = open("dict.txt","r")
    # 逐行查找
    for line in file:
        tmp = line.split(" ",1)
        # 如果遍历的单词已经大于目标了，说明一定没有了
        if tmp[0] > word:
            break
        elif tmp[0] == word:
            return tmp[1].strip()

print(query_word("zoo"))