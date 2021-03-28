# coding: utf-8

import json
import mysql.connector
import requests
import time
import datetime

def Inquire():
    # 获取需要查询的任务(单个)
    url_host = 'https://t.idccap.com/api/v1/QuickRanking/get_unqueried_task'
    # 获取请求
    url = requests.post(url=url_host)
    url_text = url.text
    # 时间戳
    create_at = int(time.time())
    # print(url_text)
    # 网页状态码
    status = url.status_code
    # print(status)


    # def log 函数传输点
    log(url_host=url_host, create_at=create_at, url_text=url_text, status=status)

    # sql_log(website=url_text['data']['website'], keyword=url_text['data']['keyword'], id=url_text['data']['id'])

    # 将str类型的数据转成dict字典
    json_url = json.loads(url_text)
    # print(json_url)

    # 查询 code 是否属于1
    if json_url['code'] != 1:
        print("任务读取已完成，暂无任务。")
        return
    # 输出请求结果
    site_host(website=json_url['data']['website'], keyword=json_url['data']['keyword'], id=json_url['data']['id'], create_at=create_at)
    # print(json_url['data']['id'])
    # print(json_url['data']['website'])
    # 解析出data内容
    # json_data = json_url['data']
    # for a in json_data:
    #     # id = a['id']
    #     # website = a['website']
    #     # keyword = a['keyword']
    #     print(a)



# site_host 表操作
def site_host(website, keyword, id, create_at):

    # sql insert 插入语句
    sql = 'insert into task( website, keyword, fr_id, create_at) values(%s, %s, %s, %s)'
    values = (website, keyword, id, create_at)
    try:
        cursor.execute(sql, values)
        print('加入任务》》', '网址：', website,  '关键词：', keyword)
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()

# log 表操作
def log(url_host, create_at, url_text, status):
    # print("记录储存数据库")
    sql = 'insert into log(host, create_at, return_en, status) values(%s, %s, %s, %s)'
    values = (url_host, create_at, url_text, status)
    # print('状态码是', status)
    try:
        cursor.execute(sql, values)
        print('加入记录》》', '地址：', url_host, '时间:', create_at, '状态：', status)
        con.commit()
    except Exception as e:
        print(e)
        con.rollback()


# # 查询
# def s_q():
#     # sql查询语句
#     sql = 'SELECT id,host,status FROM site_host;'
#     # 将sql变量语句传入execute方法里面，执行mysql语句
#     cursor.execute(sql)
#     # 输出查询结果
#     for one in cursor:
#         print(one[0], one[1], one[2])
#     # sq = 'select count(1) from task where website = "http://www.baidu.com" and keyword = "test"'

# ------------------
# con = mysql.connector.connect(**config)
# # 创建游标，用于执行mysql语句，并且查询结果会一并保存游标之中。
# cursor = con.cursor()
# # sql查询语句
# sql = 'SELECT id,host,status FROM site_host;'
# # 将sql变量语句传入execute方法里面，执行mysql语句
# cursor.execute(sql)
# # 输出查询结果
# for one in cursor:
#     print(one[0], one[1], one[2])
# # 关闭连接
# con.close()


if __name__ == '__main__':
    config = {
        'host': 'localhost',
        'port': 3306,
        'user': 'duobao',
        'password': 'wasd123',
        'database': 'duobao'
    }
    con = mysql.connector.connect(**config)
    # 创建游标，用于执行mysql语句，并且查询结果会一并保存游标之中。
    cursor = con.cursor()
    Inquire()
    # sql_log()
    con.close()
    # site_host()
