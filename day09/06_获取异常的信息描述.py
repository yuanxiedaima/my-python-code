# @Time : 2022/2/2 19:54 
# @Author : Jface 
# @desc :
"""
try:
    可能发生异常的代码
except 异常类型 as 异常对象名:
    print(异常对象名) 即可获取异常的信息描述
"""

try:
    # f = open("xxx.txt", "r")
    # print(10 / 0)
    print("18" > 18)
except Exception as e:
    print(type(e), "异常描述：", e)