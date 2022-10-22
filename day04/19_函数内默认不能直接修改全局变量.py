# @Time : 2022/1/25 22:42
# @Author : Jface
# @desc : 函数内默认不能直接修改全局变量

# 定义全局变量
num = 10


# 定义函数
def func():
    # 函数中给num赋值,重新定义一个局部变量num,并赋值250
    # 只不过这个局部变量和全局变量num同名, 但是实际上是两个变量
    num = 250
    print("函数内定义的num: ", num)  # 函数内访问的num是局部变量


# 调用函数
func()
print(num)
