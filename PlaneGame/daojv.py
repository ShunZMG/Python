import pygame
from random import *


class Daojv1(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, bg_size):
        # 调用父类方法
        pygame.sprite.Sprite.__init__(self)
        # 定义图片
        self.image = pygame.image.load("./images/daojv1.png").convert_alpha()
        # 从图片获取大小
        self.rect = self.image.get_rect()
        # 获得屏幕大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 定义速度2
        self.speed = 1
        # 定义是否活着
        self.active = True
        # 设置位置
        self.rect.left, self.rect.top = \
            randint(1, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        # from_surface()可以将Surface中的对象的非透明部分标志为mask并返回
        # 应用于碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

    # 敌机道具移动方法
    def move(self):
        # 当道具未移动出屏幕时
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # 重置道具方法
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)


class Daojv2(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, bg_size):
        # 调用父类方法
        pygame.sprite.Sprite.__init__(self)
        # 定义图片
        self.image = pygame.image.load("./images/daojv2.png").convert_alpha()
        # 从图片获取大小
        self.rect = self.image.get_rect()
        # 获得屏幕大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 定义速度2
        self.speed = 1
        # 定义是否活着
        self.active = True
        # 设置位置
        self.rect.left, self.rect.top = \
            randint(1, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        # from_surface()可以将Surface中的对象的非透明部分标志为mask并返回
        # 应用于碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

    # 敌机道具移动方法
    def move(self):
        # 当道具未移动出屏幕时
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # 重置道具方法
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)


class Daojv3(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, bg_size):
        # 调用父类方法
        pygame.sprite.Sprite.__init__(self)
        # 定义图片
        self.image = pygame.image.load("./images/daojv3.png").convert_alpha()
        # 从图片获取大小
        self.rect = self.image.get_rect()
        # 获得屏幕大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 定义速度2
        self.speed = 1
        # 定义是否活着
        self.active = True
        # 设置位置
        self.rect.left, self.rect.top = \
            randint(1, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        # from_surface()可以将Surface中的对象的非透明部分标志为mask并返回
        # 应用于碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

    # 敌机道具移动方法
    def move(self):
        # 当道具未移动出屏幕时
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # 重置道具方法
    def reset(self):
        self.active = True
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)


def add_daojv1(group1, group2, num, screen_size):
    '''添加第一种道具'''
    for i in range(num):
        e1 = Daojv1(screen_size)
        group1.add(e1)
        group2.add(e1)


def add_daojv2(group1, group2, num, screen_size):
    '''添加第二种道具'''
    for i in range(num):
        e1 = Daojv2(screen_size)
        group1.add(e1)
        group2.add(e1)


def add_daojv3(group1, group2, num, screen_size):
    '''添加第三种道具'''
    for i in range(num):
        e1 = Daojv3(screen_size)
        group1.add(e1)
        group2.add(e1)
