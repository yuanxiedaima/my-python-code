# @Time : 2022/1/25 23:15 
# @Author : Jface 
# @desc :

# 一 交换变量的值
# 1. 借助辅助变量
a = 10
b = 20
print(a, b)

tmp = a
a = b
b = tmp
print(a, b)

# 2. 不借助辅助变量
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)


# 二 函数可以同时返回多个数
def foo():
    return 1, 2, 3


# 函数调用

# 变量名 = 函数()
ret = foo()
x, y, z = ret
print(ret, type(ret))
print(x, y, z)

# 返回值直接做拆包
r1, r2, r3 = foo()
print(r1, r2, r3)

# 3. 字典元素拆包
# 遍历字典，取出每一个item
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
for key, value in my_dict.items():
    print(key, value)
