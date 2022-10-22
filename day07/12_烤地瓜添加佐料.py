# @Time : 2022/2/1 20:07 
# @Author : Jface 
# @desc :
"""
# SweetPotato 类的设计
    地瓜有两个属性：
        状态 state：字符串
        烧烤总时间 cooked_time：整数

# 1. 定义__init__方法，添加2个属性
    # 1.1 默认状态state是生的
    # 1.2 默认时间cooked_time是0

# 2. 定义__str__方法
    # 2.1 返回地瓜状态，烧烤总时间

# 3. 定义 cook 方法, 提供参数 time 设置 本次烧烤的时间
    # 3.1 使用 本次烧烤时间 对 烧烤总时间 进行 累加
    # 3.2 根据 烧烤总时间, 设置地瓜的状态：
        [0, 3) -> 生的
        [3, 6) -> 半生不熟
        [6, 8) -> 熟了
        大于等于8 -> 烤糊了

# 4. 主逻辑程序
# 4.1 创建 地瓜对象
# 4.2 分多次烧烤地瓜
# 4.3 每烧烤一次，输出地瓜信息
"""


# SweetPotato 类的设计
# 地瓜有两个属性：
# 状态 state：字符串
# 烧烤总时间 cooked_time：整数
class SweetPotato(object):
    # 1. 定义__init__方法，添加2个属性
    def __init__(self):
        # 1.1 默认状态state是生的
        self.state = "生的"
        # 1.2 默认时间cooked_time是0
        self.cooked_time = 0
        # 5.1 添加属性 condiments， 列表类型，默认为空列表
        self.condiments = []

    # 2. 定义__str__方法
    # 2.1 返回地瓜状态，烧烤总时间
    def __str__(self):
        return ("地瓜状态：%s 地瓜烧烤总时间：%d 地瓜已经添加的佐料: %s") % (self.state, self.cooked_time, self.condiments)

        # 3. 定义 cook 方法, 提供参数 time 设置 本次烧烤的时间

    def cook(self, time):
        # 3.1 使用 本次烧烤时间 对 烧烤总时间 进行 累加
        self.cooked_time += time
        # 3.2 根据 烧烤总时间, 设置地瓜的状态：
        # [0, 3) -> 生的
        if 0 <= self.cooked_time < 3:
            self.state = "生的"
        # [3, 6) -> 半生不熟
        elif 3 <= self.cooked_time < 6:
            self.state = "半生不熟"
        # [6, 8) -> 熟了
        elif 6 <= self.cooked_time < 8:
            self.state = "熟了"
        # 大于等于8 -> 烤糊了
        elif self.cooked_time >= 8:
            self.state = "烤糊了"

    # 5.3 定义 add_condiments(self, temp), temp为添加什么佐料的参数
    def add_condiments(self, condiment):
        # 5.3.1 佐料列表追加元素
        self.condiments.append(condiment)


# 4. 主逻辑程序
# 4.1 创建 地瓜对象
sp1 = SweetPotato()
print(sp1)

# 4.2 分多次烧烤地瓜
sp1.cook(2)
# 5.4 再次测试代码，添加佐料，重新打印信息
sp1.add_condiments("盐")
# 4.3 每烧烤一次，输出地瓜信息
print(sp1)

sp1.cook(5)
sp1.add_condiments("孜然")
print(sp1)

sp1.cook(2)
sp1.add_condiments("辣椒")
print(sp1)
