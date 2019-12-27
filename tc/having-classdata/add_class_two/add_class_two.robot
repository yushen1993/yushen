*** Settings ***
Library  pylib.SchoolClassLib.School_class

*** Test Cases ***
添加班级2 - tc000002
    ${addclass2}=       add_classroom   1     实验三班      80

    #列出班级,检查
    ${listclass2}=       list_classroom
    ${findsjson}=       evaluate      $listclass2['retlist'][-1]
    log to console      ${findsjson}
    log to console      &{findsjson}[id]
    should be true      $findsjson['id']==$addclass2['id']
    should be true      $findsjson['grade__name']=="七年级"
    should be true      $findsjson['invitecode']==$addclass2['invitecode']
    should be true      $findsjson['name']=='实验三班'
    should be true      $findsjson['studentlimit']==80