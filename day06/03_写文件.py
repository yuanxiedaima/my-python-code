# @Time : 2022/1/29 23:10 
# @Author : Jface 
# @desc :
"""
# 1. 打开文件，只写方式打开
# 2. 写文件
# 3. 关闭文件
"""

# 1. 打开文件，只写方式打开
f = open("abc.txt", "w")

# 2. 写文件
# 写文件格式：文件变量.write(所需的内容)
f.write("hello abc")
f.write("hello python\n")
f.write("hello file")

# 3. 关闭文件
f.close()
