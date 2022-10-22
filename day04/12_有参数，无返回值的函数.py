# @Time : 2022/1/25 22:22 
# @Author : Jface 
# @desc :
"""
有参数，无返回值的函数
函数定义：
def 函数名字(形参1，形参2，……)：
    函数体

函数调用：
函数名(实参1，实参2，……)
"""


# 函数定义
def print_char(num, char):
    """
    输入指定数量的字符
    :param num:  字符数量
    :param char: 输入的字符
    :return: None
    """
    print(char * num)


# 函数调用
print_char(10, "(*^▽^*)")
