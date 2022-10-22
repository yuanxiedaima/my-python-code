# @Time : 2022/1/31 20:18 
# @Author : Jface 
# @desc :
"""
# 1. 通过with 只写方式打开文件，with里面的语句执行完，自动处理关闭
# 2. 将列表转换为字符串后，再往文件中写
"""

user_list = [{'name': 'mike', 'age': 34, 'tel': 110},
             {'name': 'yoyo', 'age': 30, 'tel': 120}]

# 1. 通过with 只写方式打开文件，with里面的语句执行完，自动处理关闭
with open("info2.txt", "w") as f:
    # 2. 将列表转换为字符串后，再往文件中写
    f.write(str(user_list))
