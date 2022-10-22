# @Time : 2022/2/3 21:40 
# @Author : Jface 
# @desc :
"""
学生类Student：保存学生的基本信息
1. __init__添加属性name, age, tel
2. __str__返回实例属性信息
3. to_dict，将属性内容以字典的形势返回

学生管理类ManagerStuSys，管理学生：增删改查学生信息
1. __init__添加属性，专门保存学生对象，属性是列表
2. 设计方法，测试功能使用
3. 类的外面，创建学生管理类，调用测试功能方法
"""


class Student(object):
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return 'name:%s\t, age:%s\t, tel:%s\t' % (self.name, self.age, self.tel)

    def to_dict(self):
        return {'name': self.name, 'age': self.age, 'tel': self.tel}


class ManagerStuSys(object):
    def __init__(self):
        self.stu_list = []

    def test(self):
        stu1 = Student('张三', 20, '123456789')
        stu2 = Student('李四', 21, '987654321')
        stu3 = Student('王五', 22, '123456789')

        self.stu_list.append(stu1)
        self.stu_list.append(stu2)
        self.stu_list.append(stu3)

        print("序号\t姓名\t年龄\t电话")
        for i, obj in enumerate(self.stu_list):
            print(f"{i + 1}\t{obj}")

        for obj in self.stu_list:
            print(obj.to_dict())


ms = ManagerStuSys()
ms.test()
