#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 18:13
from electshelf_Common_Lib.common_libs import *
from electshelf_conf.conf import *

def test_015_getMallCaseList():
    '''获取电子货架模板列表，检测上面添加的模板信息是否在该列表内'''
    response = mallCase_getMallCaseList()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    assert response['result']['data'][0]['name'] == 'test-one'
    assert response['result']['data'][0]['layoutName'] == '电子货架'
    assert response['result']['data'][0]['style'] == 1  #1:标准版 2：炫酷版
    assert response['result']['data'][0]['updateBy'] == userName