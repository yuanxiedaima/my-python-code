# @Time : 2022/2/2 20:13 
# @Author : Jface 
# @desc :
"""
try:
    可能发生异常的代码
except:
    处理异常的代码
else:
    没有发生异常，except不满足执行else
finally:
    不管有没有异常，最终都要执行的代码
"""

try:
    # f = open('xxx.txt', 'r')
    # print(10 / 0)
    pass
except Exception as e:
    print(type(e), "错误描述：", e)
else:
    print("没有异常")
finally:
    print("无论是否有异常，都会执行的代码")
