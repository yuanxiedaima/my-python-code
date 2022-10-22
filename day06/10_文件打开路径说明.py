# @Time : 2022/1/30 22:10 
# @Author : Jface 
# @desc :

# 1. 绝对路径下，打开文件，如果绝对路径E:/Code/PyCode不存在，打开失败
# open("路径"+"文件名")
# \\: 表示字符\. 第一个\叫转义字符,表示把第二个\的特殊意义去掉.
# f = open("C:\\Users\\35477\\Desktop\\python42\\day06\\a.txt", "w")
# f = open("C:/Users/35477/Desktop/python42/day06/a.txt", "w")
# f = open(r"C:\Users\35477\Desktop\python42\day06\a.txt", "w")
# name = str(random.randint(1, 10)) + ".txt"

name = "a.txt"
f = open("/Users/jface/PycharmProjects/learnPython/day06/" + name, "r")
data = f.read()

print(data)

f.close()

# 2. 相对路径下打开文件，相对于当前的目标文件，就是当前py文件所在路径
# 2.1 当前路径下，如果文件不存在，新建文件
# f = open("b.txt", "w")
f = open("./b.txt", "w")
f.close()

# 2.2 上一级路径下，如果文件不存在，新建文件
f = open("../../b.txt", "w")
f.close()