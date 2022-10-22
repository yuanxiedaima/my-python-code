# @Time : 2022/1/23 20:50 
# @Author : Jface 
# @desc : 从头开始找，直到结束

name_list =['rose', 'mike', 'tom', 'jack']

# while 实现遍历
# 1.定义变量
i = 0
# 2.while i < 列表元素个数
while i < len(name_list):
# 3.取出元素打印
    print(name_list[i])
# 条件变量的修改
    i += 1

print("======华丽分割线======")
# for 遍历循环
for name in name_list:
    print(name)
