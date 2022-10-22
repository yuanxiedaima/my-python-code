# @Time : 2022/2/2 21:22 
# @Author : Jface 
# @desc :
"""
方式1：
导入格式：   import 包名.模块名
            包名就是文件夹名    模块名就是文件名字
使用格式：   包名.模块名.工具   (类名、函数、变量)

方式2：
导入格式：   from 包名.模块名 import send_test
使用格式：   工具   (类名、函数、变量)
"""

# 搜索路径，默认找当前路径
# 方式1
import msg.sendmsg

msg.sendmsg.send_msg()

# 方式2
from msg.sendmsg import send_msg

send_msg()
