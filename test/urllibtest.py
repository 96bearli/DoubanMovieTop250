# -*- codeing = utf-8 -*-
# @Time : 2021/1/7 15:40
# @Author : 96bearli
# @File : urllibtest.py
# @Software : PyCharm

# import urllib.request

# get方式获取网页源代码
'''
response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode("utf-8"))
'''

# post方式请求

# import urllib.parse
# # data  (urllib.parse解析+encoding="utf-8") bytes二进制封装
# data = bytes(urllib.parse.urlencode({"hi":"this is a test"}),encoding="utf-8")  # 转为2进制
# # 在open的基础上还要发出data
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# # decode()默认utf-8
# print(response.read().decode())

# 输出
'''
{
  "args": {}, 
  "data": "", 
  "files": {}, 
  "form": {
    "hi": "this is a test"
  }, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Content-Length": "17", 
    "Content-Type": "application/x-www-form-urlencoded", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.8", 
    "X-Amzn-Trace-Id": "Root=1-5ff6bfd7-6a2d67496b666e397f6b32d8"
  }, 
  "json": null, 
  "origin": "", 
  "url": "http://httpbin.org/post"
}
'''
# 超时处理,单位秒
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode())
# except urllib.error.URLError as result:
#     print('time out')

# import urllib.request
# response = urllib.request.urlopen("http://www.baidu.com/")
# # print(response.status)
# # 200 #状态码,正常
# print(response.getheaders())
# print(response.getheader("Set-Cookie")) #去掉s可以获取单个信息

# UA伪装(例子：伪装真实访问并获取网页源码)
'''
import urllib.request

url = "http://www.httpbin.org/post"
# data的构建形式
data = bytes(urllib.parse.urlencode({"hi": "this is a test"}), encoding="utf-8")  # 转为2进制
# headers字典内可以构建完全的浏览器信息键值对（可以在devTool获取）
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
}
# req是用Request类构建的请求 默认get方式
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# 用urlopen对网站发起请求req
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''

#  应用
import urllib.request

url = "https://movie.douban.com/top250?start=0"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66"
}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
