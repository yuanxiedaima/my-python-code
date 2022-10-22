# @Time : 2022/1/31 20:02 
# @Author : Jface 
# @desc :
"""
# 1. 获取pytest的目录信息，返回文件名的列表
# 2. 切换到目标路径
# 3. for遍历文件名的列表取出某个元素
# 4. 对这个元素重命名
"""

import os

# 1. 获取pytest的目录信息，返回文件名的列表
dir_list = os.listdir("pytest")
print(dir_list)
# 2. 切换到目标路径
os.chdir("pytest")
# 3. for遍历文件名的列表取出某个元素
for old_file_name in dir_list:
    new_file_name = "[竖屏看春晚]" + old_file_name
    # 4. 对这个元素重命名
    os.rename(old_file_name, new_file_name)

os.chdir("../")
