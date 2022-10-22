# @Time : 2022/1/25 22:28 
# @Author : Jface 
# @desc :函数的嵌套调用: 函数里面调用别的函数

# 定义函数 func01 函数
def func01():
    print("调用 func01 开始")
    print("调用 func01 结束")

# 定义函数 func02 函数
def func02():
    print("调用 func02 开始")
    func01()
    print("调用 func02 结束")

# 函数调用
func02()