# @Time : 2022/1/23 20:40 
# @Author : Jface 
# @desc :
"""
列表[索引] = 值	修改指定索引的数据，数据不存在会报错
列表[索引]        根据索引取值，索引不存在会报错
len(列表)	    列表长度(元素个数)
if 值 in 列表:	判断列表中是否包含某个值
"""
temp_list = [1, 2, 3, 4]
print(temp_list)

# 修改
temp_list[-1] = 5
print(temp_list)

# 访问索引为 1 的元素
print(temp_list[1])

# 列表长度，就是元素个数
print(len(temp_list))

# 判断元素是否在列表
if 3 in temp_list:
    print("3 在列表中")
else:
    print("3 不在列表中")
