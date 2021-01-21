# -*- codeing = utf-8 -*-
# @Time : 2021/1/9 11:29
# @Author : 96bearli
# @File : dealWithData.py
# @Software : PyCharm
from bs4 import BeautifulSoup
import os


def dealOne(Num,savePath):
    print("正在处理第%s个文件"%Num)
    name = []  # 初始化电影名称,电影图片,豆瓣评分,评价数,电影概况,电影链接的列表
    imgUrl = []
    star = []
    evaluationNum = []
    Overview = []
    movieUrl = []
    try:
        with open('movie.douban_%s.txt'%Num,"r",encoding="utf-8") as f:
            bs = BeautifulSoup(f.read(),"html.parser")
            print(bs)
    except Exception as er:
        print(er)


def dealAll(workpath, savePath):
    try:
        os.chdir("%s"%workpath)  # 改变工作目录到cache
    except Exception as a:
        print(a)
        exit()
    for count in range(10):
        dealOne(count+1,savePath)
    pass


if __name__ == '__main__':
    workpath = "./cache"  # 工作目录
    savePath = "../save"  # 最终数据的保存路径
    dealAll(workpath, savePath)
