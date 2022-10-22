# @Time : 2022/2/3 21:52 
# @Author : Jface 
# @desc :
"""
学生管理系统设计：主逻辑设计
"""


class Student(object):

    def __init__(self, _name, _age, _tel):
        self.name = _name
        self.age = _age
        self.tel = _tel

    def __str__(self):
        return f"{self.name}\t{self.age}\t\t{self.tel}"

    def to_dict(self):
        return {"name": self.name, "age": self.age, "tel": self.tel}


class ManagerStuSys(object):

    def __init__(self):
        self.user_list = []

    # 显示功能菜单
    @staticmethod
    def show_menu():
        print("=" * 20)
        print("= 1. 添加学生")
        print("= 2. 查询所有学生")
        print("= 3. 查询某个学生")
        print("= 4. 修改某个学生")
        print("= 5. 删除某个学生")
        print("= 6. 保存信息")  # 1.1 菜单增加保存信息的提示
        print("= 7. 退出系统")
        print("=" * 20)

    # 定义新建学生函数
    def add_stu_info(self):
        """添加学生信息"""
        # 1.输入用户信息
        _name = input("请输入姓名：")
        _age = int(input("请输入年龄："))
        _tel = input("请输入电话：")

        # 2.遍历取出元素，判断是否重复
        for obj in self.user_list:
            if obj.name == _name:
                print("姓名重复，请重新输入")
                break
        else:
            # 3.创建对象
            new_stu = Student(_name, _age, _tel)
            # 4.添加到列表
            self.user_list.append(new_stu)
            print("添加成功")

    # 显示所有的学生，带序号的
    def show_all_stu(self):
        """显示所有学生信息"""
        print("序号\t\t姓名\t\t年龄\t\t电话")
        for i, obj in enumerate(self.user_list):
            print(f"{i + 1}\t{obj}")

    # 显示某个学生
    def show_one_stu(self):
        # 1.输入姓名
        _name = input("请输入要查询的姓名：")
        for obj in self.user_list:
            if obj.name == _name:
                print("查找到学生信息如下：")
                print(obj)
                break
        else:
            print("没有找到该学生")

    # 修改某个学生信息
    def update_stu_by_name(self):
        """"更新某个学生信息，根据输入姓名匹配哪个学生"""
        update_name = input("请输入要修改的学生姓名：")
        for obj in self.user_list:
            if obj.name == update_name:
                obj.name = input("请输入新的学生姓名：")
                obj.age = int(input("请输入新的学生年龄："))
                obj.tel = input("请输入新的学生电话：")
                print("修改成功")
                break
            else:
                print("输入的用户不在列表，请重新输入")

    def del_stu_by_name(self):
        """删除某个学生信息，通过输入的名字"""
        _name = input("请输入要删除的学生姓名：")
        for i, obj in enumerate(self.user_list):
            if obj.name == _name:
                del self.user_list[i]
                print("删除成功")
                break
            else:
                print("输入的用户不在列表，无法删除")

    # 写一个主程序
    def start(self):
        # 2.1 程序启动时，循环的前面，调用加载数据函数
        # load_info()

        # 1. 死循环
        while True:
            # 调用菜单
            self.show_menu()

            # 2. 用户输入数字
            cmd = input("请输入功能数字：")

            # 3. 条件选择
            if cmd == "1":
                print('添加学生')
                self.add_stu_info()
                # print(user_list)  # 打印列表，做测试，看数据
            elif cmd == "2":
                print('查询所有学生')
                self.show_all_stu()
            elif cmd == "3":
                print('查询某个学生')
                self.show_one_stu()
            elif cmd == "4":
                print('修改某个学生')
                self.update_stu_by_name()
            elif cmd == "5":
                print('删除某个学生')
                self.del_stu_by_name()
            elif cmd == '6':  # 1.2 主逻辑增加 名片信息保存到文件 的选择
                # save_info()
                print('保存学生信息到文件')
            elif cmd == "7":
                print('退出循环')
                break
            else:
                print('输入有误，请重新输入')


ms = ManagerStuSys()
ms.start()
