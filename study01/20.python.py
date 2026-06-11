
#类的定义
class Car:
    pass

#创建对象
c1=Car()
#动态为对象添加属性-->不推荐
c1.brand="BWM"
c1.name="X5"
c1.price=500000
#__dict__是python中用户自定义类实例的一个特殊属性，用于以字典形式存储对象的属性
#__dict__存储c1所有的属性和属性值
print(c1.__dict__) #会将对象中所有属性以字典的形式输出


#定义类
class Car1:
    #def：定义在类外面叫函数，定义在类里面叫方法
    #__init__:初始化方法。对象创建后自动调用，用于设置对象的初始状态（设置对象属性）
    #self：方法的第一个参数，表示当前创建的实例对象（类似于this）
    def __init__(self,c_brand,c_name,price):
        self.c_brand=c_brand
        self.c_name=c_name
        self.price=price

    def running(self):
        print(f"{self.c_brand} {self.c_name} 正在高速行驶...")
    def total_cost(self,discount,rate):
        return self.price*rate*discount

#创建对象
car1=Car1("BWM","X5",500000)
print(car1.__dict__)

#调用方法
total_cost=car1.total_cost(discount=0.2,rate=0.5)
print(total_cost)

car1.running()