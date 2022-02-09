from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl_test = "http://www.baidu.com"
    baseurl = "https://movie.douban.com/top250?start="
    #爬取网页
    datalist = getData(baseurl)
    savaPath = ".\\doubanTop250.xls"
    #保存数据
    savaData(savaPath,datalist)
    # askURL(baseurl_test)

#获取链接
findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"/>',re.S)  # 忽略换行符
findTitle = re.compile(r'<span class="title">(.*?)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
findRatingPeople = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*?)</span>')
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)
#爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0,10): #调用不同页面
        url = baseurl + str(i*25)
        html = askURL(url)  #保存网页源码

        # 逐一解析数据
        soup = BeautifulSoup(html,"html.parser")
        # 查找形成列表
        for item in soup.find_all('div' ,class_ ="item"):
            data = []
            item = str(item)
            #信息收集
            link = re.findall(findLink,item)[0]
            data.append(link)
            imgSrc = re.findall(findImgSrc,item)[0]
            data.append(imgSrc)
            title = re.findall(findTitle,item)
            if (len(title) >= 2):
                ctitle = title[0]
                data.append(ctitle)
                otitle = re.sub('/', "", title[1])
                otitle = re.sub('\xa0', "", otitle)
                data.append(otitle)
            else:
                data.append(title[0])
                data.append('  ')
            rating = re.findall(findRating,item)[0]
            data.append(rating)
            judgeNumber = re.findall(findRatingPeople,item)[0]
            data.append(judgeNumber)
            inq = re.findall(findInq,item)
            if (len(inq)!=0):
                data.append(inq[0].replace("。",""))
            else:
                data.append(" ")
            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)
            bd = re.sub('/', " ", bd)
            bd = re.sub('\xa0', " ", bd)
            data.append(bd.strip())

            datalist.append(data)
    # print(datalist)
    return datalist

#保存数据
def savaData(savaPath,datalist):
    print("sava...")
    book = xlwt.Workbook(encoding='utf-8')
    sheet = book.add_sheet('豆瓣TOP250')
    col = ("电影详情链接","图片链接","影片中文名","影片外文名","评分","评分数","概况","相关信息")
    for i in range(0,8) :
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("这是第{0}条",i)
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save(savaPath)



# 获得网页内容
def askURL(url):
    head = { #模拟浏览器头部
        'User-Agent':'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    req = urllib.request.Request(url,headers = head)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    # html = ""
    # try:
    #     response = urllib.request.urlopen(req)
    #     content = response.read()
    #     html = response.read().decode('utf-8')
    #     f = open("test.html", "ab+")
    #       # 读取网页内容
    #     f.write(content)
    #     f.close()
    # except  urllib.error.URLError as e:
    #     if hasattr(e,"code"):#有标签，或者有属性
    #         print(e.code)
    #     if hasattr(e,"reason"):
    #         print(e.reason)
    return html

if __name__== "__main__" :
    main()
    print("爬取完毕")