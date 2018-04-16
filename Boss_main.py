# -*- coding:utf-8 -*-
import re
import requests
from Boss_rule import *
from sqlite_common import *
keywords=""

def build_reg(dic_info_re):
    str_re=""
    for key in dic_info_re:
        str_re+=dic_info_re.get(key,"9999999")+".*?"
    return str_re

def parse_main_page(html,reg):
    #print(reg)
    pat=re.compile(reg,re.S)
    list_info = pat.findall(html)
    pro_keypoint(list_info, 3)
    return list_info
def parse_detail_page(html,reg):
    pat = re.compile(reg, re.S)
    list_detail = pat.findall(html)
    for i,dataRow in enumerate(list_detail):
        dataRow=list(dataRow)
        for j,data in enumerate(dataRow):
            data=data.replace('\n','').replace('<br/>',"  ").strip()
            dataRow[j]=data
        list_detail[i]=dataRow
    return list_detail


def get_page_html(url,head=None):
    responce = requests.get(url,headers=head)
    if(responce.status_code==200):
        return responce.text
    else:
        print("抓取数据错误")
        return None
def pro_keypoint(data,index):
    i=0
    for row in data:
        data_copy=list(row)
        str=row[index].replace("</span>","").replace("<span>"," ")
        data_copy[index]=str
        data[i]=data_copy
        i+=1

def build_head_sql(head_list):
    return (',').join(head_list)

def format_value(org_value):
    return "\'"+str(org_value)+"\'"
def build_insert_sql(data,head_list,table_name):
    list_insert=[]
    str_insert=""
    str_head_sql=build_head_sql(head_list)
    if(data and len(data[0])!=len(head_list)-1):
        print("数据错误")
        return str_insert
    if(isinstance(data,list)):
        for info in data:
            str_row_value=",".join(map(format_value,info))+","+format_value(keywords)
            if(str_row_value):
                str_insert = "insert into %s (%s) values(%s)" % (table_name, str_head_sql,str_row_value)+"\n"
                list_insert.append(str_insert)
    return list_insert
def save_to_db(list_info):
    sql_insert = build_insert_sql(list_info, boss_info_list, "boss_info")
    insert(sql_insert, connect("boss.db"))


def make_boss_url(keywords,page_index):
    boss_site = "https://www.zhipin.com/"
    boss_url = "job_detail/?query=%s&page=%s" % (keywords, page_index)
    return boss_site+boss_url
def get_detail_info(detail_url,head=None):
    boss_site = "https://www.zhipin.com"
    detail_url=boss_site+detail_url
    text_detail=get_page_html(detail_url,head)
    detail_info=parse_detail_page(text_detail,build_reg(dic_detail_re))
    print(detail_info)

def main():
    keywords = "python"
    page = 1
    url = make_boss_url(keywords, page)
    print(url)
    html = get_page_html(url, boss_head)
    #print(html)
    list_info = parse_main_page(html, build_reg(dic_info_re))
    print(list_info)
    print("共抓取%d条数据" % len(list_info))
    #save_to_db(list_info)
    for eachRow in list_info:
        detail_url=eachRow[0]
        get_detail_info(detail_url,boss_head)
main()


