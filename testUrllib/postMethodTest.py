#post 方法使用1 直接利用urllib.request.urlopen打开
import urllib.request
data = bytes(urllib.parse.urlencode({"hello":"word"}),encoding = 'utf-8')
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
print(response.read().decode('utf-8'))

#post 方法使用2 利用 urllib.request.Request 组织url
#利用伪装来实现豆瓣爬虫  agent伪装
url = "http://httpbin.org/post"
data = bytes(urllib.parse.urlencode({"hello":"word"}),encoding = 'utf-8')
headers = {
'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
req = urllib.request.Request(url = url,headers=headers,data=data,method="POST")

response = urllib.request.urlopen(req)

print(response.read().decode('utf-8'))