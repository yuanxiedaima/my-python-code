# @Time : 2022/1/23 15:20 
# @Author : Jface 
# @desc : 猜拳基础代码实现

"""
规则：石头 1， 剪刀 2， 布 3
角色：user computer
用户赢的情况：
    (user == 1 and computer == 2) or
    (user == 2 and computer == 3) or
    (user == 3 and computer == 1)
"""
# 1. 用户输入数字：请输入（石头 1， 剪刀 2， 布 3）
user = int(input("请输入（石头 1， 剪刀 2， 布 3）："))
# 2. 电脑固定一个数字，假定只会出石头
computer = 1
# 3. if 用户赢电脑的判断：
if (user == 1 and computer == 2) or (user == 2 and computer == 3) or (user == 3 and computer == 1):
    # 3.1 如果用户赢，打印：电脑弱爆了
    print("电脑弱爆了")
# 4. elif 平局：
elif user == computer:
    # 4.1 打印：心有灵犀，再来一盘！
    print("心有灵犀，再来一盘！")
# 5. 否则，电脑赢
else:
    # 5.1 打印：不行，我要和你决战到天亮！
    print("不行，我要和你决战到天亮！")
