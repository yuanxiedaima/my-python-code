"""
学生名片管理系统
"""

# 0. 函数的外面，定义一个全局变量(列表)，用于保存用户信息
user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]


# 显示菜单函数定义
def show_menu():
    print('=' * 20)
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')
    print('=' * 20)


# 定义新建学生的函数
def add_stu_info():
    """添加学生信息"""
    # 1. 输入用户信息：姓名、年龄、电话
    _name = input('请输入学生姓名：')
    _age = int(input('请输入学生年龄：'))  # 年龄应该是整型，所有做了int转换
    _tel = input('请输入学生电话：')

    # 2. 通过for遍历，取出某个元素后，这个元素就是字典
    for user_dict in user_list:
        # 2.1 字典[‘name’] == 用户输入的名字，是否相等，相等则跳出循环
        if user_dict['name'] == _name:
            print('此用户已经存在，请重来')
            # 2.2 break跳出循环
            break
    else:
        # 3. for中的else 如果用户不存在列表中，添加用户字典到列表
        # 3.1 创建字典
        info_dict = {'name': _name, 'age': _age, 'tel': _tel}

        # 3.2 追加列表
        # user_list是可变类型，没有重新赋值，没有改变原来地址，所以不用global声明
        user_list.append(info_dict)


# 显示所有的学生，带序号的
def show_all_stu():
    """显示所有的学生"""
    # 1. 遍历前，打印一些提示信息：序号    姓名  年龄  电话
    # \t一个tab键的空格
    print('序号\t\t姓名\t\t年龄\t\t电话')

    # 2. 遍历 for 索引位置，字典 in enumerate(user_list)：
    for i, user_dict in enumerate(user_list):
        # 2.1 打印一个用户的信息 索引位置+1，user_dict[‘name’]……
        print('%d\t\t%s\t\t%d\t\t%s' % (i + 1, user_dict['name'], user_dict['age'], user_dict['tel']))


# 显示某个学生
def show_one_stu():
    """显示某个学生"""
    # 1. 输入姓名
    _name = input('请输入学生姓名：')

    # 2. 通过for遍历，取出一个字典user_dict
    for user_dict in user_list:
        # 2.1 user_dict[‘name’]和输入姓名判断
        if user_dict['name'] == _name:
            # 2.1.1 如果相等，输出用户信息，退出循环
            print('查询到的用户信息如下：')
            print('%s\t%d\t%s' % (user_dict['name'], user_dict['age'], user_dict['tel']))
            break
    # 3. for中的else，循环执行完毕，没有break，说明用户不存在，提示一下
    else:
        print('查询的用户不存在')


def update_stu_by_name():
    """更新某个学生信息，根据输入的姓名匹配哪个学生"""
    # 1. 输入需要修改的用户姓名
    update_name = input('输入需要修改的用户姓名：')

    # 2. for遍历，带索引的遍历   i, user_dict  in user_list
    for i, user_dict in enumerate(user_list):
        # 2.1 如果user_dict['name']和输入用户名字相等
        if user_dict['name'] == update_name:
            # 2.1.1 重新输入新的姓名、年龄、电话
            _name = input('请输入新的学生姓名：')
            _age = int(input('请输入新的学生年龄：'))
            _tel = input('请输入新的学生电话：')
            # 2.1.2 对user_list[i]['name'] = 新的name
            user_list[i]['name'] = _name
            user_list[i]['age'] = _age
            user_list[i]['tel'] = _tel
            # 2.1.3 ……、修改成功打印、break跳出循环
            print('修改成功')
            break
    # 3. for中的else 输入的用户不在列表
    else:
        print('输入的用户不在列表，请重新输入')


def del_stu_by_name():
    """删除某个学生，根据输入的姓名"""
    # 1. 输入用户姓名
    _name = input('请输入需要删除的名字：')

    # 2. for遍历，带索引的遍历   i, user_dict
    for i, user_dict in enumerate(user_list):
        # 2.1 如果user_dict['name']和输入用户名字相等
        if user_dict['name'] == _name:
            # 2.1.1 del 列表[i], 同时break跳出循环
            del user_list[i]
            print('删除成功')
            break
    # 3. for中else 输入的用户在列表中，不存在
    else:
        print('用户不在列表中，无法删除')


# 写一个主程序
def main():
    # 1. 死循环
    while True:
        # 调用菜单
        show_menu()

        # 2. 用户输入数字
        cmd = input("请输入功能数字：")

        # 3. 条件选择
        if cmd == "1":
            # print('添加学生')
            add_stu_info()
            # print(user_list) # 打印列表，做测试，看数据
        elif cmd == "2":
            # print('查询所有学生')
            show_all_stu()

        elif cmd == "3":
            # print('查询某个学生')
            show_one_stu()

        elif cmd == "4":
            # print('修改某个学生')
            update_stu_by_name()
        elif cmd == "5":
            # print('删除某个学生')
            del_stu_by_name()
        elif cmd == "6":
            print('退出循环')
            break
        else:
            print('输入有误，请重新输入')


# 调用主程序
main()
