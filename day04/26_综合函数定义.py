# @Time : 2022/1/25 23:02 
# @Author : Jface 
# @desc :
"""
# 1. 关键字参数必须在位置参数右边
# 2. args: 不定长的位置参数
# 3. kwargs: 不定长的关键字参数
"""


# 扩展: 多种参数同时出现时的函数定义的模板:
def foo(name, *args, city="sz", **kwargs):
    print(name, args, city, kwargs)


# 函数调用
foo("rose")
foo("tom", city="bj")
foo("tom", 18, "male")

# tom (18, 'male') shenzhen {'cls': 'python42期', 'like': 'python'}
foo("tom", 18, 'male', city='shenzhen', cls="python42期", like='python')
