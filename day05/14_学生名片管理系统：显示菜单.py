# @Time : 2022/1/27 22:54 
# @Author : Jface 
# @desc :
"""
显示菜单
"""


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
