
#注意事项：Python中是没有真正的私有机制的，__开头为私有是一种约定

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

        def get_owner(self):
            return self.__owner[0:1] + "**"
