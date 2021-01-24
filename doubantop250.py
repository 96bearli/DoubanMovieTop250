# -*- codeing = utf-8 -*-
# @Time : 2021/1/24 15:05
# @Author : 96bearli
# @File : doubantop250.py
# @Software : PyCharm
import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re


def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
    }
    try:
        req = urllib.request.Request(url=url, headers=headers)
    except Exception as error:
        print(error)
        print("构造请求出错")
        return
    try:
        html = urllib.request.urlopen(req, timeout=1)
    except Exception as error:
        print(error)
        print("urlopen出错")
        return
    return html.read().decode("utf-8")


def getData(html, count):
    global savePath
    soup = BeautifulSoup(html, "html.parser")
    items = soup.findAll(class_="item")

    findDicts = {"src": 'https://img.+?jpg',
                 "link": '<a href="(.*?)">',
                 "title": '<span class="title">(.*?)</span>',
                 "bd": re.compile('<div class="bd">\n<p class="">(.+?)</p>', re.S),
                 "rating": '<span class="rating_num" property="v:average">(.+?)</span>',
                 "judge": '<span>(\d+?人)评价</span>',
                 "inq": '<span class="inq"(.*?)</span>'
                 }
    try:
        for item in items:
            list = []
            list.append(str(count))
            print("第%d名电影正在处理..." % count)
            count += 1
            try:
                list.append(re.findall(findDicts['src'], str(item))[0])
            except:
                list.append("None")
            try:
                list.append(re.findall(findDicts['link'], str(item))[0])
            except:
                list.append("None")
            try:
                list.append(re.findall(findDicts['title'], str(item))[0])
            except:
                list.append("None")
            try:
                list.append(re.findall(findDicts['bd'], str(item))[0].replace("<br/>\n", " ").strip())
            except:
                list.append("None")
            try:
                list.append(re.findall(findDicts['rating'], str(item))[0])
            except:
                list.append("None")
            try:
                list.append(re.findall(findDicts['judge'], str(item))[0])
            except:
                list.append("None")
            try:
                list.append(re.findall(findDicts['inq'], str(item))[0])  # replace进行替换,strip()去掉字符串前后空格
            except:
                list.append("None")
            try:
                saveDataMd(list, savePath)
            except Exception as error:
                print(error)
                print("保存出错")
                continue
    except Exception as error:
        print(error)
        print("出错于数据获取过程")

    print("本页面数据保存成功")


# # 保存为markdown格式表格
# def saveDataMd(list, path):
#     if list[0] == '1':
#         with open(path, "a", encoding='utf-8') as f:
#             f.write("|排名|影名|评分|评论人数|影评|详细信息|\n| ---- | ---- | ---- | ---- | ---- | ---- |\n")
#     try:
#         with open(path, "a", encoding='utf-8') as f:
#             f.write("|%s|[%s](%s)|%s|%s|%s|%s|\n" % (list[0], list[3], list[2], list[5], list[6], list[7], list[4]))
#     except Exception as error:
#         print(error)


# 保存为markdown格式分介绍，带图片
def saveDataMd(list, path):
    if list[0] == '1':
        with open(path, "a", encoding='utf-8') as f:
            f.write("# 豆瓣Top250电影简介\n")
    with open(path, "a", encoding='utf-8') as f:
        f.write("## 第%s名:%s\n" % (list[0], list[3]))
        f.write("[![%s](%s)](%s)\n" % (list[3], list[1], list[2]))
        f.write(
            "|排名|影名|评分|评论人数|\n| ---- | ---- | ---- | ---- |\n|%s|%s|%s|%s|\n" % (list[0], list[3], list[5], list[6]))
        if list[7] != "None":
            f.write("### 影评\n%s\n" % list[7])
        f.write("### 详细信息\n%s\n" % list[4])


if __name__ == '__main__':
    baseUrl = "https://movie.douban.com/top250?start="
    savePath = "./doubantop250.md"
    for i in range(0, 250, 25):
        url = baseUrl + str(i)
        print("当前正在处理的url为:%s" % url)
        try:
            html = getHtml(url)
            # print(html)  # test
        except Exception as htmlError:
            print(htmlError)
            print("获取页面出错")
            continue
        try:
            getData(html, i + 1)
        except Exception as getDataError:
            print(getDataError)
            print("获取数据出错")
            continue
        print("本页完成")
        # try:
        #     saveDataMd(dataList, savePath)
        # except Exception as saveError:
        #     print(saveError)
        #     print("保存数据出错")
        #     continue
        # test
    print("全部完成")
