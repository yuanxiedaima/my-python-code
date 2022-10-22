# @Time : 2022/1/23 16:07 
# @Author : Jface 
# @desc : 循环里面没有遇到break语句，while执行完后，则会执行else的分支
i = 0
while i < 10:
    print("跑了%d圈" % (i+1))
    if i ==4:
        break
    i += 1
else:
    print("while循环中没有break, 不仅会执行while语句, 还会执行else语句")
