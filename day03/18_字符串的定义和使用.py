# @Time : 2022/1/23 21:55 
# @Author : Jface 
# @desc :
"""
字符串变量 = '字符串内容'
说明：可以是单引号、双引号、三引号
"""

str1 = 'hello'
print(type(str1))
str2 = "hello"
print(type(str2))
str3 = """hello"""
print(type(str3))

# 单引号和双引号没有区别, 三引号可以存储多行字符串
str4 = """hello
        world"""
print(str4)

# 取出某个元素，和列表一样
str1 = "hello"
print(str1[0])

# 字符串能读不能写
# str1[1] = "a"
# print(str1)
# TypeError: 'str' object does not support item assignment

# 遍历所有元素
for c in str1:
    print(c)

# 扩展:注意 嵌套使用单引号和双引号
# str1 = 'hello "&" world'
str1 = "hello '&' world"
print(str1)