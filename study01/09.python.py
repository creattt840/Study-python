
#match case 匹配
a=input("输入一个数字：")

match a:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case 4:
        print("4")
    case 5:
        print("5")
    case 6|7:
        print("6")
    case _:
        print("输入错误")