# @Time : 2022/1/24 22:32 
# @Author : Jface 
# @desc :
# 内建（内置）函数
# 通过len获取容器类型的元素个数
my_list = [1, 2, 3, 4]
print(len(my_list))
my_set = set(my_list)
print(len(my_set))

# 运算符
# +：拼接，同类型的容器
# 字符串拼接合并
print("hello " + "world")

# 列表元素拼接合并
print([1, 2, 3] + [10, 20, 30])
print((10, 20, 30) + (100, 200, 300))

# *: 赋值
print([1, 2, 3] * 10)
print("=" * 20 + "华丽分割线" + "=" * 20)
