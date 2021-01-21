# -*- codeing = utf-8 -*-
# @Time : 2021/1/7 14:39
# @Author : 96bearli
# @File : spider.py.py
# @Software : PyCharm
# coding = utf-8

import re  # 网页解析获取数据
import bs4  # 正则表达式,文字匹配
import urllib.request, urllib.error  # 指定url获取网页数据
import xlwt  # 进行excel操作
import sqlite3  # sqlite数据库操作

from test1 import t1  # 引入模块，其中test1表示文件夹(package)，文件t1.py

print(t1.add(23, 22))
'''
45 #成功引入t1并使用其中add函数
'''


def main():
    print("sad")


if __name__ == "__main__":  # 意思就是当程序执行时，为了更清楚的看主流程
    main()  # 调用函数 就是个程序入口
