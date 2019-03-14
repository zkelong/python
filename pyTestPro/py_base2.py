#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 15:59
# @Author  : Aries
# @Site    : 
# @File    : pyBase2.py
# @Software: PyCharm

"""
Python 变量赋值不需要类型声明。
每个变量在内存中创建，都包含变量的标识，名称和数据这些信息。
每个变量在使用前都必须赋值，赋值后该变量才会被创建。
"""
"""
Python 有五个标准的数据类型
Numbers(数字)
String(字符串)
List(列表)
Tuple(元组)
Dictionary(字典)
"""
"""
数字类型：
int(有符号整型)
long(长整型[也可以代表八进制和十六进制])
float(浮点型)
complex(复数)
"""


def variable_use():
    #变量赋值
    counter = 100 # 赋值整型变量
    miles = 1000.0 # 浮点型
    name = "John" # 字符串
    print counter
    print miles
    print name
    a = b = c = 1
    print a, b, c
    a, b, c = 1, 2, "John"
    print a, b, c


def string_use():
    #字符串列表有2种取值顺序：
    #从左到右索引默认0开始的，最大范围是字符串长度少1
    #从右到左索引默认-1开始的，最大范围是字符串开头
    s = "ilovepython"
    print s[1:5]
    print s[0:-6]
    print s[5:11]


def list_use():
    #列表：可以完成大多数集合类的数据结构实现。支持，字符，数字，字符串甚至可以包含列表(即嵌套)
    #截取列表同字符串[头下标，尾小标]
    list = ["runoob", 7876, 2.23, 'john', 70.2]
    tinylist = [123, 'johnn']
    print list
    print tinylist[1]
    print tinylist * 2 #输出列表两次


def tuple_use():
    #元组，类似于List(列表)
    #用 () 标识，内部元素逗号隔开。不能二次赋值，相当于只读列表
    tuple = ('runoob', 786, 2.23, 'john', 70.2)
    tinytuple = (123, 'john')
    print tuple
    print tinytuple[0:]


def dict_use():
    #字典(dictionary)是出列表外最最灵活的内置数据结构类型。
    #列表是有序的对象组合，字典是无序的对象组合
    #字典中元素通过键来存取，而不类似列表的通过偏移来存取。
    #字典用"{}"。字典由索引(key)和它对应的值 value 组成
    dict = {}
    dict["one"] = "This is one"
    dict[2] = "This is two"
    tinydict = {"name": "john", 'code': 123, 'dept':'scale'}
    print dict["one"]
    print dict[2]
    print tinydict
    print tinydict.keys()
    print tinydict.values()


"""
有时我们需要对数据内置的类型进行转换，数据类型的转换，只需要将数据类型作为函数名即可。
Python 有办法将任意值转为字符串：将它传入repr() 或str() 函数。
函数str() 用于将值转化为适于人阅读的形式，而repr() 转化为供解释器读取的形式
尽管str(),repr()和``运算在特性和功能方面都非常相似，事实上repr()和``做的是完全一样的事情，它们返回的是一个对象的“官方”字符串表示，也就是说绝大多数情况下可以通过求值运算（使用内建函数eval()）重新得到该对象，但str()则有所不同。str()致力于生成一个对象的可读性好的字符串表示，它的返回结果通常无法用于eval()求值，但很适合用于print语句输出。需要再次提醒的是，并不是所有repr()返回的字符串都能够用 eval()内建函数得到原来的对象。
也就是说 repr() 输出对 Python比较友好，而str()的输出对用户比较友好。
"""
def type_exchange():
    a = 100.01
    b = int(a) #转为整型
    print a, b
    c = long(a) #转为长整型
    print c
    d = float(b)  #浮点数
    print d
    # 复数
    e = str(d) + "x" #字符串
    print e
    obj = ("a", "b", "c") #字符串-表达式字符串
    a = repr(obj)
    print a
    o = eval(a)
    print a
    if a == o:
        print o
    # ...


def opereator_test():
    #算术运算符
    a, b = 10, 20
    print a + b
    print a - b
    print a * b
    print a / b
    print a % b
    print a ** b
    print a // b


def comparision_character():
    #逻辑运算符
    a, b = 10, 20
    print a == b
    print a != b
    print a <> b
    print a > b
    print a < b
    print a >= b
    print a <= b


def assignment_operator():
    #赋值运算符
    a, b = 10, 20
    c = a + b
    print c
    a += b
    print a
    a -= b
    print a
    a *= b
    print a
    a /= b
    print a
    a %= b
    print a
    a **= b
    print a
    a //= b
    print a


def bit_operator():
    #位运算符
    a, b = 0b111100, 0b001101
    print a, b
    print a & b
    print a | b
    print a ^ b
    print ~a
    print a << 2
    print a >> 2

def logical_operator():
    #逻辑运算符
    a, b = True, False
    print a, b
    print a and b
    print a or b
    print not b


def member_operator():
    #成员运算符
    a, b = 10, 20
    list = [1, 2, 10, 3, 8]
    if(a in list):
        print "a in list"
    else:
        print "a not in list"
    if(b not in list):
        print str(b) + " in " + str(list)
    else:
        print "b in list"

def type_operator():
    #身份运算符
    a, b = 10, 10
    if( a is b ):
        print "a, b have same identifier"
    else:
        print "a, b have different identifier"
    b = 20
    if(a is not b):
        print "a, b have different identifier"
    else:
        print "a, b have same different identifier"

"""
运算符优先级：
** 指数(最高)
~ + - 按位翻转，一元加号和减号
* / % // 乘，除，取模和取整除
+ - 加减法
>> << 右移，左移运算符
& 位'and'
^ | 位运算符
<= < > >= 比价运算符
<> == != 等于运算符
= %= /= //= -= += *= **= 赋值运算符
is is not 身份运算符
in not in 成员运算符
not or and 逻辑运算符
"""


def test():
    # variable_use()
    # string_use()
    # list_use()
    # tuple_use()
    # dict_use()
    # type_exchange()
    # opereator_test()
    # comparision_character()
    # assignment_operator()
    # bit_operator()
    # logical_operator()
    # member_operator()
    type_operator()