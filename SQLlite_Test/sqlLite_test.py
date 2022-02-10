#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')

print ("数据库打开成功")

c = conn.cursor()       # get 游标

sql = ""

c.execute(sql)

conn.commit()
conn.close()

print("successfully create a table")