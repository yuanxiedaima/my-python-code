# @Time : 2022/2/2 20:20 
# @Author : Jface 
# @desc :
"""
函数嵌套时，如果内层函数没有捕获处理该异常，就会向外层函数进行传递
"""


# 定义1个函数，函数内部发生了异常 test01()，没有捕获处理
def test01():
    print("test01() 开始执行")
    print(num)
    print("test01() 执行结束")


# 定义另外一个函数 test02, 在函数内部调用test01
def test02():
    print("test02() 开始执行")
    test01()
    print("test02() 执行结束")


# 定义一个test03函数，函数内部调用test01，但是对test01做异常处理
def test03():
    print("test03() 开始执行")
    try:
        test01()
    except Exception as e:
        print("test01() 发生了异常:", e)
    print("test03() 执行结束")


# 函数调用
# test02()
test03()
