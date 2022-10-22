# @Time : 2022/1/27 22:54 
# @Author : Jface 
# @desc :
"""
1. 死循环
2. 用户输入数字
3. 条件选择
"""
while True:
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
