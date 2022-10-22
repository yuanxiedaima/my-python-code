# @Time : 2022/1/25 22:54 
# @Author : Jface 
# @desc :
"""
# 形参设定默认值，称为缺省参数，也叫默认参数
# 调用函数时，如果没有传入默认参数对应的实参，则使用默认值
"""


# 函数定义
def foo(a, b, c, d=40, e=50):
    print(a, b, c, d, e)


# 函数调用
foo(1, 2, 3)
foo(1, 2, 3, 4)
foo(1, 2, 3, 4, 5)

# 默认参数必须放在普通参数的右边
# SyntaxError: non-default argument follows default argument
# def foo(a, b, d=40, c,  e=50):
#     print(a, b, c, d, e)
