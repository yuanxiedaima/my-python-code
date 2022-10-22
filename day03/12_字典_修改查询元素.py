# @Time : 2022/1/23 21:25 
# @Author : Jface 
# @desc :
"""
字典[键] = 值	键存在，会修改键值对的值
字典[键]	        根据键取值，键值对不存在会报错
字典.get(键)	    根据键取值，键值对不存在返回None, 不会报错
"""
student_dict = {"name": "rose", "age": 20}
print(student_dict)

# 字典[键] = 值	键存在，会修改键值对的值
student_dict["name"] = "tom"
print(student_dict)

# 字典[键]	        根据键取值，键值对不存在会报错
name = student_dict["name"]
print(name)

# 字典.get(键)	    根据键取值，键值对不存在返回None, 不会报错
age = student_dict.get("age")
print(age)
city = student_dict.get("city")
print(city)
