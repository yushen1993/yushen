#-*- coding:utf-8 -*-
# @Author : yushen
# @Time : 2019-12-25 16:23
import requests
import pprint
from cnf import g_vcode

class School_class():

    Url='http://ci.ytesting.com/api/3school/school_classes'

    def __init__(self):
        self.vcode = g_vcode

    def set_vcode(self,vcode):
        self.vcode = vcode

    def add_classroom(self,grade,name,studentlimi):
        """
        添加课程
        :param grade:   指明年级的id号
        :param name:    指明添加班级的名称
        :param studentlimi:     指明班级学生的人数上限
        :return:
        """
        body = {
            "vcode":self.vcode,
            "action":'add',
            "grade":int(grade),
            "name":name,
            "studentlimit":int(studentlimi)
        }
        response = requests.post(self.Url,data=body)

        pprint.pprint(response.json(),indent=2)
        return response.json()

    def modify_classroom(self,classid,name,studentlimit):
        """
        修改课程
        :param classid: 要修改班级的ID号
        :param name:    指明添加班级的名称
        :param studentlimit:    指明班级学生的人数上限
        :return:
        """
        url = "{}/{}".format(self.Url,classid)
        body = {
            "vcode":self.vcode,
            "action":"modify",
            "name":name,
            "studentlimit":studentlimit
        }
        response = requests.put(url,data=body)
        pprint.pprint(response.json())
        return response.json()

    def list_classroom(self,gradeid=None):
        """
        列出课程
        :param gradeid: 年级的id号
        :return:
        """
        if gradeid != None:
            body = {
                "vcode":self.vcode,
                "action":'list_classes_by_schoolgrade',
                "gradeid":int(gradeid)
            }
        else:
            body = {
                "vcode":self.vcode,
                "action":'list_classes_by_schoolgrade'
            }
        response = requests.get(self.Url,params=body)
        # classidlList = []
        bodydict = response.json()
        pprint.pprint(bodydict)
        return bodydict
        # classID = bodydict['retlist']
        # for id in classID:
        #     classidlList.append(id['id'])
        # print(classidlList)
        # pprint.pprint(response.json(),indent=2)
        # return classidlList
        # return response.json()
    def delete_classroom(self,classid):
        """
        删除课程
        :param classid: 班级ID
        :return:
        """
        url = "{}/{}".format(self.Url,classid)
        body = {
            "vcode":self.vcode
        }
        response = requests.delete(url,data=body)
        # pprint.pprint(response.json())
        return response

    def delete_all_classroom(self):
        """
        删除所有课程
        :return:
        """
        #现列出所有班级
        classJson = self.list_classroom()
        pprint.pprint(classJson)
        classId = classJson['retlist']
        for id in classId:
            self.delete_classroom(id['id'])
        #检查课程是否删除完
        cp =self.list_classroom()
        if cp['retlist'] != []:
            print("列表数据未删空，存在数据残留，请检查！！")
            # School_class().delete_classroom(id['id'])
        # classid=self.list_classroom(1)
        # # print(classid)
        # for id in classid:
        #     url = "{}/{}".format(self.Url,id)
        #     body = {
        #         "vcode":self.vcode
        #     }
        #     response = requests.delete(url,data=body)
        #     print(response.json())

# if __name__ == '__main__':
#     scm = School_class()
#     ret = scm.list_classroom(1)
cm = School_class()
# cm.delete_classroom(290709)
cm.list_classroom()
# cm.add_classroom(1,'1班',60)
# cm.list_classroom()
# cm.delete_all_classroom()
# cm.list_classroom()

