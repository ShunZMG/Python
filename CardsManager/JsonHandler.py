# !/usr/bin/python3
# -*- coding: utf-8 -*-

# 读取用户数据的json文件
import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def write_to_json(data, filename):
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'w') as f:
        json.dump(data, f)


def open_json_file(filename):
    filename = os.path.join(BASE_DIR, filename)
    with open(filename, 'r') as f:
        data = json.load(f)
    return data
