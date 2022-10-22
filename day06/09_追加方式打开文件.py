# @Time : 2022/1/30 22:09 
# @Author : Jface 
# @desc :

# 追加方式打开文件，文件不存在新建，文件存在写光标放在文件末尾，写数据直接写在文件末尾

# 1. 'a'，追加方式打开文件, 不会清空源文件
f = open('xxxx.txt', "a")

# 2. 写数据
f.write("hello python\n")
# f.read()    # io.UnsupportedOperation: not readable


# 3. 关闭文件
f.close()