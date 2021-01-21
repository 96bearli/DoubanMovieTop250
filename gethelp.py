# -*- codeing = utf-8 -*-
# @Time : 2021/1/7 15:06
# @Author : 96bearli
# @File : gethelp.py
# @Software : PyCharm
import bs4
import os


def getHelp(str):
    try:
        help(str)
    except Exception as result:
        print(result)
        print("出现错误,请重新输入")
        exit()
    return help(str)


def writeHelp(str, thing):
    f = open("help.txt", "a", encoding='utf-8')
    if str is not None:
        f.write(str)
        f.write("\n")
    else:
        f.write("%s is not found\n" % thing)
    f.close()


def main():
    thing = input("要获取帮助的函数是?(带括号)")
    writeHelp(getHelp(thing), thing)
    print("已保存到当前目录help.txt")


if __name__ == '__main__':
    main()
