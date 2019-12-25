import pygame
from random import randint
from math import *


# 小型敌机类
class SmallEnemy(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, bg_size):
        # 调用父类方法
        pygame.sprite.Sprite.__init__(self)
        # 定义图片
        self.image = pygame.image.load("./images/enemy0.png").convert_alpha()
        # 定义爆炸效果图
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("./images/enemy0_down1.png").convert_alpha(),
            pygame.image.load("./images/enemy0_down2.png").convert_alpha(),
            pygame.image.load("./images/enemy0_down3.png").convert_alpha(),
            pygame.image.load("./images/enemy0_down4.png").convert_alpha()
        ])
        # 从图片获取大小
        self.rect = self.image.get_rect()
        # 获得屏幕大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 定义速度2
        self.speed = 2
        # 定义血量
        self.hp = 1
        # 定义是否活着
        self.active = True
        # 设置位置
        self.rect.left, self.rect.top = \
            randint(1, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        # from_surface()可以将Surface中的对象的非透明部分标志为mask并返回
        # 应用于碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

    # 敌机小飞机移动方法
    def vertical_move(self):
        # 当小飞机未移动出屏幕时
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()
    # 敌机飞机的特技移动方法，直接撞机
    def move(self, plane):
        # 当小飞机未移动出屏幕时
        if self.rect.top <= self.height:
            # 如果敌机在上面就让它去撞机
            if self.rect.centery < plane.rect.centery:
                x = plane.rect.centerx - self.rect.centerx
                y = plane.rect.centery - self.rect.centery
                a = atan(x / y)
                speed_x = 1.2*self.speed * sin(a)
                speed_y = 1.2*self.speed * cos(a)
                self.rect.centery += speed_y
                self.rect.centerx += speed_x
                # 如果敌机到了我方飞机的下面就让他自己垂直往下
            elif self.rect.centery >= plane.rect.centery:
                self.vertical_move()
        else:
            self.reset()

    # 重置敌机方法

    def reset(self):
        self.active = True
        self.hp = 1
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)

############################################################################

# 中型敌机类


class MiddleEnemy(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, bg_size):
        # 调用父类方法
        pygame.sprite.Sprite.__init__(self)
        # 定义图片
        self.image = pygame.image.load("./images/enemy1.png").convert_alpha()
        # 定义爆炸效果图
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("./images/enemy1_down1.png").convert_alpha(),
            pygame.image.load("./images/enemy1_down2.png").convert_alpha(),
            pygame.image.load("./images/enemy1_down3.png").convert_alpha(),
            pygame.image.load("./images/enemy1_down4.png").convert_alpha()
        ])
        # 从图片获取大小
        self.rect = self.image.get_rect()
        # 获得屏幕大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 定义速度2
        self.speed = 2
        # 定义血量
        self.hp = 3
        # 定义是否活着
        self.active = True
        # 设置位置
        self.rect.left, self.rect.top = \
            randint(1, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        # from_surface()可以将Surface中的对象的非透明部分标志为mask并返回
        # 应用于碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

    # 敌机中型飞机移动方法
    def move(self):
        # 当中型飞机未移动出屏幕时
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    # 重置敌机方法
    def reset(self):
        self.active = True
        self.hp = 3
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)

#######################################
# 大型敌机类


class BigEnemy(pygame.sprite.Sprite):
    # 初始化
    def __init__(self, bg_size):
        # 调用父类方法
        pygame.sprite.Sprite.__init__(self)
        # 定义图片
        self.image = pygame.image.load("./images/enemy2.png").convert_alpha()
        # 定义爆炸效果图
        self.destroy_images = []
        self.destroy_images.extend([
            pygame.image.load("./images/enemy2_down1.png").convert_alpha(),
            pygame.image.load("./images/enemy2_down2.png").convert_alpha(),
            pygame.image.load("./images/enemy2_down3.png").convert_alpha(),
            pygame.image.load("./images/enemy2_down4.png").convert_alpha()
        ])
        # 从图片获取大小
        self.rect = self.image.get_rect()
        # 获得屏幕大小
        self.width, self.height = bg_size[0], bg_size[1]
        # 定义速度2
        self.speed = 1
        # 定义血量
        self.hp = 6
        # 定义是否活着
        self.active = True
        # 设置位置
        self.rect.left, self.rect.top = \
            randint(1, self.width - self.rect.width), \
            randint(-5 * self.height, 0)
        # from_surface()可以将Surface中的对象的非透明部分标志为mask并返回
        # 应用于碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        '''敌机小飞机移动方法'''
        # 当小飞机未移动出屏幕时
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        '''重置敌机方法'''
        self.active = True
        self.hp = 6
        self.rect.left, self.rect.top = \
            randint(0, self.width - self.rect.width), \
            randint(-5 * self.height, 0)


def add_small_enemies(group1, group2, num, screen_size):
    '''添加小型敌机方法'''
    for i in range(num):
        e1 = SmallEnemy(screen_size)
        group1.add(e1)
        group2.add(e1)


def add_middle_enemies(group1, group2, num, screen_size):
    '''添加中型敌机方法'''
    for i in range(num):
        e1 = MiddleEnemy(screen_size)
        group1.add(e1)
        group2.add(e1)


def add_big_enemies(group1, group2, num, screen_size):
    '''添加大型敌机方法'''
    for i in range(num):
        e1 = BigEnemy(screen_size)
        group1.add(e1)
        group2.add(e1)
