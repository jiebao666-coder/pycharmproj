import base64

import pandas as pd
# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
import os
import sys
import json
import openpyxl

from typing import List
from alibabacloud_ocr_api20210707.client import Client as ocr_api20210707Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_ocr_api20210707 import models as ocr_api_20210707_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_darabonba_stream.client import Client as StreamClient
from alibabacloud_tea_console.client import Client as ConsoleClient




class Sample:
    def __init__(self):
        pass


    @staticmethod
    def create_client() -> ocr_api20210707Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/ocr-api
        config.endpoint = f'ocr-api.cn-hangzhou.aliyuncs.com'
        return ocr_api20210707Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        body_stream = StreamClient.read_from_file_path(r"D:/pic/2023guangdong.png")
        recognize_basic_request = ocr_api_20210707_models.RecognizeBasicRequest(
            body=body_stream,
            need_rotate=False
        )
        try:
            # 复制代码运行请自行打印 API 的返回值
            result = client.recognize_basic_with_options(recognize_basic_request, util_models.RuntimeOptions())
            items = json.loads(result.body.data)

            with open(r"D:\result.xlsx", 'wb') as fout:
                fout.write(base64.b64decode(items))

        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        body_stream = StreamClient.read_from_file_path(r"D:/pic/2023guangdong.png")
        recognize_basic_request = ocr_api_20210707_models.RecognizeBasicRequest(
            body=body_stream,
            need_rotate=False
        )
        try:
            # 复制代码运行请自行打印 API 的返回值
            resp = await client.recognize_table_ocr_with_options_async(recognize_basic_request, util_models.RuntimeOptions())
            ConsoleClient.log(UtilClient.to_jsonstring(resp))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])

    # result = []
    # for i in r.json()['prism_wordsInfo']:
    #     pos = []
    #     for j in i['pos']:
    #         pos.append(j['x'])
    #         pos.append(j['y'])
    #     pos.append(i['word'])
    #     result.append(pos)
    # print(result)