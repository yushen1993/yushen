#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2020-03-25 13:37
import requests
from electshelf_conf.conf import *
from pprint import pprint

def operating_login():
    """
    运营后台登录，获取cookie
    :return:
    """
    url = host + '/ryoms/j_spring_security_check'
    header = {
        "Content-Type":"application/x-www-form-urlencoded",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
    data = {"j_username":j_username,"j_password":j_password,"verifyCode":""}
    response = requests.post(url,headers=header,params=data,allow_redirects=False)
    # pprint(response.headers,indent=2)
    cookie = response.headers['Set-Cookie'].split('=')[1].split(';')[0]
    # cookie = requests.utils.dict_from_cookiejar(response.cookies)
    pprint(cookie.strip())
    return cookie.strip()

def merchants_login():
    """
    商家后台登录，获取cookie
    :return:
    """
    url = host + '/bsoms/user/ajaxLogin'
    header = {
        "Content-Type":"application/json;charset=UTF-8",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"userName":userName,"password":password,"verifyCode":"","verifyCode1":"","phone":"","userPwd":"","userPwd2":""}
    response = requests.post(url,headers=header,json=data)

    cookie = response.headers['Set-Cookie'].split(',')[1].split(';')[0]
    # cookie = requests.utils.dict_from_cookiejar(response.cookies)
    # pprint(cookie.strip())

    return cookie.strip()

def machine_list():
    '''设备列表'''
    url = host + '/easy-smart-basic/machine/list'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"currentPage": 1, "mallId": mallId,"pageSize": 20,"terminalCode": "",
            "terminalName": "", "online": 2,"groupId":"","resolution":None,"shopIds":[]}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def mallApplication_getMallAppConfig():
    '''应用中心，应用列表'''
    url = host + '/easy-smart-basic/mallApplication/getMallAppConfig'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"mallId": mallId}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def merchantTemplate_shelfTemplateList():
    '''商家-电子货架模板配置列表'''
    url = host + '/easy-smart-shelf/merchantTemplate/shelfTemplateList'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"mallId": mallId}
    response = requests.post(url=url, headers=header, json=data)
    # pprint(response.json(),indent=2)
    return response.json()

def electronicShelfTemplate_list():
    '''大运营-电子货架模板列表'''
    url = host + '/easy-smart-shelf/ryMerchantTemplate/list'
    header = {
        "Cookie": operating_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    print(header)
    data = {"mallId":"5be53145b80a81146db071e2"}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def case_add(style):

    '''
    获取标准版模板id
    :param style: 模板类型 1.标准版 2.炫酷版
    :return: 返回模板id
    '''

    url = host + '/easy-smart/case/add'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    print(header)
    data = {"direction":"v","layoutName":"电子货架","mallId":"5be53145b80a81146db071e2","layoutId":650,"name":"test-one","style":style}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def eshelfCaseLayer_addOrUpdateCategory(name):

    '''
    修改模板分类名称
    :param name: 分类名称
    :return:
    '''

    url = host + '/easy-smart/eshelfCaseLayer/addOrUpdateCategory'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"dataList":[{"id":852,"name":name,"index":0,"caseId":3429,"pageId":2291,"caseLayerId":19513,"sourceId":2517,
            "clickSourceId":None,"backgroundSourceId":None,"state":None,
            "sourceUrl":"http://rongyi.b0.rongyi.com/system/smart/test/file/resourcePic/2003181743526995/2003181743526829.gif",
            "commodityNum":5,"easyCommodityNum":0,"aopuCommodityNum":0,"myCommodityNum":4,"clickSourceUrl":None,"backgroundSourceUrl":None}],
            "detailMap":{"style":1},"mallId":"5be53145b80a81146db071e2","pageId":2291}
    response = requests.post(url=url,headers=header,json=data)
    pprint(response.json(),indent=2)
    return response.json()

