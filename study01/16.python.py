

#函数：组织好的，可重复使用的，用来实现特定功能的代码片段

#定义函数
#def 函数名字(参数列表):
#    函数体
#    ......
#    return 返回值
def out_line():
    print("-----------")

#调用函数
out_line()

#函数的说明文档：用三引号包裹的字符串，用于解释函数的功能，参数，返回值等信
#定义一个函数：根据半径，计算圆的周长，面积
#round:保留几位小数
def circle_area_len(r):
    """
    该函数用于根据圆的半径，计算圆的面积和圆的周长
    :param r: 圆的半径
    :return: 圆的面积，圆的周长
    """
    return round(3.14*r**2,1),round(2*3.14*r,1)

print(circle_area_len(5))

#global关键字：告诉Python解释器，在函数中要使用全局变量

#默认参数：在定义函数时，为参数提供默认值，调用函数时，可以不传递有默认值的参数
def reg_stu(name,age,gender,city='北京'):
    print(name,age,gender,city)

#调用函数
reg_stu("张三",18,"男")

#不定长参数(位置参数 *args-->元组)
def calc_data(*args):
    min_data=min(args)
    max_data=max(args)
    return min_data,max_data

data=calc_data(1,2,3,4)
print(data)

#不定参数-关键字传递(**kwargs)
#注意：参数是以“键=值”形式传递关键字参数，这些“键=值”参数都会被kwargs接收，并合并封装为一个字典类型
def calc_data(*args,**kwargs):
    """
    :param args: 不定长位置参数
    :param kwargs: 不定长关键字参数
    :return: 最小值，最大值，平均值
    """
    min_data=min(args)
    max_data=max(args)
    if kwargs.get('round'):
        avg_data=round((min_data+max_data)/2,kwargs.get('round'))
    return min_data,max_data,avg_data

data=calc_data(1,2,3,4,round=2,count=0)
print(data)


#匿名函数：没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写
#定义匿名函数
#lambda 参数列表：函数体
line=lambda : print('hello world')
add=lambda a,b:a+b
line()
print(add(5,6))
