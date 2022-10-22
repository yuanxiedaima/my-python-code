# @Time : 2022/1/23 22:04 
# @Author : Jface 
# @desc : 字符串.find(目标字符串, 开始索引, 结束索引)	在指定范围内, 查询目标字符串的索引, 不存在返回-1
str1 = "hello abc python"

# 在str1字符串中，查找’abc‘字符串，返回找到字符串所对应的索引
index = str1.find("abc")
print(index)
# 如果没有找到，返回-1
index = str1.find("88")
print(index)

# 指定区间查找子串, 从索引2到索引11-1为止
index = str1.find("py", 2, 11) # [2,11) 包括开始索引，不包括结尾索引
print(index)