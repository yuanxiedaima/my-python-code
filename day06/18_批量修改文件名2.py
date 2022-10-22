# @Time : 2022/1/31 20:06 
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
# 2. 切换到目标路径
os.chdir("pytest")
# 3. for遍历文件名的列表取出某个元素
for ole_file_name in dir_list:
    # 4. 对这个元素重命名
    temp_str = "[竖屏看春晚]"
    print(ole_file_name.find(temp_str))
    if ole_file_name.find(temp_str) != -1:
        new_file_name = ole_file_name[len(temp_str):]
        # 对这个元素重命名
        os.rename(ole_file_name, new_file_name)


os.chdir("../")
