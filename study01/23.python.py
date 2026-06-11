from typing import final

#捕获异常：按我们自己的处理方式，处理完异常，程序继续执行。
#try:
#   可能出现异常的业务代码1
#   可能出现异常的业务带吗2
#   ...
#except 异常类型 as 变量名:
#   出现异常时的预案
#finally:
#   不管是否出现异常，都会执行的代码

try:
    print("=========")
except NameError as e:
    print("程序运行错误，错误信息:",e)
finally:
    print("释放资源")