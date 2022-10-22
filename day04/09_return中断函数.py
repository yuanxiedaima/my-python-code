# @Time : 2022/1/24 22:59 
# @Author : Jface 
# @desc : 函数一旦执行return，函数内return下一句往后的代码不会执行
def foo():
    print("不努力，咋实现奶茶自由车厘子自由")
    return
    print("我要玩游戏")


foo()
