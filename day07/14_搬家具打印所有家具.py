# @Time : 2022/2/1 20:25 
# @Author : Jface 
# @desc :
"""
家具类 Item
# 1. 定义__init__方法，添加2个属性，需要2个形参 _type, _area
    # 1.1 家具类型 type
    # 1.2 家具面积 area

# 2. 实现__str__方法
    # 2.1 返回家具类型和家具面积

房子类 Home
# 1. 定义__init__方法，添加3个属性，需要3个形参
    # 1.1 地址 address
    # 1.2 房子面积 area
    # 1.3 房子剩余面积 free_area，默认为房子的面积

# 2. 实现__str__方法
    # 2.1 返回房子地址、面积、剩余面积信息

# 3. 实现add_item方法，提供item参数来添加家具，item是对象
    # 3.1 如果 房间的剩余面积 >= 家具的面积，可以容纳家具：
        # 3.1.1 打印添加家具的类型和面积
        # 3.1.2 剩余面积 减少
    # 3.2 否则 不能容纳家具：提示家具添加失败

主程序逻辑：
# 1. 创建 家具对象, 输出 家具信息
# 2. 创建 房子对象, 输出 房子信息
# 3. 房子添加家具, 输出 房子信息

输出房子时，显示包含的所有家具的类型
# a. Home类中添加 item_type_list 属性(家具类型列表)，用于记录所有家具类型
# b. Home类的 add_item 方法中, 将添加成功的 家具类型 添加到 item_type_list 中
# c. Home类的 __str__ 方法中, 打印家具的类型列表
"""


# 家具类 Item
class Item(object):
    # 1. 定义__init__方法，添加2个属性，需要2个形参 _type, _area
    def __init__(self, _type, _area):
        # 1.1 家具类型 type
        self.type = _type
        # 1.2 家具面积 area
        self.area = _area

    # 2. 实现__str__方法
    # 2.1 返回家具类型和家具面积
    def __str__(self):
        return f"家具类型: {self.type} 家具面积: {self.area}"


# 房子类 Home
class Home(object):
    # 1. 定义__init__方法，添加3个属性，需要3个形参
    def __init__(self, _address, _area, _free_area):
        # 1.1 地址 address
        self.adress = _address
        # 1.2 房子面积 area
        self.area = _area
        # 1.3 房子剩余面积 free_area，默认为房子的面积
        self.free_area = _free_area
        # a. Home类中添加 item_type_list 属性(家具类型列表)，用于记录所有家具类型
        self.item_type_list = []

    # 2. 实现__str__方法
    def __str__(self):
        # 2.1 返回房子地址、面积、剩余面积信息
        # c. Home类的 __str__ 方法中, 打印家具的类型列表
        return f"房子地址是：{self.adress} 房子面积是：{self.area} 房子剩余面积是：{self.free_area} 房子中已添加的家具: {self.item_type_list}"

    # 3. 实现add_item方法，提供item参数来添加家具，item是对象
    def add_item(self, item):
        # 3.1 如果 房间的剩余面积 >= 家具的面积，可以容纳家具：
        if self.free_area >= item.area:
            # 3.1.1 打印添加家具的类型和面积
            print(f"添加家具成功，家具类型: {item.type} 占地面积: {item.area}")
            # 3.1.2 剩余面积 减少
            self.free_area -= item.area
            # b. Home类的 add_item 方法中, 将添加成功的 家具类型 添加到 item_type_list 中
            self.item_type_list.append(item.type)
        # 3.2 否则 不能容纳家具：提示家具添加失败
        else:
            print("家具添加失败, 再买一个大的房子")


# 主程序逻辑：
# 1. 创建 家具对象, 输出 家具信息
tv = Item("超大电视", 20)
print(tv)
# 2. 创建 房子对象, 输出 房子信息
h = Home("北京一环四合院", 160, 160)
print(h)
# 3. 房子添加家具, 输出 房子信息
i = Item("超级大床", 40)
print(i)

h.add_item(tv)
print(h)

h.add_item(i)
print(h)
