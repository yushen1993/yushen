#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 18:29

from electshelf_Common_Lib.common_libs import *
from electshelf_conf.conf import *
from electshelf_Common_Lib.mysql_db_lib import *

def test_016_machineList():
    '''获取设备信息'''
    response = machine_list()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    for one in response['result']['data']['machines']:
        if one['code'] == code:
            assert one['address'] == "TEST-2019-wz"
            assert one['appName'] == "电子货架"
            assert one['caseName'] == "test-one"
            assert one['updateBy'] == userName
            assert one['dataVersion'] == mysql_db()[3]

    # assert response['result']['data'][0]['layoutName'] == '电子货架'
    # assert response['result']['data'][0]['style'] == 1  #1:标准版 2：炫酷版
    # assert response['result']['data'][0]['updateBy'] == userName