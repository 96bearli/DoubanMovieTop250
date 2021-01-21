# -*- codeing = utf-8 -*-
# @Time : 2021/1/14 12:01
# @Author : 96bearli
# @File : testRe.py
# @Software : PyCharm
import re

# 正则表达式:字符串模式(判断字符串是否符合一定的标准)


# 创建模式,AA为正则表达式
# pat = re.compile("AA")
# " "被校验内容,search只招第一个
# m = pat.search("CBA")
# None

# m = pat.search("ASDAA")
# <re.Match object; span=(3, 5), match='AA'>区间左开右弼

# m = re.search("asd","asdsadasdasdasd")
# 第一个是匹配模式，第二个是被匹配的内容
# <re.Match object; span=(0, 3), match='asd'>
# print(m)

#
# f = re.findall("asd", "asdasdasdasd")
# # findall 返回一个列表
# print(f)
# # ['asd', 'asd', 'asd', 'asd']
#
# print(re.findall("[a-z].+a", "asdASDasdASD"))
#
# # 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符问题
# # "a\'\bv\n\\'"
# a = r"a\'\bv\n\\'"
# print(a)
# # a\'\bv\n\\'


from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open("../cache/movie.douban_1.txt", encoding="utf-8") as html:
        soup = BeautifulSoup(html.read(), features="html.parser")
    items = soup.findAll("div", class_='item')
    findDicts = {
        'link': re.compile(r'<a href="(.*?)">'),
        'src': re.compile(r'<img .+src="(.*?jpg)"', re.S),
        'title': re.compile(r'<span.*?([\u4e00-\u9fa5]*?)</span>'),
        'rating': re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>'),
        'judge': re.compile(r'<span>(\d*?人评价)</span>'),
        'inq': re.compile(r'<span class="inq">(.*?)</span>'),
        'bd': re.compile(r'<p class="">(.*?)</p>', re.S)
    }
    for item in items:
        print("第%i名"%(items.index(item)+1))
        print(re.findall(findDicts['link'], str(item))[0])
        print(re.findall(findDicts['src'], str(item))[0])
        print(re.findall(findDicts['title'], str(item))[0])
        print(re.findall(findDicts['rating'], str(item))[0])
        print(re.findall(findDicts['judge'], str(item))[0])
        print(re.findall(findDicts['inq'], str(item))[0])
        # replace进行替换,strip()去掉字符串前后空格
        print(re.findall(findDicts['bd'], str(item))[0].replace("<br/>\n"," ").strip())

    # findLink = "[https://movie.douban.com/subject/]+[0-9]+/"
    # findZh = "[\u4e00-\u9fa5]+"

"""    findLink = re.compile(r'<a href="(.*?)">')  # 带上括号就是输出的内容，这种规则比上边那种方便构造
    findImgSrc = re.compile(r'<img .+src="(.*?jpg)"', re.S)  # re.S表示"."可以代表换行之内的任意字符
    findTitle = re.compile(r'<span.*?([\u4e00-\u9fa5]*?)</span>')  # 中文，?表示非贪婪模式，就近匹配，可以试试去掉</span>就明白了
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
    findJudge = re.compile(r'<span>(\d*?人评价)</span>')
    findInq = re.compile(r'<span class="inq">(.*?)</span>')
    findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
    
    for item in items:
        print(re.findall(findLink, str(item))[0])
        print(re.findall(findImgSrc, str(item))[0])
        print(re.findall(findTitle, str(item))[0])
        print(re.findall(findRating, str(item))[0])
        print(re.findall(findJudge, str(item))[0])
        print(re.findall(findInq, str(item))[0])
        print(re.findall(findBd, str(item))[0])
        break"""



