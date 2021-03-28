# coding:utf-8

import requests
import json

def search(name,url):
    # 添加任务地址
    add_task = 'http://query.shuzhikj.com/api/platform/add_task?name='+name+'&url='+url+'&type=1&urlmode=1'
    # 请求头带上apikey参数以及对应的值
    headers = {
        'apikey': 'mJDNNXnsu946MLB'
    }
    name = input('请输入关键词')
    uel = input('请输入url')

