# @Time : 2022/1/24 22:48 
# @Author : Jface 
# @desc :
"""
形参：函数定义是()里面的参数
作用域：变量起作用的范围
形参的作用域只在当前函数的内部有效，和外面没有任何关系
"""


def fucn_add(num1, num2):
    """ 作用： 求两数之和 """
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))


def fucn_sub(num1, num2):
    """ 作用： 求两数之差 """
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")


fucn_add(1, 3)
fucn_sub(4, 4)
