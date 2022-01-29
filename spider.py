from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    #爬取网页
    datalist = getData(baseurl)
    savaPath = ".\\doubanTop250.xls"
    #保存数据
    savaData(savaPath)

#爬取网页
def getData(baseurl):
    datalist = []
    # 解析数据
    return datalist


#保存数据
def savaData(savaPath):
    print("sava...")
    pass


if __name__== "__main__" :
    main()