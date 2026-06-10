
#字典：使用键值对（key:value）来存储数据，每一个键都对应一个值，通过键可以快速找到对应的值
#特点：键值对存储，键不能重复，可以修改

#定义字典
dict1={"张三":555,"李四":444}

#定义空字典
dict2={}
dict3=dict()

#根据key获取value
socre=dict1["张三"]
print(socre)
dict1["张三"]=600 #修改
print(dict1["张三"])

