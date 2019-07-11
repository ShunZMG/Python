# !/usr/bin/python3
# -*- coding: utf-8 -*-

# Log Test
# from LogToFile import Log
# import os
# Log('hello')
# Log('world!')
# path = os.path.dirname(os.path.abspath(__file__))


# JsonHandler Test
# from JsonHandler import *
# data = [
#     {
#         'a': 1,
#         'b': 2
#     }
# ]
# write_to_json(data, 'data.json')
# data = open_json_file('data.json')
# print(type(data))


import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
