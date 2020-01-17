# !/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json


def main(long_url):
    host = 'https://dwz.cn'
    path = '/admin/v2/create'
    url = host + path
    method = 'POST'
    content_type = 'application/json'

    token = 'd04356ae29428200fe6ec27fa8f4fe67'

    bodys = {
        'Url': long_url,
        'TermOfValidity': '1-year'}

    # 配置headers
    headers = {'Content-Type': content_type, 'Token': token}

    # 发起请求
    response = requests.post(url=url, data=json.dumps(bodys), headers=headers)

    # 读取响应
    print(response.json()['ShortUrl'])
    return response.json()['ShortUrl']
