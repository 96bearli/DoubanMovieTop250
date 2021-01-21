# -*- codeing = utf-8 -*-
# @Time : 2021/1/7 14:40
# @Author : 96bearli
# @File : t1.py.py
# @Software : PyCharm


# def add(a, b):
#     return a + b
savepath = ".\\cache"
dataList = ["1","2"]
count = 1
for data in dataList:
    try:
        with open("%s\\%s.txt" % (savepath,count), "w+", encoding='utf-8') as f:
            f.write(data)
    except Exception as result:
        with open("%s\\%s.txt" % (savepath,count), "w+", encoding='utf-8') as f:
            f.write(result)
    count += 1