# @Time : 2022/1/23 22:00 
# @Author : Jface 
# @desc :
name = "小明"
age = 20
sex = "male"

# 字符串格式化 %
str1 = "我叫%s，今年%d岁，我的性别是%s" % (name, age, sex)
print(str1)

# 字符串格式化: f-string (python3.6版本后)
str2 = f"我叫{name}，今年{age}岁，我的性别是{sex}"
print(str2)
str3 = F"我叫{name}，今年{age}岁，我的性别是{sex}"
print(str3)

# 扩展: 字符串格式化: format
str4 = "我叫{}，今年{}岁，我的性别是{}".format(name, age, sex)
print(str4)
