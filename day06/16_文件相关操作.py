# @Time : 2022/1/31 19:57 
# @Author : Jface 
# @desc :
"""
1. 导入模块，只需导入一次即可
import os
2. 使用os中的方法，完成功能
os.方法名()
"""

import os
# 1. 给文件重新命名
# 格式： os.rename(旧的文件名，新的文件名)
# os.rename("stu.txt", "stu2.txt")

# 2. 删除文件
# 格式： os.remove(待删除的文件名)
# os.remove("temp.png")
# os.remove("temp[备份].png")

# 3. 创建文件夹，只能创建文件夹，不能创建普通文件
# 格式： os.mkdir(文件夹的名字)
# os.mkdir("张三")

# 4. 删除文件夹，只能删除空的文件夹
# 格式：os.rmdir(待删除文件夹的名字)
# os.rmdir("张三")

# 5. 获取当前工作的路径
# 格式：路径变量 = os.getcwd()
# C:\Users\35477\Desktop\python42\day06
# path = os.getcwd()
# print(path)

# 6. 改变路径
# 格式：os.chdir(改变的路径)
# 切换到上一级路径
# os.chdir("../")  # change dir
#
# path = os.getcwd()
# print(path)

# 7. 【重点】获取某个目录的文件信息，获取文件夹或文件的名字
# 格式：目录列表变量 = os.listdir(指定某个目录)
#      如果不指定目录，默认当前路径
dir_list = os.listdir()
print(dir_list)


# 8. 判断文件是否存在
# 语法格式：os.path.exists(需要判断的文件)
# 文件存在返回True，文件不存在返回False
print(os.path.exists("abc.txt"))
print(os.path.exists("abcd.txt"))


# my_list = os.listdir("C:/Users/35477/Desktop/")
# print(my_list)
