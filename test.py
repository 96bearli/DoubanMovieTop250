# -*- codeing = utf-8 -*-
# @Time : 2021/1/9 12:07
# @Author : 96bearli
# @File : test.py
# @Software : PyCharm
from bs4 import BeautifulSoup
import os
import re

with open('./cache/movie.douban_1.txt', "rb") as f:
    bs = BeautifulSoup(f.read(), features="html.parser")
    # print(bs.select('title')[0].string)
    # infoList=bs.find_all(class="item")
    # print(infoList.get_text())
    # infoList = bs.select("[class='title']" ) # 缺少霸王别姬的英文名
    # infoList = bs.select("div>div>a")
    # infoList = []
    # 电影名称, 电影图片, 豆瓣评分, 评价数, 电影概况, 电影链接的列表
    '''infoList = bs.select(".hd")  # 通过hd的class获取所有标题'''

    '''infoList = bs.select("li>div>div>div>p") # 0-49 偶数是简介，单数是一句话简述'''

    # infoList = bs.select("ol>li>div>div>div>div>span")

    '''infoList = bs.select('.rating_num')  # 评分'''
    # def name_is_exists(tag):
    #     return tag.has_attr("人评论")
    # infoList=bs.find_allr(name_is_exists)
    infoList = bs.find_all(text=re.compile(r'<span>(\d*)人评价</span>'))

    for info in infoList:
        print(info.get_text(), '%d' % infoList.index(info))
# /html/body/div[3]/div[1]/div/div[1]/ol/li[5]/div/div[2]/div[2]/div/span[2]
# //*[@id="content"]/div/div[1]/ol/li[5]/div/div[2]/div[2]/div/span[2]