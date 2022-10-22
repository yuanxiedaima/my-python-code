# @Time : 2022/1/26 23:20 
# @Author : Jface 
# @desc :
"""
# 匿名函数是简单普通函数的简洁写法
# 匿名函数没有函数名字
"""


# 1. 有参无返回值
# 普通函数
def foo():
    return 1 + 1


ret = foo()
print(ret)

print("=" * 20)

# 匿名函数
# 定义：lambda : 函数体
# 函数体就是返回值的内容，无需return
# lambda: 1 + 1

# a) 匿名函数整体就是函数名字， 函数名字()就是函数调用
ret = (lambda: 1 + 1)()
print(ret)
print("=" * 20)

# b) 给匿名函数起一个函数名字，函数名字()就是调用函数
func = lambda: 1 + 1
ret = func()
print(ret)
print("=" * 20)


# 2. 有参有返回值
# 普通函数
def foo(n1, n2):
    return n1 - n2


ret = foo(30, 10)
print(ret)
print("=" * 20)
# 匿名函数
# a 直接调用匿名函数
ret = (lambda n1, n2: n1 - n2)(30, 10)
print(ret)
print("=" * 20)
# b 给匿名函数起个名字再调用
func = lambda n1, n2: n1 - n2
ret = func(30, 10)
print(ret)
