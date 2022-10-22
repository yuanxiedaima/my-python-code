# @Time : 2022/1/31 20:39 
# @Author : Jface 
# @desc :

# 定义类，只是定义了一个类型
class Dog(object):

    def eat(self):  # 定义方法时,self这个形参是必须写的.
        print("啃骨头")

    def drink(self):
        print("喝汤")


# 创建对象格式：实例对象变量名 = 类名()
dog1 = Dog()
# 对象变量.方法名字(), self不用处理
dog1.eat()  # 调用对象方法时,self参数会自动由解释器传递.
dog1.drink()  # ....


dog2 = Dog()
dog2.eat()
dog2.drink()
