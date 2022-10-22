# @Time : 2022/1/30 22:21 
# @Author : Jface 
# @desc :

# 1. 只读方式打开源文件(旧文件)
file_r = open("abc.txt", "r")
# 2. 只写方式打开新的备份文件(新文件)
file_w = open("abc[备份].txt", "w")
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
