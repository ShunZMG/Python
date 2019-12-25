# -*- coding: utf-8 -*-

import tkinter as tk
import threading
import time
from main import *


def main_frame():
    '''游戏初始化窗口'''
    global main_window
    # 实例化tkinter对象,建立窗口Window
    main_window = tk.Tk()
    # 禁止窗口拉伸
    main_window.resizable(width=False, height=False)
    # 设置窗口的title
    main_window.title('飞机大战')
    # 设定窗口大小
    main_window.geometry('300x200')

    # 设定标签
    label1 = tk.Label(main_window, text='飞机大战',
                      font=('微软雅黑', 18), width=25, height=2)
    # 放置标签
    label1.pack()

    # 设定第二个标签
    label2 = tk.Label(main_window, text='请选择模式',
                      font=('微软雅黑', 14), width=25, height=2)
    # 放置标签
    label2.pack()

    # 创建空标签
    label3 = tk.Label(main_window, text='', width=7, height=1)
    label3.pack(side=tk.LEFT)
    # 创建第一个按钮
    btn1 = tk.Button(
        main_window,
        text='单人模式',
        command=singal_play,
        width=10,
        height=1
    )
    btn1.pack(side=tk.LEFT)

    # 创建空标签
    label4 = tk.Label(main_window, text='', width=5, height=1)
    label4.pack(side=tk.LEFT)

    # 创建第二个按钮
    btn2 = tk.Button(main_window, text='多人联机', width=10, height=1)
    btn2.pack(side=tk.LEFT)
    main_window.mainloop()


def singal_play():
    '''单人模式处理函数'''
    print('进入单人模式')
    # 打开单人模式窗口
    main_window.withdraw()
    singal_frame()
    main_window.quit()


def singal_frame():
    '''单人模式窗口'''
    global singal_window
    # 创建窗口
    singal_window = tk.Toplevel()
    # 设置窗口标题
    singal_window.title('飞机大战-单人模式')
    # 禁止窗口拉伸
    singal_window.resizable(width=False, height=False)
    # 设定窗口大小
    singal_window.geometry('850x400')

    # 创建标签
    label1 = tk.Label(singal_window, text='单人模式', width=25,
                      height=2, font=('微软雅黑', 18))
    label1.pack()

    # 创建第二个标签
    label2 = tk.Label(singal_window, text='点击战机即可进入游戏',
                      width=25, height=2, font=('微软雅黑', 18))
    label2.pack()
    # 图像列表
    img_list = []
    # 按钮列表
    btn_list = []
    # 获取图像
    for i in range(8):
        img_str = './frame_images/hero' + str(i + 1) + '.png'
        temp_img = tk.PhotoImage(file=img_str)
        img_list.append(temp_img)

    # 绘制button
    btn0 = tk.Button(singal_window, text='',
                     image=img_list[0], command=lambda: btn_def(1))
    btn0.pack(side=tk.LEFT)
    btn1 = tk.Button(singal_window, text='',
                     image=img_list[1], command=lambda: btn_def(2))
    btn1.pack(side=tk.LEFT)
    btn2 = tk.Button(singal_window, text='',
                     image=img_list[2], command=lambda: btn_def(3))
    btn2.pack(side=tk.LEFT)
    btn3 = tk.Button(singal_window, text='',
                     image=img_list[3], command=lambda: btn_def(4))
    btn3.pack(side=tk.LEFT)
    btn4 = tk.Button(singal_window, text='',
                     image=img_list[4], command=lambda: btn_def(5))
    btn4.pack(side=tk.LEFT)
    btn5 = tk.Button(singal_window, text='',
                     image=img_list[5], command=lambda: btn_def(6))
    btn5.pack(side=tk.LEFT)
    btn6 = tk.Button(singal_window, text='',
                     image=img_list[6], command=lambda: btn_def(7))
    btn6.pack(side=tk.LEFT)
    btn7 = tk.Button(singal_window, text='',
                     image=img_list[7], command=lambda: btn_def(8))
    btn7.pack(side=tk.LEFT)

    singal_window.mainloop()


def btn_def(plane_num):
    '''单人模式，用于接收选择的飞机号码'''
    print(plane_num)
    # 开启线程
    singal_thread = threading.Thread(target=lambda: main_game(plane_num), name='sinal_thread')
    singal_thread.start()
    singal_thread.join()
    # FIXME 有个小bug，不能删除窗口
    singal_window.withdraw()
    singal_window.quit()
    main_window.quit()


if __name__ == "__main__":
    main_frame()
