#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-04-01 10:06
from electshelf_Common_Lib.common_libs import *

def test_018_send_delGoods_package():
    '''删除分类下商品'''
    #删除商品前先列出分类商品，获取caseid
    response =commodityManage_queryCategoryCommodity()
    assert response['meta']['errno'] == 0
    assert response['meta']['msg'] == 'success'
    try:
        assert response[ 'result']['data'][0]['name'] == '1203商品'
        assert response[ 'result']['data'][0]['shopId'] == '5c2c2adbb80a8117ea575ea2'
        assert response[ 'result']['data'][0]['shopName'] == '语过添晴'
        assert response[ 'result']['data'][0]['sourceList'] != None
    except:
        print("该商品也被删除，请检查是否有该商品")

    getShop_caseID = response[ 'result']['data'][0]['id']

    if getShop_caseID != None:
        deleteCommodity = eshelfCaseLayer_deleteCommodity(int(getShop_caseID))
        assert deleteCommodity['meta']['errno'] == 0
        assert deleteCommodity['meta']['msg'] == 'success'

    # 删除完成以后，再次调用列出商品，检查是否删除
    listShop = commodityManage_queryCategoryCommodity()
    assert listShop['meta']['errno'] == 0
    assert listShop['meta']['msg'] == 'success'
    assert listShop['result']['data'][0]['name'] != '1203商品'

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