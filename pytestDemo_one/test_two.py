# -*- coding: utf-8 -*-
import pytest

import requests
@pytest.mark
def test_usrLogin():
    a = input("请输入你要发送HTTP请求的URL链接：")
    response = requests.get(a)
    if response.status_code == 404:
        print("你输入的HTTP请求地址：{} 出现链接异常，请确认地址是否正确！".format(response.url))
    else:
        print(response.status_code)