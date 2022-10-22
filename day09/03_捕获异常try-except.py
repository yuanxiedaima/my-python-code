# @Time : 2022/2/2 19:47 
# @Author : Jface 
# @desc :
"""
try:
    可能发生异常的代码
except:
    # 处理异常的代码
    1. 如果try里面发生异常
    2. 自动跳转到except里面
"""

try:
    print("=====开始=====")
    f = open("xxx.txt", "r")
    print("=====结束=====")
except:
    print("try里面发生异常")
