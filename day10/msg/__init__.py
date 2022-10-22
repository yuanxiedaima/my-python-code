"""
导入包，自动执行__init__.py文件的内容
"""
print("__init__文件被执行了, 控制包中模块的导入")

# from . import sendmsg
# from . import recvmsg

# from msg import sendmsg
# from msg import recvmsg

from msg.sendmsg import send_msg
from msg.recvmsg import recv_msg
