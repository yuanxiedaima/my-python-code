# @Time : 2022/1/31 20:39 
# @Author : Jface 
# @desc :
"""
给对象添加属性：
1. 创建对象变量
2. 对象变量.属性 = 数值
    # 第一次赋值是添加属性，再次赋值是修改

如果使用属性
对象变量.属性
"""


class Dog(object):
    def eat(self):
        print("啃骨头")

    def drink(self):
        print("喝汤")


# 1. 创建对象变量
dog1 = Dog()
# 2. 对象变量.属性 = 数值
dog1.name = "旺财"

# 打印属性
print(dog1.name)

# 修改属性
dog1.name = "二哈" # 第一次赋值是添加属性，再次赋值是修改
print(dog1.name)


dog2 = Dog()
dog2.name = "金毛"
print(dog2.name)
