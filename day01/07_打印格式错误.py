# @Time : 2022/1/22 23:26 
# @Author : Jface 
# @desc :
"""
age = input('请输入你的年龄：')
age是字符串类型，默认需要使用%s打印
print("你输入的年龄是: %d" % age)
int(age)把age转换为int类型
"""
age = input("请输入你的年龄：")
print("你的年龄是%s" % age)

# 转换成 int 类型
age = int(age)
print("你的年龄是%d" % age)
