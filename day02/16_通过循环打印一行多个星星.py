# @Time : 2022/1/23 15:54 
# @Author : Jface 
# @desc :
"""
要求：每一次只能打印 1 个 *
print()默认是换行的
print('* ', end=''), end=''让打印不换行
"""
print("* ", end='')
# print()
print("* ", end='')
print("* ", end='')
print("* ", end='')
print("* ", end='')
print()

print("=========华丽分割线=========")

# 要求：通过循环实现打印1行多个星星
# 1 定义循环条件变量 j = 0
j = 0
# 2 循环 while j < 5:
while j < 5:
    # 3 打印一个星星，end=''作用指定不换行打印
    print("* ",end='')
    # 4 循环的条件变量改变
    j += 1
print()
