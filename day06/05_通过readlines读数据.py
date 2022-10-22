# @Time : 2022/1/30 21:57 
# @Author : Jface 
# @desc :

# 1. 打开文件，只读方式打开，'r'
f = open("abc.txt", "r")

# 2. 读取文件内容
# readlines: 读取所有的行，按行作为分隔条件
# 格式：内容列表变量 = 文件变量.readlines()
r_list = f.readline()

# 通过for取出列表的所有元素
for row in r_list:
    print(row)

# 3. 关闭文件
f.close()
