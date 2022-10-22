# @Time : 2022/1/23 22:09 
# @Author : Jface 
# @desc : 字符串.split(分割符)	以分割符拆分字符串, 返回列表

str1 = "hello python hello world"

# str1中字符串内容以' '分隔，返回字符串列表['hello', 'python', 'hello', 'world']
new_str = str1.split(" ")
print(new_str)

# 扩展1: \t: tab键 \n: 回车键
# split() 不指定分割字符,会以空白字符作为分割, 空白字符:空格,tab键,回车换行键.
str2 = "hello python\thello\nworld"
new_str = str2.split()
print(new_str)

# 扩展2: split("分隔符", maxsplit=最大分割次数)
str3 = "hello python hello world"
new_list = str3.split(" ", maxsplit=2)
print(new_list)
