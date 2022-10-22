# @Time : 2022/2/3 20:54 
# @Author : Jface 
# @desc :
"""
1. 以前存储
    user_list = [{'name':'mike', 'age':34, 'tel':'110'},
                {'name':'yoyo', 'age':24, 'tel':'120'}]

2. user_list = [对象1，对象2]
    2.1 对象类设计，学生类：属性有name, age, tel
"""


class Student:
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return '我叫:%s, 我今年:%s岁了, 我的电话号码是:%s' % (self.name, self.age, self.tel)


"""
增加学生:
# 1. 定义空列表
# 2. 创建对象
# 3. 列表追加对象
"""

user_list = []
stu = Student('rose', 18, "123")
user_list.append(stu)
stu = Student('mike', 20, "123")
user_list.append(stu)
stu = Student('lily', 19, "123")
user_list.append(stu)
stu = Student('yoyo', 20, "123")
user_list.append(stu)

"""
遍历打印信息:
# 1. 遍历从列表取出对象
# 2. 打印的是对象.属性
# 如果列表中是对象，直接打印列表，打印的是对象的地址，不能打印对象的属性
"""
for obj in user_list:
    print(obj)

"""
查询某人：
# 1. 遍历从列表取出对象
# 2. 判断对象.name和查找的用户是否相等
# 3. 如果相等，打印对象的相应属性信息，然后break
# 4. for的else，提示没有此人
"""
search_name = input("请输入要查询的姓名:")
for obj in user_list:
    if obj.name == search_name:
        print("查询到学生如下：", obj)
    else:
        print("查无此人")

"""
修改某人：
# 1. 通过enumerate(user_list)带序号遍历：索引、对象
# 2. 判断对象.name和修改的用户是否相等
# 3. 修改内容，然后break
# 4. for的else，提示没有此人
"""
update_name = input("请输入要修改的姓名:")
for obj in user_list:
    if obj.name == update_name:
        obj.name = input("请输入新的姓名:")
        obj.age = input("请输入新的年龄:")
        obj.tel = input("请输入新的电话:")
        print("修改成功")
        break
else:
    print("没有此人")

"""
删除某人：
# 1. 通过enumerate(user_list)带序号遍历：索引、对象
# 2. 判断对象.name和删除的用户是否相等
# 3. 通过 del 列表[索引] 删除元素，然后break
# 4. for的else，提示没有此人
"""
del_name = input("请输入要删除的姓名:")
for i, obj in enumerate(user_list):
    if obj.name == del_name:
        del user_list[i]
        print("删除成功")
        break
else:
    print("没有此人")

