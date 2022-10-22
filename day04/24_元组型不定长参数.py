# @Time : 2022/1/25 22:56 
# @Author : Jface 
# @desc : 函数形参变量的前面加一个*， 这个参数就是不定长参数

# 函数定义
# *args 不定长参数，可以接收0~多个实参
# 把实参的1,2,3, 包装成元组(1, 2, 3)再传递, 等价于args = (1, 2, 3)

def foo(*args):
    print(args, type(args))


# 函数调用
foo()
foo(1)
foo("hello")
foo(1, 2, 3)
foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
