# @Time : 2022/2/2 20:15 
# @Author : Jface 
# @desc :
"""
# finally: 有没有异常，最终都要执行
# 对于文件操作，在文件打开的前提下，后面文件的其它操作，不管有没有发生异常，最终都应该关闭文件
"""
f = open('abc.txt', 'r')

try:
    # data = f.read()
    f.write("hello world")
except Exception as e:
    print(type(e), "错误描述：", e)
finally:
    print("无论是否发生异常，关闭文件")
    f.close()
