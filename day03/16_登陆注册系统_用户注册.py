# @Time : 2022/1/23 21:38 
# @Author : Jface 
# @desc :
"""
登录注册系统需求：1.用户注册/ 2.用户登录/ 3.退出程序

# 0. 定义一个列表，用于存储用户字典

# 1. 死循环 while True:
    # 2. 输入数字指令
    # 3. 判断指令，选择分支
    # 4. 用户注册功能
        # 4.1 输入注册的用户名
        # 4.2 通过for遍历列表，取出的每个元素是字典
            # 4.3 字典['name']和输入注册的用户名比较是否相等
                # 4.4 如果相等，打印提示：名字在列表中，不允许注册
                # 4.5 跳出循环
        # 4.6 for循环的else，循环里面没有执行到break，则会执行else
            # 4.7 输入注册的密码
            # 4.8 创建一个字典
            # 4.9 字典追加到列表中
            # 4.10 打印：注册成功
"""
# 0. 定义一个列表，用于存储用户字典
user_list = [{"name": "rose", "password": "123"}, {"name": "mike", "password": "456"}]

# 1. 死循环 while True:
while True:
    # 2. 输入数字指令
    num = int(input("请输入操作: 1.用户注册/ 2.用户登录/ 3.退出程序 : "))
    # 3. 判断指令，选择分支
    if num == 1:
        # 4. 用户注册功能
        # 4.1 输入注册的用户名
        user_name = input("请输入需要的注册的用户名：")
        # 4.2 通过for遍历列表，取出的每个元素是字典
        for user_dict in user_list:
            # 4.3 字典['name']和输入注册的用户名比较是否相等
            if user_dict["name"] == user_name:
                # 4.4 如果相等，打印提示：名字在列表中，不允许注册
                print("名字在列表中，不允许注册")
                # 4.5 跳出循环
                break
        # 4.6 for循环的else，循环里面没有执行到break，则会执行else
        else:
            # 4.7 输入注册的密码
            user_password = input("请输入注册密码：")
            # 4.8 创建一个字典
            new_dist = {"name": user_name, "password": user_password}
            # 4.9 字典追加到列表中
            user_list.append(new_dist)
            # 4.10 打印：注册成功
            print("注册成功！")
            # print(user_list[-1])
    elif num == 2:
        pass
    elif num == 3:
        print("退出程序")
    else:
        print("输入错误，重新输入")
