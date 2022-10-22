# @Time : 2022/2/2 19:50 
# @Author : Jface 
# @desc :
"""
try:
    可能发生异常的代码
except 异常类型:
    # 处理异常的代码
    1. 如果try里面发生异常
    2. 自动跳转到except里面
"""

try:
    print("=*10")
    # f = open("xxx.txt", "r")
    print("=*10")
    print(10 / 0)
    print("=*10")
except FileExistsError:
    print("文件不存在")
except ZeroDivisionError:
    print("除数不能为0")
