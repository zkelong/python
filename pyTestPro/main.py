#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 14:42
# @Author  : Aries
# @Site    : 
# @File    : main.py
# @Software: PyCharm

"""
命令行参数：
python 可以使用 -h 参数来查看各参数帮助信息
在使用脚本形式执行 Python 时，可以接收命令行输入的参数
"""


import py_base
import py_base2
import py_base3
import py_base4
import py_base5
import sys  #获取命令行参数


def py_base_test():
    py_base.multi_line_code()
    py_base.code_multi_line()
    py_base.quotation_marks_use()
    py_base.print_use()


def py_base2_test():
    py_base2.test()

def py_base3_test():
    py_base3.test()

def py_base4_test():
    py_base4.test()

def py_base5_test():
    py_base5.test()

if __name__ == "__main__":
    print sys.argv
    # py_base_test()
    # py_base2_test()
    # py_base3_test()
    # py_base4_test()
    py_base5_test()