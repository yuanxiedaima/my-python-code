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

    # 写一个主程序
    def start(self):
        # 2.1 程序启动时，循环的前面，调用加载数据函数
        # load_info()

        # 1. 死循环
        while True:
            # 调用菜单
            # self.show_menu()

            # 2. 用户输入数字
            cmd = input("请输入功能数字：")

            # 3. 条件选择
            if cmd == "1":
                print('添加学生')
                # self.add_stu_info()
                # print(user_list) # 打印列表，做测试，看数据
            elif cmd == "2":
                print('查询所有学生')
                # self.show_all_stu()
            elif cmd == "3":
                print('查询某个学生')
                # self.show_one_stu()
            elif cmd == "4":
                print('修改某个学生')
                # self.update_stu_by_name()
            elif cmd == "5":
                print('删除某个学生')
                # self.del_stu_by_name()
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
