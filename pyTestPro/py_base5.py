#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 17:29
# @Author  : Aries
# @Site    : 
# @File    : py_base5.py
# @Software: PyCharm

def string_use():
    var1 = "Hello World"
    print "var1[0]: ", var1[0]
    print "var1[0:5]", var1[0:5]

# 字符串更新
def string_update():
    v = 'Hello World!'
    print "update: -", v[:6] + 'Runoob!'

"""
Python 转义字符
\(行尾时)   - 续行符
\ \         - 反斜杠符号
\ '         - 单引号
\ "         - 双引号
\ a         - 响铃
\ b         - 退格(BackSpace)
\ e         - 转义
\ 000       - 空
\ n         - 换行
\ v         - 纵向制表符
\ t         - 横向制表符
\ r         - 回车
\ f         - 还页
\ oyy       - 八进制，yy代表的字符，例如：\o12 代表换行
\ xyy        - 十六进制，yy代表字符，例如：\x0a 代表换行
\ other     - 其它的字符以普通格式输出
\和后边的是没有空格的，如果没有空格，报错
"""

'''
Python 字符串运算符
+   - 字符串连接
*   - 重复输出字符串
[]  - 通过索引获取字符串中字符
[:] - 截取字符串中的一部分
in  - 成员运算符 - 如果字符串中包含给定的字符 返回 True
not in - 成员运算符 - 如果字符串中不包含给定的字符串 返回 True
r/R  - 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊后不能打印的字符。原始字符除在字符串的第一个引号前加上字母"r"(可以大小写)以外，与普通字符串有着几乎完全相同的语法。
% 格式字符串
'''
def string_operator():
    s1 = "string1"
    s2 = "string2"
    print s1 + s2
    print s1 * 2
    print s1[1]
    print s1[0:4]
    print s1[1:]
    print s1[:3]
    print 's' in s1
    print 'x' not in s1
    print r'\n'
    print '%s + xxx' % s1
    print '%s + xx + %d cc' % (s1, 10)

"""
Python 字符串格式化符号
%c 格式化字符及其 ASCII 码
%s 格式化字符串
%d 格式化整数
%u 格式化无符号整型
%o 格式化无符号八进制数
%x 格式化无符号十六进制数
%X 格式化无符号十六进制数(大写)
%f 格式化浮点数字，可以指定小数点后的精度
%e 用科学计数法格式化浮点数
%E 作用同 %e，用科学计数法格式化浮点数
%g %f 和 %e的简写
%G %f 和 %E 的简写
%p 用十六进制数格式化变量的地址
"""
"""
格式化操作符辅助指令
* 定义宽度或者小数点进度
- 用做左对齐
+ 在正数前面显示加号(+)
<sp> 正数前面显示空格
# 在八进制数前面显示零('0')，在十六进制前面显示 '0x '或者 '0X'(取决于用的是'x'还是'X')
0 显示的数字前面填充 '0' 而不是默认的空格
% '%%'输出一个单一 '%'
(var) 映射变量(字典参数)
m.n m是显示的最小总宽度，n 是小数点后的位数(如果可用的话)
"""
"""
Python 三引号(triple quotes)
python 中三引号可以将复杂的字符串进行复制：
python 三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。
三引号的语法是一对连续的单引号或者双引号(通常都是成对的用)
三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式所谓的 WYSIWYG (所见即所得)格式。
"""
"""
Unicode 字符串
Python 中定义一个 Unicode 字符串和定义一个普通字符串一样简单
u"Hello"
"""


def test():
    # string_use()
    # string_update()
    string_operator()