# !/usr/bin/python3
# -*- coding: utf-8 -*-

# 名片管理系统
from LogToFile import Log
from JsonHandler import *


class CardsManager:
    # 名片列表
    card_list = []

    def __init__(self):
        print('--------欢迎使用名片管理系统--------')
        Log('登入系统', 0)
        while True:
            print('''功能菜单如下：
            1 -->> 添加一张名片
            2 -->> 删除一张名片
            3 -->> 修改一张名片
            4 -->> 查看一张名片
            5 -->> 查看所有名片
            0 -->> 退出系统''')
            try:
                select_num = int(input('请输入您的选择：'))
            except:
                print('输入有误！请重新选择！')
                continue
            if select_num == 0:
                print('退出系统！')
                Log('退出系统', 0)
                break
            elif select_num == 1:
                self.add_card()
            elif select_num == 2:
                self.remove_card()
            elif select_num == 3:
                self.alter_card()
            elif select_num == 4:
                self.view_card()
            elif select_num == 5:
                self.print_cards()

    # 添加名片
    def add_card(self):
        self.card_list = open_json_file('data.json')
        temp_card = {}
        print('下面添加一张名片，请输入信息：')
        try:
            temp_card['Name'] = input('姓名：')
            temp_card['Tel'] = int(input('联系方式：'))
            temp_card['QQ'] = int(input('QQ：'))
            self.card_list.append(temp_card)
            write_to_json(self.card_list, 'data.json')
            print('添加成功！')
            Log('添加了一张名片，', 1, Name=temp_card['Name'])
        except:
            print('添加失败，请重新输入！')

    # 删除名片
    def remove_card(self):
        flag = 0
        self.card_list = open_json_file('data.json')
        name = input('请输入您要删除的名片中的姓名：')
        for l in self.card_list:
            if l['Name'] == name:
                flag = 1
                self.card_list.remove(l)
                print('删除成功！')
                Log('删除了一张名片，', 2, Name=l['Name'])
        if flag == 0:
            print('名片列表中没有这个人哦！请重新选择')
        write_to_json(self.card_list, 'data.json')

    # 修改名片
    def alter_card(self):
        self.card_list = open_json_file('data.json')
        flag = 0
        name = input('请输入您要修改的名片中的姓名：')
        for l in self.card_list:
            if l['Name'] == name:
                while True:
                    flag = 1
                    print('''所要修改的名片存在，请选择修改选项(选择0 -->> 退出修改之后才会保存哦！)：
                    1 -->> 修改姓名
                    2 -->> 修改电话
                    3 -->> 修改QQ号
                    0 -->> 退出修改''')
                    try:
                        alter_num = int(input('您的选择是：'))
                        if alter_num == 0:
                            print('退出修改！')
                            Log('修改成功保存', 0)
                            break
                        elif alter_num == 1:
                            self.alter_name(l)
                        elif alter_num == 2:
                            self.alter_tel(l)
                        elif alter_num == 3:
                            self.alter_qq(l)
                    except:
                        print('输入有误！请输入数字！')
        if flag == 0:
            print('您要修改的名片不在名片列表中，请先添加！')
            return
        write_to_json(self.card_list, 'data.json')

    # 查看名片
    def view_card(self):
        try:
            self.card_list = open_json_file('data.json')
            index = int(input('请输入您要查看的名片的次序(从1开始)：'))
            if 0 < index <= len(self.card_list):
                print('您要查看的名片是：')
                temp_dict = self.card_list[index - 1]
                print('姓名\t\t电话\t\tQQ号')
                print('%s\t\t%s\t\t%s' %
                      (temp_dict['Name'], temp_dict['Tel'], temp_dict['QQ']))
                Log('查看了一次名片！', 6, Name=temp_dict['Name'])
            else:
                print('输入有误！没有这个名片序号！请重新选择！')
        except:
            print('输入有误！请输入数字！')

    # 打印名片列表
    def print_cards(self):
        self.card_list = open_json_file('data.json')
        print('姓名\t\t电话\t\tQQ号')
        for cards in self.card_list:
            print('%s\t\t%s\t\t%s' %
                  (cards['Name'], cards['Tel'], cards['QQ']))
        Log('读取了整个名片列表', 0)

    # 修改名片姓名
    def alter_name(self, card_dict):
        name = input('请输入修改后的姓名：')
        pre_name = card_dict['Name']
        card_dict['Name'] = name
        Log('修改了姓名，', 3, PRE_NAME=pre_name, Name=name)
        print('修改成功！')

    # 修改名片电话号码
    def alter_tel(self, card_dict):
        try:
            tel = int(input('请输入修改后的电话号码：'))
            pre_tel = card_dict['Tel']
            card_dict['Tel'] = tel
            Log('修改了电话号码，', 4,
                Name=card_dict['Name'], PRE_TEL=pre_tel, Tel=tel)
            print('修改成功！')
        except:
            print('请输入数字！')

    # 修改名片QQ号
    def alter_qq(self, card_dict):
        try:
            qq = int(input('请输入修改后的QQ号码：'))
            pre_qq = card_dict['QQ']
            card_dict['QQ'] = qq
            Log('修改了QQ号，', 5, Name=card_dict['Name'], PRE_QQ=pre_qq, QQ=qq)
            print('修改成功！')
        except:
            print('请输入数字！')


if __name__ == '__main__':
    card_manager = CardsManager()
