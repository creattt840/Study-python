
#JSON是软件开发中最常用的数据交换格式，为了简化JSON数据的处理，在Python标准库中就提供了处理JSON
#数据的核心模块json
import json

obj={
    "name":"张三",
    "age":18,
    "gender":"male"
}

with open("python.txt","w",encoding="utf-8") as f:
    #indent:缩进（格式化）
    json.dump(obj,f,ensure_ascii=False,indent=4) #序列化

with open("python.txt","r",encoding="utf-8") as f:
    obj=json.load(f)
    print(obj) #反序列化

