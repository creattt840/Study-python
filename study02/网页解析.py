#lxml:是一个高性能的HTML/XML文档的解析库，支持基于Xpath语法来解析和获取网页数据
#Xpath:是一种用于在HTML/XMl文档中导航或定位元素的查询语言，
# 让你能够准确的定位文档中的特定元素，属性或文本


from lxml import html

#读取html文件
with open("python.txt","r",encoding="utf-8") as f:
    html_text=f.read()

    #解析html的文本，将其转换为一个文档对象
    document=html.fromstring(html_text)

    #解析表头 - Xpath语法
    th_list=document.xpath("//table/thead/tr/th/text()")

    #获取第一行数据
    #td_list=document.xpath("//table/tbody/tr[1]/th/text()")
    #print(td_list)

    #获取所有行数据
    tr_list=document.xpath("//table/tbody/tr")
    for td in tr_list:
        td_list=td.xpath("./td/text()")
        print(td_list)