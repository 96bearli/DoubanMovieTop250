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


f = re.findall("asd","asdasdasdasd")
# findall 返回一个列表
print(f)
# ['asd', 'asd', 'asd', 'asd']

print(re.findall("[a-z].+a","asdASDasdASD"))