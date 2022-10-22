# @Time : 2022/1/30 22:08 
# @Author : Jface 
# @desc :
"""
# 文件打开访问模式
# 文件变量 = open(文件名字，访问模式)
"""
f = open("xxx.txt", "w")

# f.read()  # 只写打开文件,不允许读操作 io.UnsupportedOperation: not readable

# input()     # 阻塞等待用户输入
# 没有close或者程序结束, 新写的文件内容不会刷新到磁盘中

f.write("hello lily")

f.close()
