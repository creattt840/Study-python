
#csv:是一种简单，通用的文本文件格式，用于存储表格数据，可以直接使用Excel打开
import csv

#写
with open("csv_data/01.csv","w",encoding="utf-8",newline="") as f:
    writer=csv.DictWriter(f,fieldnames=["姓名","年龄","性别","爱好"])
    writer.writeheader() #写入表头
    writer.writerow({"姓名":"小王","年龄":18,"性别":"男","爱好":"Java"}) #写入数据

#读
with open("csv_data/01.csv","r",encoding="utf-8") as f:
    reader=csv.DictReader(f)
    for row in reader:
        print(row)
    