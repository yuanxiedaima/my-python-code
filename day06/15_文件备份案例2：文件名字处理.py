# @Time : 2022/1/31 19:48 
# @Author : Jface 
# @desc :

# 拷贝的文件名，不要写死，需要用户输入 input
# 新文件的名字变成：旧文件名[复制].txt

"""
# a. 输入需要拷贝的文件名 old_file_name = input()
# b. 找文件名字右边的第一个点，通过切片组装成： 旧文件名[备份].后缀

# 1. 只读方式打开源文件(旧文件)
# 2. 只写方式打开新的备份文件(新文件)
# 3. while True:
    # 4. 一次读取一点源文件的内容
    # 5. 如果读取的内容，往写文件中写
    # 6. 如果没有读到内容，文件已经读取完毕，break跳出循环
# 7. 关闭文件
"""

# a. 输入需要拷贝的文件名 old_file_name = input()
old_file_name = input("请输入需要备份的文件名：")
# b. 找文件名字右边的第一个点，通过切片组装成： 旧文件名[备份].后缀
pos = old_file_name.rfind(".")
new_file_name = old_file_name[:pos] + "[备份]" + old_file_name[pos:]

# 1. 只读方式打开源文件
# 扩展:使用二进制读写,可以读取任意格式
file_r = open(old_file_name, "rb")  # rb: 二进制方式只读打开(不用考虑编码)
# 2. 只写方式打开新的备份文件
file_w = open(new_file_name, "wb")  # wb: 二进制方式只写打开(不用考虑编码)
# 3. while True:
while True:
    # 4. 一次读取一点源文件的内容
    data = file_r.read(1024)
    # 5. 如果读取的内容，往写文件中写
    if data:
        file_w.write(data)
    # 6. 如果没有读到内容，文件已经读取完毕，break跳出循环
    else:
        break
# 7. 关闭文件
file_r.close()
file_w.close()
