# @Time : 2022/1/23 21:28 
# @Author : Jface 
# @desc : 遍历字典, 获取所有的键值对 (键, 值)

student_dict = {"name": "rose", "age": 20}

# for k in 字典变量:
for key in student_dict:
    print("%s: %s" % (key, student_dict[key]))

print("=====华丽分割线=====")

# 遍历字典, 获取所有的键值对 (键, 值)
# for k, v in 字典变量.items():
#     print(k, v)
for key, value in student_dict.items():
    print("%s: %s" % (key, value))
