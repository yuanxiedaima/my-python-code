# @Time : 2022/1/23 21:22 
# @Author : Jface 
# @desc :
"""
字典[键] = 值	键不存在，会添加键值对
字典.pop(键)	    删除指定键值对,返回被删除的值,如果键不存在,会报错
"""
# 字典定义
student_dict = {"name": "rose", "age": 20}
print(student_dict)

# 字典[键] = 值	键不存在，会添加键值对
student_dict["city"] = "sz"
print(student_dict)

# 字典.pop(键)	    删除指定键值对,返回被删除的值,如果键不存在,会报错
age = student_dict.pop("age")
print(age)
print(student_dict)

# student_dict.pop("age")
