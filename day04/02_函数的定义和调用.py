# @Time : 2022/1/24 22:40 
# @Author : Jface 
# @desc :
"""
1.函数的定义格式
def 函数的名字():
    函数内部的代码块

2.函数只是定义，不调用用户看不到没有效果的
函数调用的格式： 函数名字()
"""


# 1. def 函数名字():
def say_hello():
    # 2. 函数体，打印信息
    print("hello 1")
    print("hello 2")
    print("hello 3")


print("函数调用前")

# 3. 函数调用：函数名字()
say_hello()

print("函数调用后")
