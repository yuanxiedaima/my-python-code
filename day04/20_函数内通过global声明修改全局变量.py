# @Time : 2022/1/25 22:44 
# @Author : Jface 
# @desc : 函数内修改全局变量，先global声明全局变量，再修改

# 定义全局变量
num = 10


# 定义函数

def func():
    # 函数内修改全局变量，先声明 global 声明全局变量，再修复
    global num
    num = 250
    print("全局变量 num：", num)


# 调用函数

func()
print(num)
