# @Time : 2022/1/31 20:21 
# @Author : Jface 
# @desc :
"""
# 1. 定义空列表，用户后续做学生信息保存
# 2. 通过with打开文件，只读方式打开文件
# 3. 文件变量.read()读取所有内容，返回内容是字符串类型
# 4. 把读取内容通过eval转换成列表，给前面的列表赋值
# 5. 在with的外面，打印列表内容
"""

# 1. 定义空列表，用户后续做学生信息保存

# 2. 通过with打开文件，只读方式打开文件
with open("info.txt", "r") as f:
    # 3. 文件变量.read()读取所有内容，返回内容是字符串类型
    data = f.read()
# 4. 把读取内容通过eval转换成列表，给前面的列表赋值
my_list = eval(data)
# 5. 在with的外面，打印列表内容
print(my_list)

for user_dict in my_list:
    print(user_dict["name"], user_dict["age"], user_dict["tel"])
