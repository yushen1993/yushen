*** Settings ***
Library  pylib.SchoolClassLib.School_class

*** Test Cases ***
添加班级3 - .tc000003
    ${addclass3}=       add_classroom       1   实验二班    80
    should be true      $addclass3['retcode']==1

    #列出班级检查
    ${listclass3}=      list_classroom      1
    ${listclass3json}=      evaluate        $listclass3['retlist'][-1]
    should be true      $listclass3json['name']=='实验二班'

#    :FOR    ${one}      IN      @{listclass3json}
#    \   log to console     ${one}