# @Time : 2022/1/26 23:15 
# @Author : Jface 
# @desc : 列表推导式， 通过for添加列表元素的简洁写法

# 普通方法：遍历 0~4 范围的元素，这些元素添加到列表
my_list = []
for i in range(5):
    my_list.append(i)

print(my_list)

print("=" * 20)

# 通过列表推导式，实现上面的效果 [计算公式 for循环体]
# 1. for i in range(5), 取出0，放在i变量中，i追加到列表
my_list = [i for i in range(5)]
# 2. 循环下一步，取出2，放在i变量中，i追加到列表
# 重复，直到退出循环
print(my_list)
print("=" * 20)

# 0~10之间数，偶数才添加到列表
# 普通方法实现
my_list = []
for i in range(11):
    if i % 2 == 0:
        my_list.append(i)
print(my_list)
print("=" * 20)
# 列表推导式实现
# [i for i in range(11) if i % 2 == 0]
# 1. for i in range(11)取第一个元素
# 2. if i % 2 == 0
# 3. 上面满足条件的i, 条件到列表
my_list = [i for i in range(11) if i % 2 == 0]
print(my_list)
