# @Time : 2022/1/23 22:07 
# @Author : Jface 
# @desc : 字符串.replace(原内容, 新内容, 替换次数)	 返回一个替换了原内容的新字符串，可以指定替换次数

str1 = "hello python2.5 python3.4 python3.5 python3.6 python3.8"

# 源字符串里的py，替换为Py，返回值才是替换后的内容
new_str = str1.replace("py", "Py")
print(new_str)

new_str = str1.replace("py", "Py", 2)
print(new_str)
