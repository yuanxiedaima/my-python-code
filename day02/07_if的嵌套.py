# @Time : 2022/1/23 15:11 
# @Author : Jface 
# @desc : 先写外层的if，再写内层的if

# 外层 if 步骤流程：
# 1. 定义布尔型变量 has_ticket，赋值为True表示有票
has_ticket = False
# 2. if 判断是否有票：
if has_ticket == True:
    # 2.1 如果有票，打印：有车票，即将进行下一步的刀具安检
    print("有车票，即将进行下一步的刀具安检")
    # 2.2 内层if的处理(先空着，不处理)
    # a. 定义整型变量 knife_length 表示刀的长度，单位：厘米
    knife_length = 10
    # b. if 判断刀具长度是否超过20：
    if knife_length > 20:
    # b.1 如果超过 20 厘米，打印：刀的长度超过20厘米，不允许上车
        print("刀的长度超过20厘米，不允许上车")
    # c. 否则，不超过20厘米：
    else:
    # c.1 打印：安检通过，请上车
        print("安检通过，请上车")

# 3. 否则，没有票
else:
    # 3.1 打印：大哥，您要先买票啊
    print("大哥，您要先买票啊")
