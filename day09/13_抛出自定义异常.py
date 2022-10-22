# @Time : 2022/2/2 20:34 
# @Author : Jface 
# @desc :
"""
# 1. 自定义异常类
class 自定义异常类名字(Exception):
    1.1 重新写__init__(self, 形参1， 形参2，……)
        # 建议调用父类的init，先做父类的初始化工作
        super().__init__()
        咱们自己写的代码

    1.2 重新写__str__()，返回提示信息

# 2. 抛出异常类
raise 自定义异常类名字(实参1， 实参2，……)

# 3. 需求
# 1. 自定义异常类，电话号码长度异常类
    # 1.1 __init__，添加2个属性，用户电话的长度，要求的长度
    # 1.2 __str__ 返回提示描述意思，如：用户电话长度为：xx位, 这边要求长度为：11位

# 2. 只要用户输入的手机号码不为11位，抛出自定义异常类
"""


# 1. 自定义异常类
# class 自定义异常类名字(Exception):
class NumberError(Exception):
    # 1.1 重新写__init__(self, 形参1， 形参2，……)
    def __init__(self, _user_len, _match_len=11):
        # 建议调用父类的init，先做父类的初始化工作
        super().__init__()
        # super().__init__()
        # 咱们自己写的代码
        self.user_len = _user_len
        self.match_len = _match_len

    # 1.2 重新写__str__()，返回提示信息
    def __str__(self):
        return "用户电话长度为：{}位, 这边要求长度为：{}位".format(self.user_len, self.match_len)


# 2. 抛出异常类
# raise 自定义异常类名字(实参1， 实参2，……)

# 3. 需求
# 1. 自定义异常类，电话号码长度异常类
try:
    phone_num = input("请输入电话号码：")
    if len(phone_num) != 11:
        # raise 自定义异常类名字(len(phone_num))
        raise NumberError(len(phone_num))
    # 2. 只要用户输入的手机号码不为11位，抛出自定义异常类
except NumberError as e:
    print("电话号码长度异常：", e)
