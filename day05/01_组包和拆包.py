# @Time : 2022/1/25 23:06 
# @Author : Jface 
# @desc :
"""
# 组包：= 右边有多个数据时, 会自动包装为元组，多变一
# 拆包：如果 变量数量 = 容器长度, 容器中的元素会一一对应赋值给变量，一变多，取出有用的信息
"""

# 组包，多变一
result = 1, 2, 3
print(result, type(result))

# 拆包，一变多
a, b, c = result
print(a, b, c)

# a, b = result   # ValueError: too many values to unpack (expected 2)
# print(a, b)


# 列表拆包
a, b, c = [10, 20, 30]
print(a, b, c)
# 字典拆包
a, b, c = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(a, b, c)

my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
# for temp in my_dict.items():
#     print(temp, type(temp))
#     key, value = temp
#     print(key, value)
for key, value in my_dict.items():
    print(key, value)

# 字符串拆包
a, b, c = "hel"
print(a, b, c)