def eshelfCaseLayer_deleteCommodity(categoryCommodityId):
    '''删除商品'''
    url = host + '/easy-smart/eshelfCaseLayer/deleteCommodity'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"commodityCategoryId":"","mallId":mallId,"categoryCommodityId":categoryCommodityId}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def commodityManage_queryCategoryCommodity():
    '''列出模板内已添加商品，获取模板id'''
    url = host + '/easy-smart/commodityManage/queryCategoryCommodity'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"caseLayerId":19513,"commodityCategoryId":852,"mallId":"5be53145b80a81146db071e2","currentPage":1,"pageSize":10}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def eshelfCaseLayer_addComodity():
    '''标准模板内添加1203商品'''
    url = host + '/easy-smart/eshelfCaseLayer/addComodity'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"commodityIdList":["5de5fe7b6bcb4a82b79fd2d4"],"mallId":"5be53145b80a81146db071e2","from":1,"type":2,"categoryId":852}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def updateData_judgeHasUpdate():
    '''检测一键更新是否可用'''
    url = host + '/easy-smart/updateData/judgeHasUpdate'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"mallId":mallId}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def updateData_packUpdate():
    '''一键更新，下发增量包'''
    url = host + '/easy-smart/updateData/packUpdate'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"mallId":mallId}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def commodityManage_queryCategoryCommodityCount():
    '''一键更新，下发增量包'''
    url = host + '/easy-smart/commodityManage/queryCategoryCommodityCount'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"commodityCategoryId":852,"mallId":"5be53145b80a81146db071e2"}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def eshelfCaseLayer_queryHomePage():
    '''获取模板分类列表'''
    url = host + '/easy-smart/eshelfCaseLayer/queryHomePage'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"mallId":"5be53145b80a81146db071e2","pageId":2291,"caseId":"3429"}
    response = requests.post(url=url, headers=header, json=data)
    # pprint(response.json(),indent=2)
    return response.json()

def eshelfCaseLayer_addOrUpdateCategory_sum(name,commodityNum,myCommodityNum):

    """
    添加分类名称
    :param name: 分类名称
    :param commodityNum: 3：添加   4:修改
    :param myCommodityNum: 3：添加 4:修改
    :return:
    """

    url = host + '/easy-smart/eshelfCaseLayer/addOrUpdateCategory'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"dataList":[{"id":852,"name":name,"index":0,"caseId":3429,"pageId":2291,"caseLayerId":19513,"sourceId":2517,
            "clickSourceId":None,"backgroundSourceId":None,"state":None,
            "sourceUrl":"http://rongyi.b0.rongyi.com/system/smart/test/file/resourcePic/2003181743526995/2003181743526829.gif",
            "commodityNum":commodityNum,"easyCommodityNum":0,"aopuCommodityNum":0,"myCommodityNum":myCommodityNum,"clickSourceUrl":None,"backgroundSourceUrl":None}],
            "detailMap":{"style":1},"mallId":"5be53145b80a81146db071e2","pageId":2291}
    response = requests.post(url=url,headers=header,json=data)
    pprint(response.json(),indent=2)
    return response.json()

def casePage_queryPage():
    '''获取模板样式列表'''
    url = host + '/easy-smart/casePage/queryPage'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"mallId":"5be53145b80a81146db071e2","caseId":"3429"}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def electronicShelf_getCaseConfig():
    '''获取模板功能配置信息'''
    url = host + '/easy-smart/electronicShelf/getCaseConfig'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"caseId":"3429"}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def electronicShelf_editTemplateConfig(keywordList):
    """
    修改模板功能配置信息
    :param keywordList: ["商品","娱乐","餐饮","影视"]
    :return:
    """
    url = host + '/easy-smart/electronicShelf/editTemplateConfig'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"caseId":"3429","configJson":{"voice":1,"keywordList":keywordList,"face":1,"words":1,"rfid":1}}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def mallCase_getMallCaseList():
    '''获取模板功能配置信息'''
    url = host + '/easy-smart-web/mallCase/getMallCaseList'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"currentPage":1,"mallId":"5be53145b80a81146db071e2","pageSize":10,"style":"","name":"","appCode":"eShelf"}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

def caseAdvert_info():
    '''获取模板功能配置信息'''
    url = host + '/easy-smart/caseAdvert/list'
    header = {
        "Cookie": merchants_login(),
        "Content-Type": 'application/json',
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
    }
    data = {"caseId":"3429","name":"","currentPage":1,"pageSize":100,"mallId":"5be53145b80a81146db071e2"}
    response = requests.post(url=url, headers=header, json=data)
    pprint(response.json(),indent=2)
    return response.json()

# merchantTemplate_shelfTemplateList()
# mallApplication_getMallAppConfig()
# electronicShelfTemplate_list()
# merchants_login()
# machine_list()
# eshelfCaseLayer_addOrUpdateCategory('test-one')

# commodityManage_queryCategoryCommodity()  #列出商品
# eshelfCaseLayer_deleteCommodity(3977)     #删除商品 前先列出商品拿出商品id需要结合 保存接口使用


# eshelfCaseLayer_addComodity()   #新增商品 后 需要调保存接口，数据才可以生效
#
# eshelfCaseLayer_addOrUpdateCategory('test-one') #保存商品
# updateData_judgeHasUpdate()
# updateData_packUpdate()
# updateData_judgeHasUpdate()