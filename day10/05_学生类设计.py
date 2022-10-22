# @Time : 2022/2/3 21:33 
# @Author : Jface 
# @desc :
"""
学生类：保存学生的基本信息
1. __init__添加属性name, age, tel
2. __str__返回实例属性信息
3. to_dict，将属性内容以字典的形势返回
"""


class Student(object):

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return 'name: %s, age: %s, tel: %s' % (self.name, self.age, self.tel)

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'tel': self.tel
        }


"""
增加学生:
# 1. 定义空列表
# 2. 创建对象
# 3. 列表追加对象
"""
user_list = []
stu1 = Student("rose", 19, "123")
stu2 = Student("jack", 20, "233")
stu3 = Student("tome", 21, "223")

user_list.append(stu1)
user_list.append(stu2)
user_list.append(stu3)

"""
遍历打印信息:
# 1. 遍历从列表取出对象
# 2. 打印的是对象，打印__str__返回值
# 3. 以字典格式打印信息
"""
print("序号\t姓名\t年龄\t电话")
for i, obj in enumerate(user_list):
    print(f"{i + 1}\t{obj}")

for obj in user_list:
    print(obj.to_dict())
