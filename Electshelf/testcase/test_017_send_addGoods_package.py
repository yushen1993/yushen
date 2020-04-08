#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-31 18:47
from electshelf_Common_Lib.common_libs import *

def test_017_send_package():
    '''添加商品'''
    response = eshelfCaseLayer_addComodity()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'

    save_goods = eshelfCaseLayer_addOrUpdateCategory('test-one')
    assert save_goods['meta']['errno'] == 0
    assert save_goods['meta']['msg'] == 'success'
    # assert save_goods['result']['data']['category']['caseName'] == 'test-one'

    #保存模板

    # updateData_judgeHasUpdate()
    # updateData_packUpdate()
    # updateData_judgeHasUpdate()

    #数据变更后，检查一键更新按钮是否可用
    cheack_updata = updateData_judgeHasUpdate()
    assert cheack_updata['meta']['errno'] == 0
    assert cheack_updata['meta']['msg'] == 'success'
    if cheack_updata['result']['data']['hasUpdate'] == True: #等于true，可更新
        send_package = updateData_packUpdate()  #点击一键更新
        assert send_package['meta']['errno'] == 0
    else:
        print("无数据变更，无需更新")
    #一键更新后再次检查一键更新是否置灰
    cheack_end_updata = updateData_judgeHasUpdate()
    assert cheack_end_updata['meta']['errno'] == 0
    assert cheack_end_updata['meta']['msg'] == 'success'
    assert cheack_end_updata['result']['data']['hasUpdate'] == False