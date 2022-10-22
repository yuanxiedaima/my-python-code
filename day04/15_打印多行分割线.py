# @Time : 2022/1/25 22:30 
# @Author : Jface 
# @desc :
"""
1. 设计一个函数，打印一行分隔线：可指定数量，可指定分隔线字符的样式
    如： 一行分隔线字符的数量为5，字符样式为'^_^ '
    ^_^ ^_^ ^_^ ^_^ ^_^
2. 设计一个函数，打印n行分隔线，可指定一行分隔线字符的数量，可指定分隔线字符的样式
    如：3行分隔线，一行分隔线字符的数量为5，字符样式为'^_^ '
    ^_^ ^_^ ^_^ ^_^ ^_^
    ^_^ ^_^ ^_^ ^_^ ^_^
    ^_^ ^_^ ^_^ ^_^ ^_^
"""


def print_char(num, char):
    """
    输出一行分割线
    :param num: 一行分割字符个数
    :param char: 分割字符
    :return: None
    """
    print(char * num)


def print_line(n, num, char):
    """
    输出 n 行分割线
    :param n:  分割线的行数
    :param num: 一行分割线字符个数
    :param char: 分割字符
    :return: None
    """
    # 1. 设置条件变量 i = 0
    i = 0
    # 2. while 条件：
    while i < n:
        # 3. 打印一行的分隔线
        print(num * char)
        # 4. 条件变量的改变
        i += 1


# 函数调用
print_char(5, "(*^▽^*)")
print_line(10, 5, "(*^▽^*)")
