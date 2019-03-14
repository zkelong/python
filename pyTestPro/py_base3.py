#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 17:32
# @Author  : Aries
# @Site    : 
# @File    : py_base3.py
# @Software: PyCharm

"""
pyton 对象对应的 True 和 False
1.数字 0 为 False, 其他为 True
2.字符串 空串("") 为 False, 其他为 True
3.list([]) 为 False, 其他为 True
4.tuple(()) 为 False, 其他为 True
5.dict({}) 为 False, 其他为 True
"""

def use_if():
    tag = 10
    if tag > 0:
        print "tag > 0"
    else:
        print "tag <= 0"
    if tag >= 1 and tag < 2:
        print "tag >= 1 and tag < 2"
    elif tag == 10:
        print "tag == 10"
    tw = "hello"
    if tw == "hello": print("hello")
    else: print("Ha-Ha")


#python 不支持switch语句


# while, break, continue
def use_loop():
    numbers = [12, 32, 5, 23, 112, 5]
    even = []
    odd = []
    while len(numbers) > 0:
        number = numbers.pop()
        if(number % 2 == 0):
            even.append(number)
        else:
            odd.append(number)
    print even
    print odd
    i = 1
    while i < 10:
        i += 1
        if i % 2 > 0:
            continue
        print i
    print "****************"
    i = 1
    while 1:
        print i
        i += 1
        if i > 10:
            break

# while 可以和 else 一起用
def loop_with_else():
    count = 0
    while count < 5:
        print count, "is less than 5"
        count = count + 1
    else:
        print count, " is not less than 5"

# for..in
def use_for():
    for letter in 'Python':
        print letter
    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:
        print fruit
    # for index....
    for index in range(len(fruits)):
        print fruits[index]
    # fro ... else
    for num in range(10, 20):
        for i in range(2, num):
            if num % i == 0:
                j = num / i
                print u"%d 等于 %d * %d" % (num, i, j)
                break
        else:
            print num, "是一个质数"


# 循环嵌套
def loop_inner():
    i = 2
    while(i < 100):
        j = 2
        while(j <= (i/j)):
            if not(i % j): break
            j = j + 1
        if(j > i / j): print i, u"是素数"
        i = i + 1


def use_break():
    for letter in 'Python':
        if letter == 'h':
            break
        print u"当前", letter


def use_continue():
    for letter in 'Python':
        if letter == 'y':
            continue
        print u"当前", letter

# Python pass 是空语句，为了保持程序结构的完整性
# pass 不做任何事情，一般只用做占位语句
def use_pass():
    for letter in 'Python':
        if letter == 'h':
            pass
            print u'这是pass块'
        print u'当前字母：', letter

def test():
    # use_if()
    # use_loop()
    # loop_with_else()
    # use_for()
    # loop_inner()
    # use_break()
    # use_continue()
    use_pass()