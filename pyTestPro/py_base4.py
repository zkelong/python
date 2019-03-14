#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 17:31
# @Author  : Aries
# @Site    : 
# @File    : py_base4.py
# @Software: PyCharm

"""
Python Number 用于存储数值，数据类型不允许改变，如果要改变 Number 数据值，将重新分配内存空间
可以用 delete 删除一些 Number 对象引用
Python 支持四种不同的数值类型：
    整型(Int)-通常被称为整型或整数，正或付整数，不带小数点
    长整型(long intergers)-无限大小的整数，整数最后是一个大小或小写的L
    浮点型(floating point real values)-浮点型由整数部分与小数部分组成，浮点也可以使用科学方法表示
    复数(complex number)-复数由实数部分和虚数部分构成，可以用 a + bj 或者 complex(a, b)表示，复数的实部 a 和虚部 b 都是浮点型
"""

"""
Python number 的类型转换
int(x [,base ]) -- int(x, base=10) -- base 表示x是何种进制的字符串：将 x 转换为整数(10进制)
long(x [, base ]) -- 转为长整型
float(x ) -- 浮点数
complext(real [, imag ]) -- 创建复数
str(x )
repr(str ) -- 表达式字符串
eval(str ) -- 计算在字符串中的有效 python 表达式，并返回一个对象
tuple(s ) -- 元组
list(s ) -- 列表
chr(x ) -- 整数转字符
unichr(x ) -- 整数转 unicode 字符
ord(x ) -- 字符转整数值
hex(x ) -- 整数转十六进制字符串
oct(x ) -- 整数转八进制字符串
"""


"""
Python 中数学运算常用的函数基本都在 math 模块，cmath 模块中
math 提供了许多对浮点数的属性运算函数
cmath 包含了一些用于复数运算的函数
"""

"""
Python 数学函数
abs(x)
ceil(x) 等到 x 的上入整数，math.ceil(4.1) = 5
cmp(x, y) x<y返回-1，x==y返回0，x>y返回1
exp(x) 返回e的x次幂(e 自然数)
fabs(x) 数的绝对值
floor(x) 返回数的下舍整数，math.floor(4.9) = 4
log(x) math.log(math.e)返回1.0, math.log(100, 10)返回2.0
log10(x) 返回以 10 为基数的 x 的对数，如 math.log10(100) 返回 2.0
max(x1, x2, ...) 最大值
min(x1, x2, ...) 最小值
modf(x) 返回 x 的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示
pow(x, y,) x**y运算后的值(** 表示幂运算)
round(x[,n]) 浮点数x的四舍五入值，n 代表舍入到小数点后的位数
sqrt(x) 返回数字 x 的平方根
"""

"""
Python 随机数函数
chioce(seq) 从序列的元素中随机挑选一个元素，比如 random.choice(range(10)),从0到9中随机挑选一个整数
randrange([start,]stop[,step]  从指定范围内，按指定基数递增的集合中获取一个随机数，基数 缺省值为1
random() 随机生成一个实数，它在[0, 1)范围内
seed([x])  改变随机数生成器的种子seed.如果不了解原理，不必特别去设定seed,Python会自动选择 seed
shuffle(lst) 将序列的所有元素随机排序
uniform(x, y) 随机生成一个实数，它在[x, y]范围内
"""

"""
Python 包含三角函数
acos(x) x 反余弦弧度值
asin(x) x 反正弦弧度值
atan(x) 反正切弧度值
atan2(y, x) 给定的x, y坐标的反正切值
cos(x) 弧度余弦值
hypot(x, y) 欧几里得范数 sqrt(x*x + y*y)
sin(x) 弧度正弦值
tan(x) 弧度正切值
degrees(x) 弧度转化为角度,degree(math.pi/2) = 90.0
radians(x) 角度转换为弧度
"""

"""
Python 数学常量
pi 数学常量pi,圆周率，一般以π来表示
e 数学常量，e 即自然常数（自然常数）
"""

def test():
    x = '23'
    y = int(x)
    print y
    z = int(x, 8)
    print z
    print 'py_base4'