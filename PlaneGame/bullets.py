import pygame

# position为传入飞机位置

# 子弹类1


class Bullet1(pygame.sprite.Sprite):
    def __init__(self, position):
        # 调用父类初始化方法
        pygame.sprite.Sprite.__init__(self)

        # 获取初始化图片
        self.image = pygame.image.load("./images/bullet1.png").convert_alpha()

        # 获取图片大小
        self.rect = self.image.get_rect()

        # 获取子弹位置数据
        self.rect.left, self.rect.top = position

        # 指定速度
        self.speed = 20

        # 子弹默认不发射
        self.active = False

        # from_surface()可以将Surface中对象的，非透明部分标志为mask并返回
        # 应用与碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

        # 子弹伤害
        self.damage = 1

    # 移动方法
    def move(self):
        # 移动
        self.rect.top -= self.speed

        # 移出屏幕时，设置不活动，之后由精灵组管理
        if self.rect.top < 0:
            self.active = False

    # 重置方法
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
# 子弹类2独头弹


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, position):
        # 调用父类初始化方法
        pygame.sprite.Sprite.__init__(self)

        # 获取初始化图片
        self.image = pygame.image.load("images/bullet2.png").convert_alpha()

        # 获取图片大小
        self.rect = self.image.get_rect()

        # 获取子弹位置数据
        self.rect.left, self.rect.top = position

        # 指定速度
        self.speed = 9

        # 子弹默认不发射
        self.active = False

        # from_surface()可以将Surface中对象的，非透明部分标志为mask并返回
        # 应用与碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

        # 子弹伤害
        self.damage = 3

    # 移动方法
    def move(self):
        # 移动
        self.rect.top -= self.speed

        # 移出屏幕时，设置不活动，之后由精灵组管理
        if self.rect.top < 0:
            self.active = False

    # 重置方法
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True

    # 射出子弹
# 子弹类3霰弹


class Bullet3_l1(pygame.sprite.Sprite):
    def __init__(self, position):
        # 调用父类初始化方法
        pygame.sprite.Sprite.__init__(self)

        # 获取初始化图片
        self.image = pygame.image.load("images/bullet3.png").convert_alpha()

        # 获取图片大小
        self.rect = self.image.get_rect()

        # 获取子弹位置数据
        self.rect.left, self.rect.top = position

        # 指定速度
        self.speed_y = 12
        self.speed_x = 1

        # 子弹默认不发射
        self.active = False

        # from_surface()可以将Surface中对象的，非透明部分标志为mask并返回
        # 应用与碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

        # 子弹伤害
        self.damage = 2

    # 移动方法
    def move(self):
        # 移动
        self.rect.top -= self.speed_y
        self.rect.left -= self.speed_x

        # 移出屏幕时，设置不活动，之后由精灵组管理
        if self.rect.top < 0:
            self.active = False

    # 重置方法
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Bullet3_l2(pygame.sprite.Sprite):
    def __init__(self, position):
        # 调用父类初始化方法
        pygame.sprite.Sprite.__init__(self)

        # 获取初始化图片
        self.image = pygame.image.load("images/bullet3.png").convert_alpha()

        # 获取图片大小
        self.rect = self.image.get_rect()

        # 获取子弹位置数据
        self.rect.left, self.rect.top = position

        # 指定速度
        self.speed_y = 12
        self.speed_x = 3

        # 子弹默认不发射
        self.active = False

        # from_surface()可以将Surface中对象的，非透明部分标志为mask并返回
        # 应用与碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

        # 子弹伤害
        self.damage = 2

    # 移动方法
    def move(self):
        # 移动
        self.rect.top -= self.speed_y
        self.rect.left -= self.speed_x

        # 移出屏幕时，设置不活动，之后由精灵组管理
        if self.rect.top < 0:
            self.active = False

    # 重置方法
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Bullet3_r1(pygame.sprite.Sprite):
    def __init__(self, position):
        # 调用父类初始化方法
        pygame.sprite.Sprite.__init__(self)

        # 获取初始化图片
        self.image = pygame.image.load("images/bullet3.png").convert_alpha()

        # 获取图片大小
        self.rect = self.image.get_rect()

        # 获取子弹位置数据
        self.rect.left, self.rect.top = position

        # 指定速度
        self.speed_y = 12
        self.speed_x = 1

        # 子弹默认不发射
        self.active = False

        # from_surface()可以将Surface中对象的，非透明部分标志为mask并返回
        # 应用与碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

        # 子弹伤害
        self.damage = 2

    # 移动方法
    def move(self):
        # 移动
        self.rect.top -= self.speed_y
        self.rect.left += self.speed_x

        # 移出屏幕时，设置不活动，之后由精灵组管理
        if self.rect.top < 0:
            self.active = False

    # 重置方法
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True


class Bullet3_r2(pygame.sprite.Sprite):
    def __init__(self, position):
        # 调用父类初始化方法
        pygame.sprite.Sprite.__init__(self)

        # 获取初始化图片
        self.image = pygame.image.load("images/bullet3.png").convert_alpha()

        # 获取图片大小
        self.rect = self.image.get_rect()

        # 获取子弹位置数据
        self.rect.left, self.rect.top = position

        # 指定速度
        self.speed_y = 12
        self.speed_x = 3

        # 子弹默认不发射
        self.active = False

        # from_surface()可以将Surface中对象的，非透明部分标志为mask并返回
        # 应用与碰撞检测，使检测更加精准
        self.mask = pygame.mask.from_surface(self.image)

        # 子弹伤害
        self.damage = 2

    # 移动方法
    def move(self):
        # 移动
        self.rect.top -= self.speed_y
        self.rect.left += self.speed_x

        # 移出屏幕时，设置不活动，之后由精灵组管理
        if self.rect.top < 0:
            self.active = False

    # 重置方法
    def reset(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
