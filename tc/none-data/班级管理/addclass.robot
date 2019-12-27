*** Settings ***
Library  pylib.SchoolClassLib.School_class

*** Test Cases ***
添加班级1-tc000001
    ${addclassone}=     add_classroom       1       实验1班      80
    log to console      ${addclassone}
    should be true      $addclassone['retcode']==0
    #列出班级检查
    ${listclass}=       list_classroom
    ${findone}=     evaluate       $listclass['retlist'][0]
    log to console      ${findone}
    should be true      $findone['id']==$addclassone['id']
    should be true      $findone['invitecode']==$addclassone['invitecode']
    should be true      $findone['name']=='实验1班'
    should be true      $findone['grade__name']=='七年级'
    should be true      $findone['studentlimit']==80

#    [Setup]     delete_classroom    &addclassone[id]