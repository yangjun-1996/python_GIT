"""
练习3： 编写一个函数，传入一个文件名(可以带路径)，
将这个传入的文件 拷贝到 函数的执行目录下

注意： 不确定要拷贝的文件类型

提示 ： 打开源文件 和 拷贝文件，从源文件读写入新文件
       可能文件很大，最好不要一次读取全部文件内容

重点代码！！！！
"""
def copy(path):
    """
    :param path: 要拷贝的文件
    """
    filename = path.split("/")[-1] #　提取文件名称

    old_file = open(path,'rb')
    new_file = open(filename,'wb')

    # 边读边写
    while True:
        data = old_file.read(1024)
        if not data:
            break
        new_file.write(data)
    old_file.close()
    new_file.close()



copy("/home/tarena/下载/timg.jpeg")







