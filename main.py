# -*- codeing = utf-8 -*-
# @Time : 2021/1/7 14:56
# @Author : 96bearli
# @File : main.py
# @Software : PyCharm

import urllib.request, urllib.error
import os
import time
from bs4 import BeautifulSoup
import re
import random


def randomSleep():
    waitTime = random.uniform(0.5, 1)
    print("由于反爬机制，随机等待%.2f秒后继续" % waitTime)
    time.sleep(waitTime)


def log(Text):
    print(nowTime(), Text)
    try:
        with open("./cache/errorLog.txt", "a", encoding="utf-8") as file:
            Text = nowTime() + Text
            file.write(Text + "\n")
    except Exception as errorText:
        print(nowTime(), "log函数出错!", errorText)


def nowTime():
    return time.strftime("%Y-%m-%d\t%H:%M:%S:\t", time.localtime())


# 获取数据并解析
def getHtml(url, i):  # 获取一页
    global retrylist
    print(nowTime(), "当前处理url为%s" % url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
    }
    try:
        req = urllib.request.Request(url=url, headers=headers)
    except Exception as reqError:
        # reqError = "reqError:urlline" % str(i+1) + reqError
        log(str(i + 1))
        log(url)
        log(reqError)
        return "error"
    print(nowTime() + "...." * 4)
    try:
        response = urllib.request.urlopen(req, timeout=1)
    except Exception as responseError:
        # responseerror = "responseError:urlline" + str(i+1) + responseError
        retrylist.append(i)
        log(str(i + 1))
        log(url)
        log(str(responseError))
        return "error"
    try:
        return response.read().decode('utf-8')
    except Exception as errorText:
        log(str(i + 1))
        log(errorText)
        return response.read()


def dealWithData(html, count):  # 数据处理
    bs = BeautifulSoup(html, "html_parser")
    for
    print(list)
    log("准备储存数据")


def getData(urlBase, limitNum, stepValue):  #
    urlParm = 0  # ?start=urlParm
    log("开始循环获取并处理信息")
    while urlParm < limitNum:
        url = urlBase + str(urlParm)
        try:
            html = getHtml(url)
        except Exception as getError:
            log(str(getError))
            log("页面获取失败，重试中。。。。")
            try:
                html = getHtml(url)
            except Exception as getError2:
                log(str(getError2))
                log("页面获取失败，跳过")
                urlParm += stepValue
                continue
        try:
            dealWithData(html, urlParm)
        except Exception as dealError:
            log(str(dealError))
            log("数据处理出错，重试中。。。。")
            try:
                dealWithData(html, urlParm)
            except Exception as dealError2:
                log(str(dealError2))
                log("数据处理出错，跳过")
                urlParm += stepValue
                continue
        urlParm += stepValue


def saveDate(datalist, savepath):
    count = 1
    for data in datalist:
        try:
            with open("%s\\movie.douban_%s.txt" % (savepath, count), "w+", encoding='utf-8') as f:
                f.write(data)
        except Exception as result:
            with open("%s\\movie.douban_%s.txt" % (savepath, count), "w+", encoding='utf-8') as f:
                f.write(result)
        count += 1


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # baseurl = "https://bear962464.cn/"
    savepath = ".\\cache"
    try:
        os.mkdir("%s" % savepath)
    except Exception as result:
        print("cache文件夹已存在，跳过")
    getData(baseurl, 250, 25)
    print("结束\n请查看cache目录")


if __name__ == "__main__":  # 意思就是当程序执行时，为了更清楚的看主流程
    main()  # 调用函数 就是个程序入口
