#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 14:43
# @Author  : Aries
# @Site    : 
# @File    : pyBase.py
# @Software: PyCharm

"""
单行注释用符号：井号
多行注释用三个单引号或者三个双引号
"""
"""
#!/usr/bin/python : 是告诉操作系统执行这个脚本的时候，调用 /usr/bin 下的 python 解释器；
#!/usr/bin/env python(推荐）: 这种用法是为了防止操作系统用户没有将 python 装在默认的 /usr/bin 路径里。当系统看到这一行的时候，首先会到 env 设置里查找 python 的安装路径，再调用对应路径下的解释器程序完成操作。
#!/usr/bin/python 相当于写死了python路径;
#!/usr/bin/env python 会去环境设置寻找 python 目录,推荐这种写法
"""
"""
python保留字符：
and, exec, not
assert, finally, or
break, for, pass
class, from, print
continue, global, raise
def, if, return
del, impor,t try
elif, in, while
else, is, with
except, lambd,a yie
"""
"""
代码块用缩进表示
缩进很严格，必须空格，或tab, 不能混用
缩进报错：IndentationError: unexpected indent
"""
"""
pyCharm 忽略警告信息：
1.鼠标移到提示的地方，按 alt + enter, 选择忽略(ignore)
2.Setting-Editor-Inspections-Python-PEP 8 coding style violation去掉勾选
"""
"""
中文乱码：
1.设置utf-8: File-Settings-Editor-File Encodings: IDE Encoding, Project Encoding 选择UTF-8
2.PyCharm 右下角就可以选编码格式(设置了 # _*_ coding: UTF-8 _*_ 就不能选了)
3.windows 命令提示符中文仍乱码，要使用 decode("utf-8") 转成 utf-8 编码，然后再使用 encode("gbk") 转换为 gbk 编码
4.中文字符串前加 u
"""

#一行代码边多行代码
def multi_line_code():
    item_one = 1
    item_two = 2
    item_three = 3
    total = item_one + \
            item_two + \
            item_three
    print total


#语句中包含[], {}, ()，不用使用多行连接符
def code_multi_line():
    days = ["Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday"]


"""
引号，双引号，三引号可表示字符串，引号结束的地方必须与开始的地方相同
三引号，特定地方用作注释，此处。
"""
def quotation_marks_use():
    word = 'word"\n'
    sentence = "sentence'\n"
    paragraph = u"""这是一个段落。'单引号'，"双引号"
    包含了多个语句"""
    print word, sentence, paragraph


"""
print 默认输出是换行的，如果要实现不换行，需要在末尾加上逗号(,)
"""
def print_use():
    x = 'x'
    y= 'y'
    s = '换行输出：'
    print s.decode("utf-8").encode("gbk")
    print x
    print y
    print '--------------------------'
    print u'不换行输出：'
    print x,
    print y
    print '--------------------------'
    print x, y