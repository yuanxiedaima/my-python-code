# @Time : 2022/1/27 22:54 
# @Author : Jface 
# @desc :
"""
显示所有的学生，带序号
# 定义函数
# 1. 遍历前，打印一些提示信息：序号    姓名  年龄  电话
# 2. 遍历 for 索引位置，字典 in enumerate(user_list)：
# 2.1 打印一个用户的信息 索引位置+1，user_dict[‘name’]……
"""
# 0. 函数的外面，定义一个全局变量(列表)，用于保存用户信息
user_list = [{"name": "rose", "age": 20, "tel": "222"},
             {"name": "mike", "age": 21, "tel": "111"}]

# 定义显示所有学生信息的函数
def show_student():
    """显示所有学生信息"""
    # 1. 遍历前，打印一些提示信息：序号    姓名  年龄  电话
    print("序号\t\t姓名\t\t年龄\t\t电话")
    # 2. 遍历 for 索引位置，字典 in enumerate(user_list)：
    for i, user_dict in enumerate(user_list):
        # 2.1 打印一个用户的信息 索引位置+1，user_dict[‘name’]……
        print("%d\t\t%s\t%02d\t\t%s" % (i + 1, user_dict['name'], user_dict['age'], user_dict['tel']))


# 定义新建学生的函数
def add_student():
    # 1. 输入用户信息：姓名、年龄、电话
    name = input("请输入学生姓名：")
    age = int(input("请输入学生年龄："))
    tel = int(input("请输入学生电话："))
    # 2. 通过for遍历，取出某个元素后，这个元素就是字典
    for user_dict in user_list:
        # 2.1 字典[‘name’] == 用户输入的名字，是否相等，相等则跳出循环
        if user_dict["name"] == name:
            print("该学生已经在列表，无需保养")
            # 2.2 break跳出循环
            break
        # 3. for中的else 如果用户不存在列表中，添加用户字典到列表
        else:
            # 3.1 创建字典
            new_dict = {"name": name, "age": age, "tel": tel}
            # 3.2 追加列表
            user_list.append(new_dict)


def menu():
    """ 输出菜单 """
    print("=" * 30)
    print("= 1. 添加学生")
    print("= 2. 查询所有学生")
    print("= 3. 查询某个学生")
    print("= 4. 修改某个学生")
    print("= 5. 删除某个学生")
    print("= 6. 退出系统")
    print("=" * 30)


def main():
    """学生管理系统主程序"""
    while True:
        menu()
        num = int(input("请输入功能数字："))
        if num == 1:
            print("添加学生")
            add_student()
        elif num == 2:
            print("查询所有学生")
        elif num == 3:
            print("查询某个学生")
        elif num == 4:
            print("修改某个学生")
        elif num == 5:
            print("删除某个学生")
        elif num == 6:
            print("退出系统")
            break
        else:
            print("输入有误，请重新输入")


main()
