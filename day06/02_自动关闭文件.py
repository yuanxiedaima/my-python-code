# @Time : 2022/1/29 23:05 
# @Author : Jface 
# @desc :
"""
# 只要文件打开了，运行完with语句，自动关闭文件
# with open() as 文件变量名：
#   文件的操作
"""
with open ("xxx.txt", "w") as f:
    pass