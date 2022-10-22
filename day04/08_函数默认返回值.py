# @Time : 2022/1/24 22:57 
# @Author : Jface 
# @desc :
"""
1. 函数内部没有任何return语句，默认返回None，表示没有任何数据
2. return不设置返回值，默认有返回None
"""


def foo1():
    print("QAQ")


def foo2():
    return


ret = foo1()
print(ret)

ret = foo2()
print(ret)
