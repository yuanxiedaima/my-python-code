# @Time : 2022/1/22 23:17 
# @Author : Jface 
# @desc :
"""
输入：通过input()读取键盘输入的内容
字符串变量 = input('提示信息：')
"""
# 1.input() 等带用户输入，按回车才会往下执行
password = input("请输入命名：")
print(type(password))
# %s,格式化打印
print("你输入的密码是：%s" % password)
# 直接打印看不出啥类型

