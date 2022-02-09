from bs4 import BeautifulSoup
import re
file = open("./baidu.html","rb")
# file = open("./test.html","rb")
html = file.read().decode('utf-8')
bs = BeautifulSoup(html,"html.parser")


# bs为BeautifulSoup类表示整个文档为一种类型
# print(type(bs))
# print(bs.name)
# print(bs)
# print(bs.a.string)
# # Comment  是一个特殊的NavigableString  输出内容不包括注释
# print(type(bs.a.string))


# attrs 将 <a.tag> 变成 键值对
# print(bs.a.attrs)
#
# print(bs.title)
# print(type(bs.title))
# print(bs.title.string)
# print(type(bs.title.string))


#——————————————————————————————————————————————————————————————
#文档的遍历
#得到head tag 里面的内容 返回为列表 嘿嘿嘿
# print(bs.head.contents)

#文档的搜索
#字符串过滤 查找与字符串完全匹配到的内容
# t_list = bs.find_all("a")
# print(t_list)

# t_list = bs.find_all(["meta","link"])
# for item in t_list:
#     print(item)
#————————————————————————————————————————————————————————————————————————————
#正则表达式搜索 使用search()方法来匹配内容