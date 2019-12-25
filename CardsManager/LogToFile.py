# !/usr/bin/python3
# -*- coding: utf-8 -*-


# class LogToFile:
#     def __init__(self):
#         pass

# @staticmethod
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def Log(log_info, flag, **kwargs):
    # flag如果为1，则表示添加
    if flag == 1:
        log_info += '名片的名字是:' + kwargs['Name']
    # flag如果为2，则表示删除
    elif flag == 2:
        log_info += '名片的名字是：' + kwargs['Name']
    # flag如果为3，则表示修改了名字
    elif flag == 3:
        log_info += kwargs['PRE_NAME'] + '修改为：' + kwargs['Name']
    # flag如果为4，则表示修改了电话号码
    elif flag == 4:
        log_info += kwargs['Name'] + '的电话号码从' + \
                    str(kwargs['PRE_TEL']) + '修改为' + str(kwargs['Tel'])
    # flag如果为5，则表示修改了QQ号
    elif flag == 5:
        log_info += kwargs['Name'] + '的QQ号码从' + \
                    str(kwargs['PRE_QQ']) + '修改为' + str(kwargs['QQ'])
    # flag如果为6，则表示读取一个名片
    elif flag == 6:
        log_info += '查看了' + kwargs['Name'] + '的名片'
    # flag如果为0，则表示读取了整个名片列表，并且为测试接口
    elif flag == 0:
        pass
    filename = os.path.join(BASE_DIR, 'log.txt')
    with open(filename, 'a+') as f:
        final_log_info = str(datetime.now()) + ":" + log_info
        f.write(final_log_info + '\n')
