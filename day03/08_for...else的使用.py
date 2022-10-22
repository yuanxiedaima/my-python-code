# @Time : 2022/1/23 21:04 
# @Author : Jface 
# @desc :
name_list = ['rose', 'tom', 'jack', 'mike']

for name in name_list:
    print(name)
    if name == 'tom':
        print("跳出循环")
        break
else:
    print("for循环执行结束,没有遇到break,执行else里面的代码块")
