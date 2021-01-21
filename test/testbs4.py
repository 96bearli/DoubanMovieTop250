# -*- codeing = utf-8 -*-
# @Time : 2021/1/8 21:15
# @Author : 96bearli
# @File : bs4.py
# @Software : PyCharm

'''
BeautifulSoup4 将复杂HTML文档转换成一个复杂的树形结构
每 个节点都是Python对象
所有对象可以归纳为4种：
tag，NavigableString，BeautifulSoup，Comment。
'''

# 使用目录下baidu.html演示

'''基础：
# 1.标签及内容 
# print(bs.title)
# < title > 百度一下，你就知道 < / title >

# 2.标签的内容 .string
print(bs.title.string)
# 百度一下，你就知道

# 3.打印属性 .attrs
print(bs.a.attrs)
# {'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}

# 4.comment 特殊的NavigableString，不包含注释符号
print(bs.a.string)
print(type(bs.a.string))
# <class 'bs4.element.Comment'>
'''

"""
from bs4 import BeautifulSoup

try:
    with open("./baidu.html", "rb") as file:  # 2进制读取
        html = file.read()
        bs = BeautifulSoup(html, "html.parser")  # (解析对象，解析器)
        # # bs是一个树形结构 根枝叶
        # print(bs.title)
        # # < title > 百度一下，你就知道 < / title >
        # print(bs.a)
        # # < a class ="mnav" href="http://news.baidu.com" name="tj_trnews" > < !--新闻--> < / a >
        # print(bs.head)
        # # html的line3-line9
        # print(bs.body)
        # # 这个形式是输出tag，找到第一个出现的标签以及标签内所有内容
        # print(type(bs.body))
        # # 输出<class 'bs4.element.Tag'>

        # print(bs.title.string)
        # # 百度一下，你就知道
        # print(bs.a.string)
        # # 新闻
        # print(type(bs.a.string))
        # # <class 'bs4.element.Comment'>

        # print(bs.a.attrs)
        # # {'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'}
        # print(bs.title.attrs)

        # print(bs.head.link.attrs)
        # # {'href': 'https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css', 'rel': ['stylesheet'],'type': 'text/css'}

        print(bs.a.string)
        print(type(bs.a.string))
        print(type(bs.title.string))
        # 新闻
        # <class 'bs4.element.Comment'>
        # <class 'bs4.element.NavigableString'>
        print(bs.a)
        print(bs.a.next_sibling.next_sibling)  # 第二个<a
        # < a class ="mnav" href="http://news.baidu.com" name="tj_trnews" > < !--新闻--> < / a >
        # < a class ="mnav" href="http://news.baidu.com" name="tj_trnews" > 新闻 < / a >

except Exception as error:
    print(error)
"""

'''应用-有针对性的扒东西 https://blog.csdn.net/xiaoyu_wu/article/details/102295184
# 文档的遍历
print(bs.head.contents[1]) # .contents得到本标签的列表,既然是列表就可以直接读取了
#<meta content="text/html;charset=utf-8" http-equiv="content-type"/>
 
# *文档的搜索
# 搜索
# 1.find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
a_list = bs.find_all("a")  # 查找所有名字叫”meta“的节点放到一个列表里
for a in a_list:
print(a)

# 2.正则表达式搜索
# 使用search()方法来匹配内容
# 需要引入re模块
import re
a_list = bs.find_all(re.compile("a"))  # 含有"a"的标签的所有内容比如<head>输出到</head>
     
# 3.方法：传入一个函数(方法)，根据函数的方法来引入,很强大
    def name_is_exists(tag):
        return tag.has_attr("class") # 键
    a_list = bs.find_all(name_is_exists)
    for a in a_list:
        print(a)   
        
# 4.kwargs 参数
# a_list = bs.find_all(id="head") # id name class_
# a_list = bs.find_all(class_=True)
a_list = bs.find_all(href = 'http://news.baidu.com')
for a in a_list:
    print(a.string)
    

'''

from bs4 import BeautifulSoup

try:
    with open("./baidu.html", "rb") as file:  # 2进制读取
        bs = BeautifulSoup(file.read(), "html.parser")
        # print(bs)
        # print(bs.head.contents)  # 得到本标签的列表
        # # ['\n', <meta content="text/html;charset=utf-8" http-equiv="content-type"/>, '\n', <meta content="IE=Edge" http-equiv="X-UA-Compatible"/>, '\n', <meta content="always" name="referrer"/>, '\n', <link href="https://ss1.bdstatic.com/5eN1bjq8AAUYm2zgoY3K/r/www/cache/bdorz/baidu.min.css" rel="stylesheet" type="text/css"/>, '\n', <title>百度一下，你就知道 </title>, '\n']
        # print(bs.head.contents[1])  # 既然是列表就可以直接读取了
        # # <meta content="text/html;charset=utf-8" http-equiv="content-type"/>
        # print(bs.body.contents)

        # 搜索 https://www.cnblogs.com/changwoo/p/9932085.html
        # # 1.find_all()
        # a_list = bs.find_all("a")  # 查找所有名字叫”meta“的节点放到一个列表里
        # for a in a_list:
        #     print(a)

        # 2.正则表达式搜索
        # 使用search()方法来匹配内容
        # 需要引入re模块
        # import re
        # a_list = bs.find_all(re.compile("a"))  # 含有"a"的标签的所有内容比如<head>输出到</head>
        # for a in a_list:
        #     print(a)

        # 3.方法：传入一个函数(方法)，根据函数的方法来引入,很强大
        # def name_is_exists(tag):
        #     return tag.has_attr("class") # 键
        # a_list = bs.find_all(name_is_exists)
        # for a in a_list:
        #     print(a)

        # 4.kwargs 参数
        # a_list = bs.find_all(id="head") # id name class_
        # a_list = bs.find_all(class_=True)
        # a_list = bs.find_all(href = 'http://news.baidu.com')
        # for a in a_list:
        #     print(a.string)

        # 5.text 文本参数
        # a_list = bs.find_all(text=['hao123', '地图', '贴吧'])
        # for a in a_list:
        #     print(a.string)
        '''
            这特喵有啥用？判断有没有？
            hao123
            地图
            贴吧'''
        # import re
        # # 6.用正则表达式来查找包含特定文本的内容，标签里的字符串
        # a_list = bs.find_all(text=re.compile("\d")) # 数字
        # for a in a_list:
        #     print(a.string)

        # 7.limit参数
        # a_list = bs.find_all("a", limit=3)  # 就要前三个
        # for a in a_list:
        #     print(a.string)

        # 8.css选择器.select()
        # #指定标签
        # print(bs.select('title')[0].string)
        # #百度一下，你就知道
        # #指定类名来查找 此处为class='mnav'
        # print(bs.select('.mnav'))
        # #指定id来查找
        # print(bs.select('#u1'))
        # #指定属性来查找
        # print(bs.select("[class='bri']"))
        # print(bs.select('a[href="//www.baidu.com/more/"]')[0].string)
        # [ < a class ="bri" href="//www.baidu.com/more/" name="tj_briicon" style="display: block;" > 更多产品 < / a >]
        # 更多产品

        # # 按子标签查找
        # print(bs.select("body > div > div > div > div > a"))

        # # 按照兄弟节点查找特定标签 '.'代表class
        print(bs.select(".mnav ~ .bri")[0].get_text())
        # 更多产品
except Exception:
    pass
