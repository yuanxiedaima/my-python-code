# @Time : 2022/1/23 21:34 
# @Author : Jface 
# @desc :
"""
登录注册系统需求：1.用户注册/ 2.用户登录/ 3.退出程序

# 1. 死循环 while True:
    # 2. 输入数字指令
    # 3. 判断指令，选择分支
"""

user_list = [{"name": "rose", "password": "123"}, {"name": "mike", "password": "456"}]

while True:
    num = int(input("请输入操作: 1.用户注册/ 2.用户登录/ 3.退出程序 : "))
    if num == 1:
        pass
    elif num == 2:
        pass
    elif num == 3:
        print("退出程序")
    else:
        print("输入错误，重新输入")
