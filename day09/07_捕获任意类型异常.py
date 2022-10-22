# @Time : 2022/2/2 19:58 
# @Author : Jface 
# @desc :
"""
try:
    可能发生异常的代码
except Exception as 异常对象名:
    Exception 为异常类的父类
"""

try:
    f = open('test.txt', 'r')

except Exception as e:
    print("发生异常")
