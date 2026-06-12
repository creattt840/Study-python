
#正则表达式：re 是一种由特定语法规范组成的文本模式，用来描述，匹配字符串种符合规则的字符序列
import re

s="我的手机号：1535044453448，另一个手机号175310352441"
s1="15350044550"

#r：让字符串中的符号表示他们原本的含义

#match - 从头开始匹配，只匹配第一个匹配项
result=re.match(r"1[3-9]\d{9}",s1) #match - 从字符串的开头开始匹配（返回Match对象）
print(result.group()) #group()获取到匹配的结果
print(result.span()) #span()获取匹配项的索引
print(result.start()) #start()获取匹配项的开始索引
print(result.end()) #end()获取匹配项的结束索引

result=re.search(r"1[3-9]\d{9}",s) #search - 从任意位置开始，搜索第一个匹配项（返回Match对象）
print(result.group())

result=re.findall(r"1[3-9]\d{9}",s) #findall - 从任意位置开始，搜索所有匹配项（返回list）
print(result)