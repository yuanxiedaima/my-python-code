# @Time : 2022/1/23 15:08 
# @Author : Jface 
# @desc :

# 1. 定义 holiday_name 字符串变量记录节日名称
holiday_name = "平安夜"
# 2. if 判断是否为情人节：
if holiday_name == "情人节":
    #   是两个=，==，判断是否相等
    # 2.1 如果是 情人节，打印： 买玫瑰／看电影
    print("买玫瑰/看电影")
# 3. elif 判断是否为平安夜:
elif holiday_name == "平安夜":
    # 3.1 如果是 平安夜，打印： 买苹果／吃大餐
    print("买苹果/吃大餐")
# 4. elif 判断是否为生日 :
elif holiday_name == "生日":
    # 4.1 如果是 生日，打印： 买蛋糕
    print("买蛋糕")
# 5. else 其它情况：
else:
    # 5.1 打印：每天都是节日啊……
    print("每日都是节日鸭！")
