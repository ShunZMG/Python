import pygame
import sys
from pygame.locals import *
from random import *

# 我方战机


class MyPlane(pygame.sprite.Sprite):
    # 初始化方法，给定屏幕大小
    def __init__(self, bg_size, number):
        # 调用精灵父类的初始化方法%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        # 在游戏开发中，通常把 显示图像的对象 叫做精灵 Sprite  精灵需要有两个重要的属性image 要显示的图像  rect 图像要显示在屏幕的位置
        pygame.sprite.Sprite.__init__(self)
        self.name = ''
        if number == 1:
            # 定义英雄飞机的图片，两个图片切换可以实现飞机尾部的火焰效果###############################convert_alpha()
            self.image1 = pygame.image.load(
                "./7飞机/红/hero1.png").convert_alpha()
            self.image2 = pygame.image.load(
                "./7飞机/红/hero2.png").convert_alpha()
            # 定义爆炸效果，使用列表
            self.destroy_images = []
            self.destroy_images.extend([
                pygame.image.load(
                    "./7飞机/红/hero_blowup_n1.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/红/hero_blowup_n2.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/红/hero_blowup_n3.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/红/hero_blowup_n4.png").convert_alpha()
            ])
            # 定义英雄机的姓名
            self.name = 'red'

        elif number == 2:
            # 定义英雄飞机的图片，两个图片切换可以实现飞机尾部的火焰效果###############################convert_alpha()
            self.image1 = pygame.image.load(
                "./7飞机/橙/hero1.png").convert_alpha()
            self.image2 = pygame.image.load(
                "./7飞机/橙/hero2.png").convert_alpha()
            # 定义爆炸效果，使用列表
            self.destroy_images = []
            self.destroy_images.extend([
                pygame.image.load(
                    "./7飞机/橙/hero_blowup_n1.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/橙/hero_blowup_n2.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/橙/hero_blowup_n3.png").convert_alpha(),
                pygame.image.load("./7飞机/橙/hero_blowup_n4.png").convert_alpha()
            ])
            self.name = 'orange'

        elif number == 3:
            # 定义英雄飞机的图片，两个图片切换可以实现飞机尾部的火焰效果###############################convert_alpha()
            self.image1 = pygame.image.load(
                "./7飞机/黄/hero1.png").convert_alpha()
            self.image2 = pygame.image.load(
                "./7飞机/黄/hero2.png").convert_alpha()
            # 定义爆炸效果，使用列表
            self.destroy_images = []
            self.destroy_images.extend([
                pygame.image.load(
                    "./7飞机/黄/hero_blowup_n1.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/黄/hero_blowup_n2.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/黄/hero_blowup_n3.png").convert_alpha(),
                pygame.image.load("./7飞机/黄/hero_blowup_n4.png").convert_alpha()
            ])
            self.name = 'yellow'
        elif number == 4:
            # 定义英雄飞机的图片，两个图片切换可以实现飞机尾部的火焰效果###############################convert_alpha()
            self.image1 = pygame.image.load(
                "./7飞机/绿/hero1.png").convert_alpha()
            self.image2 = pygame.image.load(
                "./7飞机/绿/hero2.png").convert_alpha()
            # 定义爆炸效果，使用列表
            self.destroy_images = []
            self.destroy_images.extend([
                pygame.image.load(
                    "./7飞机/绿/hero_blowup_n1.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/绿/hero_blowup_n2.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/绿/hero_blowup_n3.png").convert_alpha(),
                pygame.image.load("./7飞机/绿/hero_blowup_n4.png").convert_alpha()
            ])
            self.name = 'green'
        elif number == 5:
            # 定义英雄飞机的图片，两个图片切换可以实现飞机尾部的火焰效果###############################convert_alpha()
            self.image1 = pygame.image.load(
                "./7飞机/青/hero1.png").convert_alpha()
            self.image2 = pygame.image.load(
                "./7飞机/青/hero2.png").convert_alpha()
            # 定义爆炸效果，使用列表
            self.destroy_images = []
            self.destroy_images.extend([
                pygame.image.load(
                    "./7飞机/青/hero_blowup_n1.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/青/hero_blowup_n2.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/青/hero_blowup_n3.png").convert_alpha(),
                pygame.image.load("./7飞机/青/hero_blowup_n4.png").convert_alpha()
            ])
            self.name = 'light_green'
        elif number == 6:
            # 定义英雄飞机的图片，两个图片切换可以实现飞机尾部的火焰效果###############################convert_alpha()
            self.image1 = pygame.image.load(
                "./7飞机/蓝/hero1.png").convert_alpha()
            self.image2 = pygame.image.load(
                "./7飞机/蓝/hero2.png").convert_alpha()
            # 定义爆炸效果，使用列表
            self.destroy_images = []
            self.destroy_images.extend([
                pygame.image.load(
                    "./7飞机/蓝/hero_blowup_n1.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/蓝/hero_blowup_n2.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/蓝/hero_blowup_n3.png").convert_alpha(),
                pygame.image.load("./7飞机/蓝/hero_blowup_n4.png").convert_alpha()
            ])
            self.name = 'blue'
        elif number == 7:
            # 定义英雄飞机的图片，两个图片切换可以实现飞机尾部的火焰效果###############################convert_alpha()
            self.image1 = pygame.image.load(
                "./7飞机/紫/hero1.png").convert_alpha()
            self.image2 = pygame.image.load(
                "./7飞机/紫/hero2.png").convert_alpha()
            # 定义爆炸效果，使用列表
            self.destroy_images = []
            self.destroy_images.extend([
                pygame.image.load(
                    "./7飞机/紫/hero_blowup_n1.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/紫/hero_blowup_n2.png").convert_alpha(),
                pygame.image.load(
                    "./7飞机/紫/hero_blowup_n3.png").convert_alpha(),
                pygame.image.load("./7飞机/紫/hero_blowup_n4.png").convert_alpha()
            ])
            self.name = 'purple'
        elif number == 8:
            # 定义英雄飞机的图片，两个图片切换可以实现飞机尾部的火焰效果###############################convert_alpha()
            self.image1 = pygame.image.load(
                "./images/hero1.png").convert_alpha()
            self.image2 = pygame.image.load(
                "./images/hero2.png").convert_alpha()
            # 定义爆炸效果，使用列表
            self.destroy_images = []
            self.destroy_images.extend([
                pygame.image.load(
                    "./images/hero_blowup_n1.png").convert_alpha(),
                pygame.image.load(
                    "./images/hero_blowup_n2.png").convert_alpha(),
                pygame.image.load(
                    "./images/hero_blowup_n3.png").convert_alpha(),
                pygame.image.load(
                    "./images/hero_blowup_n4.png").convert_alpha()
            ])
            self.name = 'black'

        # 获得英雄飞机的大小
        self.rect = self.image1.get_rect()
        # 获得屏幕大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 获得英雄左边和顶边#######################################################
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60

        # 定义英雄机的速度
        self.speed = 10

        # 定义英雄机的生命值
        self.HP = 10

        # 看英雄机是否活着
        self.active = True
        # 定义英雄机是否无敌
        self.invincible = False
        # from_surface()可以将Surface中的对象的非透明部分标志为mask并返回
        # 应用于碰撞检测，使检测更加精准############################################################
        self.mask = pygame.mask.from_surface(self.image1)

    # 向上移动
    def moveUp(self):
        if self.rect.top > 0:
            self.rect.top -= self.speed
        else:
            self.rect.top = 0

    # 向下移动
    def moveDown(self):
        if self.rect.bottom < self.height - 60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height - 60

    # 向左移动
    def moveLeft(self):
        if self.rect.left > 0:
            self.rect.left -= self.speed
        else:
            self.rect.left = 0

    # 向右移动
    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width

    # 添加重置方法$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    def reset(self):
        self.rect.left, self.rect.top = \
            (self.width - self.rect.width) // 2, \
            self.height - self.rect.height - 60
        self.active = True
        self.invincible = True


