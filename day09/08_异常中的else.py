# @Time : 2022/2/2 20:08 
# @Author : Jface 
# @desc :
"""
try:
    可能发生异常的代码
except:
    处理异常的代码
else:
    没有发生异常，except不满足执行else
"""

try:
    # f = open('xxx.txt', 'r')
    pass
except Exception as e:
    print(type(e), "描述信息:", e)
else:
    print("没有异常")
