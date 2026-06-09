
#match case 匹配
a=input("输入一个数字：")

match a:
    case "1":
        print("1")
    case "2":
        print("2")
    case 3:
        print("3")
    case 4:
        print("4")
    case 5:
        print("5")
    case 6|7:
        print("6")
    case _: #匹配其他所有情况
        print("输入错误")


# while循环 else:条件不成立时执行
temp=1
while temp>0:
    print(temp)
    temp-=temp
else:
    print("循环正常结束，执行完毕")

print(temp)


#for循环  else在遍历结束后执行
# i 表示遍历出来的元素，msg 表示需要遍历的数据
msg="Hello-Python"
#遍历字符串，并处理
for i in msg:
    #默认遍历一个以换行结束，如果不想换行可以在后面加end=""
    print(f"元素{i}")
else:
    print("遍历结束")

#range语句 生成指定规则的数字序列
#range(end) 获取一个从0开始，到end结束的数字序列(不含end本身)
print(list(range(10)))

#range(start,end) 获取一个从start开始end结束的数字序列(不含end本身)
print(list(range(2,10)))

#range(start,end,step) 获取一个从start开始，到end结束的数字序列，step步长(不含end本身)
print(list(range(2,10,2)))
