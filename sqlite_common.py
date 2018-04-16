import sqlite3
from Boss_rule import *
#连接数据库，不存在则创建
def connect(db_name):
    try:
        con=sqlite3.connect(db_name)
    except Exception as  e:
        print(repr(e))
    return con
def excute(sql,con):
    try:
        c=con.cursor()
        c.execute(sql)
        con.commit()
        con.close()
    except Exception as  e:
        print(repr(e))
def insert(sql_list,con):
    try:
        for sql in sql_list:
            c=con.cursor()
            c.execute(sql)
        con.commit()
        con.close()
        print("插入成功")

    except Exception as  e:
        print(repr(e))
def select(sql,con):
    try:
        c=con.cursor()
        re = c.execute(sql)
        con.commit()
        con.close()
    except Exception as  e:
        print(repr(e))

conn=connect("Boss.db")
