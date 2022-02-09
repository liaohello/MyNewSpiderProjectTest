import re

pat  = re.compile("AA")

# m = pat.search("CBA")
#span左闭右开
#search 只找到第一个匹配项
m = pat.search("ACBA22AA2222AAA")
print(m)
#sub
print(re.sub("a","A","aaaaasssssdddd"))#找到a用A来替换

a = r"\aabd-\'"
print(a)
