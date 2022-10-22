# @Time : 2022/2/2 21:06 
# @Author : Jface 
# @desc :
"""

"""


def my_add(n1, n2):
    """ 实现两个数相加 """
    return n1 + n2


def my_sub(n1, n2):
    """ 实现两个数相减 """
    return n1 - n2


# 把不想导包被执行的代码放入 if __name__ == '__main__': 语句里
# if __name__ == "__main__":

# 输入main,会自动生成下一行代码:
if __name__ == "__main__":
    ret = my_add(2, 2)
    print("模块中测试代码：my_add(2, 2) = %d" % ret)
    ret = my_sub(10, 2)
    print("模块中测试代码：my_sub(10, 2) = %d" % ret)
