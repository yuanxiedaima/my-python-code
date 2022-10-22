# @Time : 2022/1/26 22:56 
# @Author : Jface 
# @desc : 给函数传参是引用传递

# 函数定义
def foo(num):
    print("func: ", id(num))


# 给函数传参，变量传参
a = 10
print("函数调用前：", id(a))

foo(a)
print("函数调用后：", id(a))
