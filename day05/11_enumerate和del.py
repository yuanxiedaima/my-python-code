# @Time : 2022/1/26 23:32 
# @Author : Jface 
# @desc : 遍历列表，同时把索引位置能打印

# 0. 定义一个列表
user_list = [{'name': 'mike', 'age': 34, 'tel': '110'},
             {'name': 'yoyo', 'age': 18, 'tel': '120'}]

# 1. 普通方法
i = 0
for user_dict in user_list:
    print(i + 1, user_dict)
    i += 1
print("=" * 20)
# 2. 通过enumerate方法实现
# enumerate(容器变量)：获取到：元素位置，元素
for i, user_dict in enumerate(user_list):
    print(i + 1, user_dict)

print("=" * 20)
# 3. 通过del删除列表元素 del 列表[索引位置]
# 删除索引位置为0的元素
print(user_list)
del (user_list[0])
print(user_list)
