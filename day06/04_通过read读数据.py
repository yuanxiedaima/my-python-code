# @Time : 2022/1/29 23:06 
# @Author : Jface 
# @desc :
"""
# 1. 打开文件，只读方式打开，'r'
# 2. 读取文件内容
# 3. 关闭文件
"""

# 1. 打开文件，只读方式打开，'r'
# 'r'： 打开文件，必须存在，不存在，报错崩溃
# f = open("abc.txt", "r")    # windows系统默认使用编码为GBK

# 扩展: open("文件名", "访问模式", endcoding="字符编码")
#   utf-8: 万国码
#   gbk: 国标简繁体中文编码
f = open("abc.txt", "r", encoding="utf-8")

# 2. 读取文件内容
# 格式： 内容变量 = 文件变量.read(读取的长度)
#       如果read的长度不指定，默认读取全部
data = f.read(4)
print(data)

data = f.read()
print(data)

# 3. 关闭文件
f.close()
