# #!/usr/bin/env python
# # coding: utf-8
#
# # # 10章  模块（模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。）
#
#
# # 文件名：using_sys.py
# import sys  # 引入已经有的系统模块
#
# print("打印命令行参数如下：")
# for i in sys.argv:
#     print(i)
#
# print("\n\nPython路径为", sys.path, '\n')
#
# # 导入自己创建的模块
# import support
#
# # 现在可以调用模块里包含的函数了
# support.print_func("Li Jinagjie")
#
# # 搜索路径被存储在sys模块中的path变量
# print(sys.path)
# # 输出为一个列表。其中第一项是代表当前目录（若是从一个脚本中打印出来的话，可以更清楚地看出是哪个目录），亦即我们执行python解释器的目录（对于脚本的话就是运行的脚本所在的目录）。

#  利用自建的Fibo模块
# import Fibo
# print(Fibo.fib1(1000))
# print(Fibo.fib2(1000))

# from   import 语句
# from Fibo import fib1, fib2
# print(fib1(1000))
# print(fib2(1000))

# from  modename import *  :引入modename中的全部方法和属性
# from Fibo import *
# print(fib1(100))
# print(fib2(100))

# import useing_modename

# dir()函数：查找模块中的全部方法,以列表方式输出
import Fibo,sys
print(dir(Fibo))
a=5
print(dir())  # 新变量的方法和属性

#  python中好多标准库是很重要的
import sys   #变量 sys.ps1 和 sys.ps2 定义了主提示符和副提示符所对应的字符串
print(sys.ps1)
print(sys.ps2)
# print(__init__)   这个是包里面的初始化文件
#  print(__all__)    这个是变量列表

                                                                                                                                                                                                                                                                                    1
                                                                                                                                                                                                                                                                                    .