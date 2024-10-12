# -*- coding: utf-8 -*-

import json
import base64
import os
import ssl

try:
    from urllib.error import HTTPError
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen, HTTPError

context = ssl._create_unverified_context()


def get_img(img_file):
    """将本地图片转成base64编码的字符串，或者直接返回图片链接"""
    # 简单判断是否为图片链接
    if img_file.startswith("http"):
        return img_file
    else:
        with open(os.path.expanduser(img_file), 'rb') as f:  # 以二进制读取本地图片
            data = f.read()
    try:
        encodestr = str(base64.b64encode(data), 'utf-8')
    except TypeError:
        encodestr = base64.b64encode(data)

    return encodestr


def posturl(headers, body):
    """发送请求，获取识别结果"""
    try:
        params = json.dumps(body).encode(encoding='UTF8')
        req = Request(REQUEST_URL, params, headers)
        r = urlopen(req, context=context)
        html = r.read()
        return html.decode("utf8")
    except HTTPError as e:
        print(e.code)
        print(e.read().decode("utf8"))


def request(appcode, img_file, params):
    # 请求参数
    if params is None:
        params = {}
    img = get_img(img_file)
    params.update({'image': img})

    # 请求头
    headers = {
        'Authorization': 'APPCODE %s' % appcode,
        'Content-Type': 'application/json; charset=UTF-8'
    }

    response = posturl(headers, params)
    return response


# 请求接口
REQUEST_URL = "https://form.market.alicloudapi.com/api/predict/ocr_table_parse"

if __name__ == "__main__":
    # 配置信息

    appcode = "71907e1500c74dd6ba9c5710530fd3ed"

    path = r"D:\AdmissionInf\pic"
    files = os.listdir(path)
    l = len(files)
    for i in range(l):
        img_file = r"D:\AdmissionInf\pic\ ({}).jpg".format(i+1)  # 注意空格
        params = {
            "configure": {
                "format": "xlsx",  # 输出格式
                "dir_assure": "true",  # 图片方向是否确定是正向的
                "line_less": "false"  # 是否为无线表格
            }
        }
        result = request(appcode, img_file, params)
        res_obj = json.loads(result)
        with open(r"D:\AdmissionInf\结果\output{}.xlsx".format(i+1), 'wb') as fout:
            fout.write(base64.b64decode(res_obj["tables"]))
