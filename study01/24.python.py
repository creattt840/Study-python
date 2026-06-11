
#打开文件 第二个参数为"r"或"w"分别表示读或写，最后一个参数表示为编码
f=open("python.txt","r",encoding="utf-8")

#读取文件
content=f.read()
print(content)

#关闭文件
f.close()

q=open("python.txt","w",encoding="utf-8")

#写入文件
q.write("hello")

#关闭文件
q.close()

#with语句（上下文管理器） 核心作用就是确保资源能被正确获取和释放（即使发送异常，也会被正常释放）
with open("python.txt","w",encoding="utf-8") as f:
    f.write("hello")

