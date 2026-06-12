
#多态：指同一个方法，具有不同的形态，行为，表现
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

#参数类型为父类，支持传入任意子类
def handle_charge(car:Car):
    car.start() #同一个方法，根据传入对象不同，触发不同行为

if __name__ == '__main__':
    car1 = ElectricCar('迈巴赫', 's-480', '黑色', '我')
    handle_charge(car1)
    car2=Car('迈巴赫', 's-480', '黑色', '我')
    handle_charge(car2)

