# @Time : 2022/2/2 20:18 
# @Author : Jface 
# @desc :
"""
try嵌套时，如果内层try没有捕获该异常，就会向外层try进行传递
"""

try:
    f = open("abc.txt", "w")

    try:
        data = f.read()
        print(data)
    finally:
        print("关闭文件")
        f.close()

except Exception as e:
    print("外层try捕获到异常：", e)
