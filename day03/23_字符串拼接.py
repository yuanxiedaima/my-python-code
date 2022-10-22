# @Time : 2022/1/23 22:13 
# @Author : Jface 
# @desc :
"""
字符串 + 字符串	        拼接两个字符串
字符串.join(字符串列表)	以字符串来连接字符串列表中每个元素，合并为一个新的字符串, 返回新的字符串
"""

# 字符串 + 字符串	        拼接两个字符串
str1 = "hello "
str2 = "world "
str3 = "python "
new_str = str1 + str2 + str3
print(new_str)

# 字符串.join(字符串列表)	以字符串来连接字符串列表中每个元素，合并为一个新的字符串, 返回新的字符串
str4 = ","
str_list =['rose', 'tom', 'lily', 'mike']
new_str = str4.join(str_list)
print(new_str)
