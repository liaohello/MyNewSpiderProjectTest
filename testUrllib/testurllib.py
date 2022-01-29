# import urllib.request
#
# #得到一个 get 请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))
#
# #得到一个 post 请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding='utf-8')
# response = urllib.request.urlopen("http://httpbin.org/post",data = data)
# print(response.read().decode('utf-8'))

from urllib.request import urlopen

myURL = urlopen("https://www.runoob.com/")
f = open("runoob_urllib_test.html", "wb")
content = myURL.read()  # 读取网页内容
f.write(content)
f.close()