# pygame.init()
# pygame.mixer.init()


# # 初始化屏幕宽高，使用对象接收屏幕
# bg_size = width, height = 1366, 768
# screen = pygame.display.set_mode(bg_size)
# pygame.display.set_caption("飞机大战 Game")

# # 初始化背景
# background = pygame.image.load("./images/background.png").convert()

# # 用于切换图片
# switch_image = True

# # 用于延迟
# delay = 100

# # 定义游戏时钟，用于游戏刷新率
# clock = pygame.time.Clock()


# # 创建英雄飞机
# me = MyPlane(bg_size, 3)

# while True:

#     # 绘制游戏背景
#     screen.blit(background, (0, 0))
#     # 绘制我方飞机
#     if me.active:
#         if switch_image:
#             screen.blit(me.image1, me.rect)

#         else:
#             screen.blit(me.image2, me.rect)
#     else:
#         # 毁灭
#         if not (delay % 3):
#             if me_destroy_index == 0:
#                 screen.blit(me.destroy_images[me_destroy_index], me.rect)
#                 me_destroy_index = (me_destroy_index + 1) % 4
#             if me_destroy_index == 0:
#                 me.reset()
#                 # life_num -= 1
#                 pygame.time.set_timer(26, 3 * 1000)

#     # 切换图片
#     if not (delay % 5):
#         switch_image = not switch_image

#     # 使用计数器
#     delay -= 1
#     if not delay:
#         delay = 100

#     # 刷新率60帧
#     clock.tick(60)

#     # 获取点击退出事件
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             sys.exit()

#     # 检测用户的键盘操作
#     key_pressed = pygame.key.get_pressed()
#     # 获得用户输入的w键，或者 向上键
#     if key_pressed[K_w] or key_pressed[K_UP]:
#         me.moveUp()
#     # 获得用户输入的s键，或者 向下键
#     if key_pressed[K_s] or key_pressed[K_DOWN]:
#         me.moveDown()
#     # 获得用户输入的a键，或者 向左键
#     if key_pressed[K_a] or key_pressed[K_LEFT]:
#         me.moveLeft()
#     # 获得用户输入的d键，或者 向右键
#     if key_pressed[K_d] or key_pressed[K_RIGHT]:
#         me.moveRight()

#     # 刷新屏幕
#     pygame.display.update()
