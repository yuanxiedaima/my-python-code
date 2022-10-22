# @Time : 2022/1/30 22:05 
# @Author : Jface 
# @desc :

# 1. 打开文件，只读方式打开，'r'
# 'r'： 打开文件，必须存在，不存在，报错崩溃
f = open("abc.txt", "r")

# 2. 读取文件内容
# readlines： 读取所有的行
# readline:   一次读取一行
# readline格式：内容变量 = 文件变量.readline()
# data = f.readline()
# print(data)
#
# data = f.readline()
# print(data)
#
# data = f.readline()
# print(data)
#
# data = f.readline()
# print(data)
#
# data = f.readline()
# print(data)

# while True:
#     data = f.readline()
#     # if data == "":    # "", False, 都代表假
#     if not data:    # 非假 -> True
#         break
#     print(data)

while True:
    data = f.readline()
    # if data == "":    # [], (), "", False, 都代表假
    if data:    # 字符串有内容即为真
        print(data)
    else:
        break

# 3. 关闭文件
f.close()
