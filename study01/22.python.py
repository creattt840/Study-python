
#属性分为：
#   实例属性：实例属性属于每个具体对象的属性，每个对象都是独立的。（各个对象特有的数据）
#   类属性：类属性是属于类本身的属性，所有实例共享的。（所有对象共享的数据或配置）

class Car:
    #类属性  类名.属性 的方式操作
    wheel=4
    tax_rate=0.1
    def __init__(self,c_brand,c_name,c_price):
        #实例属性  实例对象.属性 的方式操作
        self.c_brand=c_brand
        self.c_name=c_name
        self.c_price=c_price

    def running(self):
        print(f"{self.c_brand} {self.c_name} 正在高速行驶")

c1=Car("BYD","汉",150000)
c2=Car("Tesla","Model Y",260000)