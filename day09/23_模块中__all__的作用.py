# @Time : 2022/2/2 21:14 
# @Author : Jface 
# @desc :
"""
1. 模块中__all__变量，只对from xxx import *这种导入方式有效
2. __all__格式：
    __all__ = ['变量名', '类名', '函数名'……]
3. 模块中__all__变量包含的元素，才会被from xxx import *导入
"""

from module5 import *
# 导入module5模块中`所有`功能, 这里的所有时指__all__列举的功能
ret = my_add(10,20)
print(ret)

# ret = module5.my_sub(100,2)
# print(ret)

print(num)

import module5


ret = module5.my_sub(100, 2)
print(ret)
