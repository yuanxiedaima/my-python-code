# @Time : 2022/1/31 19:35 
# @Author : Jface 
# @desc :
# 拷贝的文件名，不要写死，需要用户输入 input
# 新文件的名字变成：旧文件名[备份].txt

# 1. 字符串找.的位置, rfind， r为right, 从右往左找
old_file_name = "a.b.c.txt"

pos = old_file_name.rfind(".")
print(pos)

# 2. 通过切片提取所要的字符串
path1 = old_file_name[:pos]
print(path1)

path2 = old_file_name[pos:]
print(path2)

new_file_name = path1 + "[备份]" + path2
print(new_file_name)
