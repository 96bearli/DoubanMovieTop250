# -*- codeing = utf-8 -*-
# @Time : 2021/1/14 11:34
# @Author : 96bearli
# @File : deal_test.py
# @Software : PyCharm
from bs4 import BeautifulSoup
import re


def dealWithData(html, count):  # 数据处理
    bs = BeautifulSoup(html, features="html.parser")
    for li in bs.select("ol>li"):
        print(re.search('泰坦.*',str(li)))
    # print(bs.select("ol>li")[-1])
    print("准备储存数据")


# //*[@id="content"]/div/div[1]/ol/li[1]
if __name__ == '__main__':
    with open("movie.douban_1.txt", "r", encoding='utf-8') as f:
        html = f.read()
        count = 0
    dealWithData(html, count)
