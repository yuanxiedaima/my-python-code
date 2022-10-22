# @Time : 2022/2/2 18:42 
# @Author : Jface 
# @desc :
"""
1. 定义一个类属性count，用于记录实例对象初始化的次数
2. __init__添加实例属性name，每初始化1次，类属性count加1
"""


class Dog(object):
    # 定义类属性: 统计使用这个Dog类创建了多少对象, 是所有实例对象公用的
    count = 0

    def __init__(self, _name):
        # 定义实例属性: 每个实例对象特有的
        self.name = _name
        # 每次调用 __init__ 方法，count 计数 +1
        Dog.count += 1


print(Dog.count)
dog1 = Dog('旺财')
print(dog1.name, Dog.count)

dog2 = Dog('旺钱')
print(dog2.name, Dog.count)

dog3 = Dog('旺仔')
print(dog3.name, Dog.count)

# 类属性是所有实例对象公用的，实例属性是每个实例对象特有的
print(dog1.count, dog2.count, dog3.count)
# 旺财 旺钱 旺仔 实例属性是每个实例对象特有的
print(dog1.name, dog2.name, dog3.name)
