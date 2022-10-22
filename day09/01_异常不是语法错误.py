# @Time : 2022/2/2 19:34 
# @Author : Jface 
# @desc :
"""
异常：不是语法错误，语法错误，是程序写错了
异常：指程序已经运行了(没有语法错误)，突然发生异常，导致程序崩溃
"""

# 语法错误
# SyntaxError: Missing parentheses in call to 'print'. Did you mean print(abc)?
# print abc

print("=====================语法错误=====================")

# 如果"xxx.txt"不存在，只读方式打开
f = open("xxx.txt", "r")
# FileNotFoundError: [Errno 2] No such file or directory: 'xxx.txt'
print("=====================异常=====================")
