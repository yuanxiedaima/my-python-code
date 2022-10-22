# @Time : 2022/2/2 19:52 
# @Author : Jface 
# @desc :
"""
try:
    可能发生异常的代码
except (异常类型1, 异常类型2):
    # 处理异常的代码
    1. 如果try里面发生异常
    2. 自动跳转到except里面
"""

try:
    print("=" * 10)
    f = open("xxx.txt", "r")
    print("=" * 10)
    print(10 / 0)
    print("=" * 10)
    if "18" > 18:
        print("年满18岁")
except (FileNotFoundError, ZeroDivisionError):
    print("捕获不到文件找不到异常或者被除数为0 异常")
