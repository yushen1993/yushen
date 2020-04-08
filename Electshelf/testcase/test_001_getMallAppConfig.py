#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-30 16:56
from electshelf_Common_Lib.common_libs import *

def test_001_mallApplication_getMallAppConfig():
    """测试应用中心，应用列表"""
    cm = mallApplication_getMallAppConfig()
    assert cm['meta']['errno'] == 0
    assert cm['meta']['msg'] == 'success'
    response = cm['result'][ 'data']
    dataList = [data['name'] for data in response]

    try:
        assert dataList == ['智能易拉宝', '电子货架', '商场版定制', '游戏盒子', '交互式货架', '丝芙兰', '套娃']
    except:
        print("列表元素有变化，请检查{}".format(response))
    # print(dataList)