# -*- coding: utf-8 -*-

# 主函数

from bullets import *
from daojv import *
from self_fighter import *
from enemies import *
import skills


def main_game(my_plane_num):
    '''此方法用于初始化游戏'''
    # 初始化pygame
    pygame.init()
    pygame.mixer.init()

    # 初始化屏幕尺寸
    screen_size = width, height = 1366, 768

    # 创建界面
    screen = pygame.display.set_mode(screen_size)

    # 设置标题
    pygame.display.set_caption('Fight Game')

    # 初始化背景
    bg_path = './images/background2.png'
    # background = pygame.image.load(bg_path)
    # background = pygame.transform.scale(background, screen_size)

    # 用于切换图片
    switch_image = True

    # 用于延迟
    delay = 100

    # 定义游戏时钟，用于游戏刷新频率
    clock = pygame.time.Clock()

    # 创建我方飞机
    # TODO 单机、联机待扩展，可选择创建何种飞机，初始界面提供8种飞机的样式
    global me
    # my_plane_num = 2
    me = MyPlane(screen_size, my_plane_num)
    # 创建技能对象
    skill = skills.Myskills(me.name)

    # another =

    # 全局子弹列表
    global bullets3_11
    global bullets3_l1
    global bullets3_r1
    global bullets3_r2
    global bullets2
    global bullets1

    # 生成子弹
    # 子弹类型设置
    bultype = 1
    # 生成普通子弹
    bullet1 = []
    bullet1_index = 0
    BULLET1_NUM = 4
    for i in range(BULLET1_NUM):
        bullet1.append(Bullet1(me.rect.midtop))

    # 生成独头弹
    bullet2 = []
    bullet2_index = 0
    BULLET2_NUM = 4
    for i in range(BULLET2_NUM):
        bullet2.append(Bullet2(me.rect.midtop))

    # 生成霰弹1~4
    bullet3_l1 = []
    bullet3_l1_index = 0
    BULLET3_l1_NUM = 4
    for i in range(BULLET3_l1_NUM):
        bullet3_l1.append(Bullet3_l1(me.rect.midtop))

    bullet3_r1 = []
    bullet3_r1_index = 0
    BULLET3_r1_NUM = 4
    for i in range(BULLET3_r1_NUM):
        bullet3_r1.append(Bullet3_r1(me.rect.midtop))

    bullet3_l2 = []
    bullet3_l2_index = 0
    BULLET3_l2_NUM = 4
    for i in range(BULLET3_l2_NUM):
        bullet3_l2.append(Bullet3_l2(me.rect.midtop))

    bullet3_r2 = []
    bullet3_r2_index = 0
    BULLET3_r2_NUM = 4
    for i in range(BULLET3_r2_NUM):
        bullet3_r2.append(Bullet3_r2(me.rect.midtop))

    # 生成敌机
    # 生成敌机精灵组
    enemies = pygame.sprite.Group()
    # 生成敌机小型飞机组
    small_enemies = pygame.sprite.Group()
    # 生成敌机中型飞机组
    middle_enemies = pygame.sprite.Group()
    # 生成敌机大型飞机组
    big_enemies = pygame.sprite.Group()
    # 添加敌机进组
    add_small_enemies(small_enemies, enemies, 15, screen_size)
    add_middle_enemies(middle_enemies, enemies, 15, screen_size)
    add_big_enemies(big_enemies, enemies, 15, screen_size)

    # 生成道具
    # 生成道具精灵组
    daojvs = pygame.sprite.Group()
    # 生成第一种道具组
    daojv1 = pygame.sprite.Group()
    # 生成第二种道具组
    daojv2 = pygame.sprite.Group()
    # 生成第三种道具组
    daojv3 = pygame.sprite.Group()
    # 添加道具进组
    add_daojv1(daojv1, daojvs, 1, screen_size)
    add_daojv2(daojv2, daojvs, 1, screen_size)
    add_daojv3(daojv3, daojvs, 1, screen_size)

    # 中弹图片索引
    me_destroy_index = 0
    e1_destroy_index = 0

    # 统计得分
    score = 0
    score_font = pygame.font.Font("font/AquaKana.ttc", 36)

    # 设置基础颜色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)

    # 生命数量
    life_image = pygame.image.load("./images/plane.png").convert_alpha()
    life_rect = life_image.get_rect()
    life_num = 4

    # 添加游戏音乐
    pygame.mixer.music.load("sound/game_music.ogg")
    pygame.mixer.music.set_volume(0.2)

    pygame.mixer.music.play(-1)

    # 游戏结束画面
    gameover_font = pygame.font.Font("font/AquaKana.ttc", 48)
    again_image = pygame.image.load("./images/restart_nor.png").convert_alpha()
    again_rect = again_image.get_rect()
    gameover_image = pygame.image.load("./images/quit_nor.png").convert_alpha()
    gameover_rect = gameover_image.get_rect()

    # 用于阻止重复打开记录文件
    recorded = False

    # 游戏结束Flag
    gameover_flag = False

    # 主循环
    while True:
        # 绘制游戏背景
        # screen.blit(background, (0, 0))
        screen.fill((255, 255, 255))

        if not gameover_flag:

            # 绘制道具
            for DJ1 in daojv1:
                if DJ1.active:
                    DJ1.move()
                    screen.blit(DJ1.image, DJ1.rect)
                else:
                    # 毁灭
                    DJ1.reset()
            for DJ2 in daojv2:
                if DJ2.active:
                    DJ2.move()
                    screen.blit(DJ2.image, DJ2.rect)
                else:
                    # 毁灭
                    DJ2.reset()
            for DJ3 in daojv3:
                if DJ3.active:
                    DJ3.move()
                    screen.blit(DJ3.image, DJ3.rect)
                else:
                    # 毁灭
                    DJ3.reset()

            # 绘制小型敌机：
            for each in small_enemies:
                if each.active:
                    # 移动判定
                    if skill.move:
                        each.move(me)
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if not (delay % 3):
                        screen.blit(
                            each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()

                        # 技能值+1
                        if skill.power != 3:
                            skill.power += 1

            # 绘制中型敌机：
            for each in middle_enemies:
                if each.active:
                    # 移动判定
                    if skill.move:
                        each.move()
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if not (delay % 3):
                        screen.blit(
                            each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()

            # 绘制大型敌机：
            for each in big_enemies:
                if each.active:
                    # 移动判定
                    if skill.move:
                        each.move()
                    screen.blit(each.image, each.rect)
                else:
                    # 毁灭
                    if not (delay % 3):
                        screen.blit(
                            each.destroy_images[e1_destroy_index], each.rect)
                        e1_destroy_index = (e1_destroy_index + 1) % 4
                        if e1_destroy_index == 0:
                            score += 1000
                            each.reset()

            # 绘制我方飞机
            if me.active:
                if switch_image:
                    screen.blit(me.image1, me.rect)
                else:
                    screen.blit(me.image2, me.rect)
            else:
                # 毁灭
                if not (delay % 3):
                    # if me_destroy_index == 0:
                    screen.blit(me.destroy_images[me_destroy_index], me.rect)
                    me_destroy_index = (me_destroy_index + 1) % 4
                    if me_destroy_index == 0:
                        me.reset()
                        life_num -= 1
                        pygame.time.set_timer(26, 3 * 1000)

                        # 技能子弹判定
                        skill.judge = False
                        skill.bullet = True

                    # 技能判定参数重置
                    skill.judge = False
                    skill.power = 0

            # 设置子弹类型1
            if not (delay % 10):
                bullets1 = bullet1
                bullets1[bullet1_index].reset(
                    ((me.rect.midtop[0] - 3), me.rect.midtop[1]))
                bullet1_index = (bullet1_index + 1) % BULLET1_NUM
            # 设置子弹类型2
            if not (delay % 20):
                bullets2 = bullet2
                bullets2[bullet2_index].reset(
                    ((me.rect.midtop[0] - 30), me.rect.midtop[1]))
                bullet2_index = (bullet2_index + 1) % BULLET2_NUM
            # 设置子弹类型3_l1
            if not (delay % 10):
                bullets3_l1 = bullet3_l1
                bullets3_l1[bullet3_l1_index].reset(
                    ((me.rect.midtop[0] - 9), me.rect.midtop[1]))
                bullet3_l1_index = (bullet3_l1_index + 1) % BULLET3_l1_NUM
            # 设置子弹类型3_r1
            if not (delay % 10):
                bullets3_r1 = bullet3_r1
                bullets3_r1[bullet3_r1_index].reset(
                    ((me.rect.midtop[0] - 9), me.rect.midtop[1]))
                bullet3_r1_index = (bullet3_r1_index + 1) % BULLET3_r1_NUM
            # 设置子弹类型3_l2
            if not (delay % 10):
                bullets3_l2 = bullet3_l2
                bullets3_l2[bullet3_l2_index].reset(
                    ((me.rect.midtop[0] - 9), me.rect.midtop[1]))
                bullet3_l2_index = (bullet3_l2_index + 1) % BULLET3_l2_NUM
            # 设置子弹类型3_r2
            if not (delay % 10):
                bullets3_r2 = bullet3_r2
                bullets3_r2[bullet3_r2_index].reset(
                    ((me.rect.midtop[0] - 9), me.rect.midtop[1]))
                bullet3_r2_index = (bullet3_r2_index + 1) % BULLET3_r2_NUM

            # 检测子弹类型，并复活子弹
            if bultype == 1:
                # 发射类型1
                for b in bullets1:
                    if b.active and skill.bullet:
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(
                            b, enemies, False, pygame.sprite.collide_mask)
                        if enemy_hit:
                            b.active = False
                            for e in enemy_hit:
                                e.hp -= b.damage
                                if e.hp <= 0:
                                    e.active = False
            elif bultype == 2:
                # 发射类型2
                for b in bullets2:
                    if b.active and skill.bullet:
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(
                            b, enemies, False, pygame.sprite.collide_mask)
                        if enemy_hit:
                            b.active = False
                            for e in enemy_hit:
                                e.hp -= b.damage
                                if e.hp <= 0:
                                    e.active = False
            elif bultype == 3:
                # 发射类型3l1
                for b in bullets3_l1:
                    if b.active and skill.bullet:
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(
                            b, enemies, False, pygame.sprite.collide_mask)
                        if enemy_hit:
                            b.active = False
                            for e in enemy_hit:
                                e.hp -= b.damage
                                if e.hp <= 0:
                                    e.active = False
                # 发射类型3r1
                for b in bullets3_r1:
                    if b.active and skill.bullet:
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(
                            b, enemies, False, pygame.sprite.collide_mask)
                        if enemy_hit:
                            b.active = False
                            for e in enemy_hit:
                                e.hp -= b.damage
                                if e.hp <= 0:
                                    e.active = False
                # 发射类型3l2
                for b in bullets3_l2:
                    if b.active and skill.bullet:
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(
                            b, enemies, False, pygame.sprite.collide_mask)
                        if enemy_hit:
                            b.active = False
                            for e in enemy_hit:
                                e.hp -= b.damage
                                if e.hp <= 0:
                                    e.active = False
                # 发射类型3r2
                for b in bullets3_r2:
                    if b.active and skill.bullet:
                        b.move()
                        screen.blit(b.image, b.rect)
                        enemy_hit = pygame.sprite.spritecollide(
                            b, enemies, False, pygame.sprite.collide_mask)
                        if enemy_hit:
                            b.active = False
                            for e in enemy_hit:
                                e.hp -= b.damage
                                if e.hp <= 0:
                                    e.active = False

            # 检测我方飞机是否被撞
            enemies_down = pygame.sprite.spritecollide(
                me, enemies, False, pygame.sprite.collide_mask)
            if enemies_down:
                me.active = False
                # 技能状态
                skill.power = 0
                skill.judge = 0
                skill.bullet = True
                for e in enemies_down:
                    bultype = 1
                    e.active = False

            # 检测道具是否被吃
            DAOJV1_down = pygame.sprite.spritecollide(
                me, daojv1, False, pygame.sprite.collide_mask)
            if DAOJV1_down:
                bultype = 3
                for d in DAOJV1_down:
                    d.active = False
            DAOJV2_down = pygame.sprite.spritecollide(
                me, daojv2, False, pygame.sprite.collide_mask)
            if DAOJV2_down:
                bultype = 2
                for d in DAOJV2_down:
                    d.active = False
            DAOJV3_down = pygame.sprite.spritecollide(
                me, daojv3, False, pygame.sprite.collide_mask)
            if DAOJV3_down:
                life_num += 1
                for d in DAOJV3_down:
                    d.active = False
        # 绘制得分
        score_text = score_font.render("Score : %s" % str(score), True, GREEN)
        screen.blit(score_text, (10, 5))

        # 绘制剩余生命数量
        if life_num:
            for i in range(life_num):
                screen.blit(life_image,
                            (width - 10 - (i + 1) * life_rect.width,
                             height - 10 - life_rect.height))
        # 当英雄生命为0时，绘制游戏结束画面
        else:
            # 添加游戏结束标志
            gameover_flag = True

            # 背景音乐停止
            pygame.mixer.music.stop()

            # 停止全部音效
            pygame.mixer.stop()

            pygame.time.set_timer(30, 0)
            if not recorded:
                recorded = True
                # 读取历史最高得分
                with open("record.txt", "r") as f:
                    record_score = int(f.read())

                # 如果玩家得分高于历史最高得分，则存档
                if score > record_score:
                    with open("record.txt", "w") as f:
                        f.write(str(score))

            # 绘制结束画面
            record_score_text = score_font.render(
                "Best : %d" % record_score, True, (255, 255, 255))
            screen.blit(record_score_text, (50, 50))

            gameover_text1 = gameover_font.render(
                "Your Score", True, (255, 255, 255))
            gameover_text1_rect = gameover_text1.get_rect()
            gameover_text1_rect.left, gameover_text1_rect.top = \
                (width - gameover_text1_rect.width) // 2, height // 3
            screen.blit(gameover_text1, gameover_text1_rect)

            gameover_text2 = gameover_font.render(
                str(score), True, (255, 255, 255))
            gameover_text2_rect = gameover_text2.get_rect()
            gameover_text2_rect.left, gameover_text2_rect.top = \
                (width - gameover_text2_rect.width) // 2, \
                gameover_text1_rect.bottom + 10
            screen.blit(gameover_text2, gameover_text2_rect)

            again_rect.left, again_rect.top = \
                (width - again_rect.width) // 2, \
                gameover_text2_rect.bottom + 50
            screen.blit(again_image, again_rect)

            gameover_rect.left, gameover_rect.top = \
                (width - again_rect.width) // 2, \
                again_rect.bottom + 10
            screen.blit(gameover_image, gameover_rect)

            # 检测用户的鼠标操作
            # 如果用户按下鼠标左键
            if pygame.mouse.get_pressed()[0]:
                # 获取鼠标坐标
                pos = pygame.mouse.get_pos()
                # 如果用户点击“重新开始”
                if again_rect.left < pos[0] < again_rect.right and \
                        again_rect.top < pos[1] < again_rect.bottom:
                    # 调用main函数，重新开始游戏
                    pygame.mixer.init()
                    pygame.mixer.music.play(-1)
                    life_num = 3
                    score = 0
                    # 重新开始技能判定
                    skill.judge = False
                    skill.power = 0
                    # 子弹判定
                    # skill.bullet = True
                    # 重置敌机
                    for each in small_enemies:
                        each.reset()
                    for each in middle_enemies:
                        each.reset()
                    for each in big_enemies:
                        each.reset()
                    # 游戏重新开始
                    gameover_flag = not gameover_flag

                # 如果用户点击“结束游戏”
                elif gameover_rect.left < pos[0] < gameover_rect.right and \
                        gameover_rect.top < pos[1] < gameover_rect.bottom:
                    # 退出游戏
                    pygame.quit()
                    sys.exit()
        # 切换图片
        if not (delay % 5):
            switch_image = not switch_image

        # 使用计数器
        delay -= 1
        if not delay:
            delay = 100

        # 刷新率60帧
        clock.tick(100)

        # 获取点击退出事件
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        # 检测用户的键盘操作
        key_pressed = pygame.key.get_pressed()
        # 获得用户输入的w键，或者 向上键
        if (key_pressed[K_w] or key_pressed[K_UP]) and skill.my_move1:
            me.moveUp()
        # 获得用户输入的s键，或者 向下键
        if (key_pressed[K_s] or key_pressed[K_DOWN]) and skill.my_move2:
            me.moveDown()
        # 获得用户输入的a键，或者 向左键
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.moveLeft()
        # 获得用户输入的d键，或者 向右键
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.moveRight()

        # 技能
        if skill.skill_status():
            if skill.me != 'black':
                pygame.draw.circle(screen, (209, 64, 43), (me.rect.centerx, me.rect.centery), 12, 0)
            if key_pressed[K_q]:
                # 技能判定
                skill.judge = True

        # black
        if skill.me == 'red' and skill.judge and not gameover_flag:
            pass
        # red
        if skill.me == 'red' and skill.judge and not gameover_flag:
            skill.red_skill_way(delay, me.rect.midtop)
            # 绘制效果
            screen.blit(skill.red_skill, skill.rect)
            # 碰撞检测
            enemy_hit = pygame.sprite.spritecollide(skill, enemies, False, pygame.sprite.collide_mask)
            if enemy_hit:
                for e in enemy_hit:
                    e.active = False

        # orange
        if skill.me == 'orange' and skill.judge and not gameover_flag:
            skill.orange_skill_way(delay, me.rect.midtop)
            # 绘制效果
            screen.blit(skill.orange_skill, skill.rect)
            # 碰撞检测
            enemy_hit = pygame.sprite.spritecollide(skill, enemies, False, pygame.sprite.collide_mask)
            if enemy_hit:
                for e in enemy_hit:
                    e.active = False

        # yellow
        if skill.me == 'yellow' and skill.judge and not gameover_flag:
            skill.yellow_skill_way(delay)
            # 绘制效果
            # screen.blit(skill.yellow_skill, skill.rect)
        # green
        if skill.me == 'green' and skill.judge and not gameover_flag:
            life_num += 1
            skill.green_skill_way()

        # light_green
        if skill.me == 'light_green' and skill.judge and not gameover_flag:
            skill.light_green_skill_way(delay, me)
            # 绘制效果
            screen.blit(skill.light_green_skill, skill.rect)
            # 碰撞检测
            enemy_hit = pygame.sprite.spritecollide(skill, enemies, False, pygame.sprite.collide_mask)
            if enemy_hit:
                for e in enemy_hit:
                    e.active = False

        # blue
        if skill.me == 'blue' and skill.judge and not gameover_flag:
            skill.blue_skill_way(delay, me)
            # 绘制效果
            pygame.draw.circle(screen, (0, 0, 255), (me.rect.centerx, me.rect.centery), 60, 1)
            # 碰撞检测
            enemy_hit = pygame.sprite.spritecollide(skill, enemies, False, pygame.sprite.collide_mask)
            if enemy_hit:
                for e in enemy_hit:
                    e.active = False

        # purple
        if skill.me == 'purple' and skill.judge and not gameover_flag:
            # 绘制效果
            pass
            # 碰撞检测
            for e in enemies:
                e.active = False
            # 结束
            skill.purple_skill_way()

        # 刷新屏幕
        pygame.display.update()
