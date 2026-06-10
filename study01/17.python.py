
#类型注解：用于标识变量，函数参数和返回值的数据类型，从而使代码更清晰，更安全，更易于维护
#定义变量
a:int =95
score:float=55.1
hobby:str="躺"
flag:bool=True
pic:None=None

names:list[str]=["a","b","c"]
phones:set[str]={"1231312322","113215553333"}
options:dict[str,int]={"count":0,"total":0}
goods:tuple[str,int,int]=("手机",5444,1)

#类型推断：python解释器自动推断出变量，表达式或函数返回值的数据类型的能力

#函数类型注解
#参数里面标识变量类型，在括号后面加->返回参数。，可以指定返回参数
def circle_area(r:float)->tuple[float,float]:
    return round(3.14*r**2)

al=circle_area(10)
print(al)