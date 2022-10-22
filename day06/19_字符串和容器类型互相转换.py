# @Time : 2022/1/31 20:16 
# @Author : Jface 
# @desc :
"""
# 字符串、容器类型相互转换
# str(容器变量)：将 容器变量 转换为一个字符串
# eval(字符串内容)：返回传入字符串内容的结果，字符串里面看到是什么，就转换成什么
"""
# 列表
user_list = [{'name': 'mike', 'age': 34, 'tel': 110},
             {'name': 'yoyo', 'age': 30, 'tel': 120}]

# 列表转字符串
my_str = str(user_list)
print(my_str, type(my_str))

# 字符串转列表
my_str2 = "[{'name': 'mike', 'age': 34, 'tel': 110}, {'name': 'yoyo', 'age': 30, 'tel': 120}]"
my_list = eval(my_str2)
print(type(my_list), my_list, type(my_list[0]))
