# @Time : 2022/1/23 15:29 
# @Author : Jface 
# @desc : 猜拳游戏实现

# 0. 导入模块
import random

# 1. 用户输入数字：请输入（石头 1， 剪刀 2， 布 3）
user = int(input("请输入（石头 1， 剪刀 2， 布 3）："))
# 2. 电脑 随机 出拳，即随机产生一个[1,3]范围的数
computer = random.randint(1, 3)
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
