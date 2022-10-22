# @Time : 2022/1/26 23:07 
# @Author : Jface 
# @desc :
"""
for 变量 in range(5), range(5)序列范围，使用和切片一样，但是以,隔开
"""
# for i in range(0, 5):
for i in range(5):
    print(i)

print("====分割线====")
# 求 1 ~ 100 累加
_sum = 0
for i in range(1, 101):
    _sum += i

print(_sum)
print("====分割线====")

# 验证步长，打印 0、2、4
for i in range(0, 5, 2):
    print(i)
print("====分割线====")
for i in range(0, 5, -1): # 不支持负数步长
    print(i)
