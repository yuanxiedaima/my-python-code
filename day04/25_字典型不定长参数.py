# @Time : 2022/1/25 22:58 
# @Author : Jface 
# @desc :
"""
函数形参变量，前面有2个*，字典型不定长参数、也叫关键字型不定长参数
函数内部使用，无需加*
**kwargs, 这个参数一定是放在最右边

把实参包装成 {'city': 'sz', 'age': 18}给kwargs传递
kwargs = {'city': 'sz', 'age': 18}
def foo(name, age, sex):
     print(name, age, sex)
"""

# 函数定义
def foo(name, **kwargs):
    print(name, kwargs, type(kwargs))


# 函数调用
# 实参的写法： 变量=数据，变量=数据
foo(name="rose", age = 18, sex = "male")
foo(name="tom")
foo("lily")
foo("mike", age=19, sex="male", city="sz", like=["sing", "dance"])