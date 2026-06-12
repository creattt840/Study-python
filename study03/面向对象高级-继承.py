
#继承：描述的是两个类之间的关系，子类继承父类，就可以获取到父类的属性和方法（非私有）

class Car:
    def __init__(self, brand,model,color,owner):
        self.brand = brand
        self.model = model
        self.color = color
        self.__owner = owner #表示私有 __ 只能通过内部方法获取

    def start(self):
        print(f"{self.brand} {self.model}汽车正在启动")

    def __control_fuel(self):  #私有方法 __
        print(f"{self.brand} {self.model} 正在控制油门")

    def charge(self):
        print(f"{self.brand} {self.model} 正在启动")

    def get_owner(self):
        return self.__owner[0:1] + "**"

#燃油车
class FuelCar(Car):
    pass

#电车
class ElectricCar(Car):
    #方法重写
    def start(self):
        #调用父类中的方法 父类名.方法名(self)/super().方法名()
        super().charge()
        print(f'{self.brand} {self.model} 电车正在启动')

car1=ElectricCar('迈巴赫','s-480','黑色','我')
car1.start()

#多继承：一个子类同时继承多个父类
#当一个类继承了多个父类时，默认会优先使用第一个父类中的同名属性或方法，可以使用 类名.__mro__属性 或
# 类名.mro()方法查看调用顺序
class HuaWeiSmartCar(Car,ElectricCar):
    pass

