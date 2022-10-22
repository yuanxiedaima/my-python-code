# @Time : 2022/1/30 22:06 
# @Author : Jface 
# @desc :
"""
# 文件打开访问模式
# 文件变量 = open(文件名字，访问模式)
# 'r'，只读方式打开文件，文件不存存在，报错
# FileNotFoundError: [Errno 2] No such file or directory: 'xxxx.txt'
# f = open("xxxx.txt", "r")
"""

f = open("xxx.txt")

data = f.read()
print(data)

f.close()
