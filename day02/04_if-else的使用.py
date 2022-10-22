# @Time : 2022/1/23 14:39 
# @Author : Jface 
# @desc :

# 1. 输入用户年龄，input返回值是字符串，类型转换为int
age = int(input("请输入用户的年龄："))
# 2. if 判断是否满 18 岁:
# if age >= 18:
# 2.1 如果满 18 岁，打印一句话：允许进网吧嗨皮
#    print("允许进网吧嗨皮")
# 3. 否则，未满 18 岁
# else:
# 3.1 打印一句话：提示回家写作业
#    print("回家写作业")

# 使用三目运算符实现 if  else 的效果
print("允许进网吧嗨皮") if age >= 18 else print("回家写作业")
