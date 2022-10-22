# @Time : 2022/2/3 21:20 
# @Author : Jface 
# @desc :
"""
1. 以前存储
    user_list = [{'name':'mike', 'age':34, 'tel':'110'},
                {'name':'yoyo', 'age':24, 'tel':'120'}]

2. user_list = [对象1，对象2]
    2.1 对象类设计，学生类：属性有name, age, tel
"""


class Student(object):
    def __init__(self, _name, _age, _tel):
        self.name = _name
        self.age = _age
        self.tel = _tel

    def __str__(self):
        return '我叫: %s, 我今年: %s 岁, 我电话: %s' % (self.name, self.age, self.tel)


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
"""
for obj in user_list:
    print(obj)

"""
写文件：
# 1. 将[对象1， 对象2] 转换为 [{}, {}]
# 2. str([{}, {}])转换后，写入文件
"""
new_user_list = []
for obj in user_list:
    user_dict = {
        "name": obj.name,
        "age": obj.age,
        "tel": obj.tel
    }
    new_user_list.append(user_dict)

with open("test.txt", "w") as file:
    file.write(str(new_user_list))

"""
读文件：
# 1. 从文件读出来的内容是字符串，通过eval转换为[{}, {}]
# 2. 从列表中取出字典，再取出字典的元素，这个元素用新建对象
# 3. 列表追加对象
"""
with open("test.txt", "r") as file:
    data = file.read()
    new_user_list = eval(data)

user_list = []
for user_dict in new_user_list:
    obj = Student(user_dict["name"], user_dict["age"], user_dict["tel"])
    user_list.append(obj)

for obj in user_list:
    print(obj)
