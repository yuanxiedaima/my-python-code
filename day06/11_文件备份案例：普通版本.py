# @Time : 2022/1/30 22:19 
# @Author : Jface 
# @desc :

# 1. 只读方式打开源文件
file_r = open("abc.txt", "r")
# 2. 只写方式打开新的备份文件
file_w = open("abc[备份].txt", "w")
# 3. 一次性读取源文件的内容
data = file_r.read()
# 4. 读取的内容，往写文件中写
file_w.write(data)
# 5. 关闭文件
file_r.close()
file_w.close()
