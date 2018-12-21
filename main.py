import pygame
from pygame.locals import *
import sys

from bullet import Bullet
from myplane import MyPlane
from enemy import Enermy
from supply import Supply
import time

# 初始化
pygame.init()
pygame.mixer.init()
# 坐标原点
origin = (0, 0)
# 设置游戏窗口大小
bg_size = width, height = 480, 850
#
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('打飞机')
# 加载背景图片
background = pygame.image.load('image/background.png').convert()

# 加载游戏背景音乐
pygame.mixer.music.load('sound/game_music.wav')
pygame.mixer.music.set_volume(0.2)
# 子弹
bullet_sound = pygame.mixer.Sound('sound/bullet.wav')
bullet_sound.set_volume(0.2)
# 使用炸弹
boom_sound = pygame.mixer.Sound('sound/use_bomb.wav')
boom_sound.set_volume(0.2)
# 获取双倍子弹
get_bullet_sound = pygame.mixer.Sound('sound/get_double_laser.wav')
get_bullet_sound.set_volume(0.2)
# 获取炸弹
get_bomb_sound = pygame.mixer.Sound('sound/get_bomb.wav')
get_bomb_sound.set_volume(0.2)
# 初级飞机坠毁
enemy1_down_sound = pygame.mixer.Sound('sound/enemy1_down.wav')
enemy1_down_sound.set_volume(0.2)
# 中级飞机坠毁
enemy2_down_sound = pygame.mixer.Sound('sound/enemy2_down.wav')
enemy2_down_sound.set_volume(0.2)
# 高级飞机坠毁
enemy3_down_sound = pygame.mixer.Sound('sound/enemy3_down.wav')
enemy3_down_sound.set_volume(0.2)
# 高级飞机出场
enemy3_fly_sound = pygame.mixer.Sound('sound/big_spaceship_flying.wav')
enemy3_fly_sound.set_volume(0.2)
# 自己坠毁
me_down_sound = pygame.mixer.Sound('sound/game_over.wav')
me_down_sound.set_volume(0.2)
# supply
supply_sound = pygame.mixer.Sound('sound/supply.wav')
supply_sound.set_volume(0.2)

clock = pygame.time.Clock()
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# 新增敌机
def add_enemies(enemies, num, type=1):
    for i in range(num):
        e = Enermy(bg_size, type)
        enemies.add(e)
    return enemies


# 初始单发化子弹
def add_bullets(num, position, type=1, deviation=0):
    single_bullets = []
    for i in range(num):
        b = Bullet(position, type, deviation)
        single_bullets.append(b)
    return single_bullets


# 炸弹
BOMB = pygame.image.load('image/bomb.png').convert_alpha()
bomb_rect = BOMB.get_rect()
MAX_BOMB_NUM = 3
bomb_draw_height = bg_size[1] - bomb_rect.height


def main():
    # 播放背景音乐
    pygame.mixer.music.play(-1)
    # 创建我的飞机
    me = MyPlane(bg_size)
    # 动画切换标记
    switch_img = True
    # 延迟刷新控制
    delay = 5
    # 初始化敌机
    enemies = pygame.sprite.Group()
    add_enemies(enemies, 15)
    # 初始化中型敌机
    add_enemies(enemies, 10, type=2)
    # 初始化大型敌机
    add_enemies(enemies, 10, type=3)
    # 初始化子弹
    bullet_index = 0
    bullet_num = 4
    bullets = add_bullets(bullet_num, me.rect.midtop)
    # 初始化双倍子弹 左右弹道
    bullets_left = add_bullets(bullet_num, me.rect.midtop, type=2, deviation=1)
    bullets_right = add_bullets(bullet_num, me.rect.midtop, type=2, deviation=2)
    running = True
    # 绘制分数信息
    font = pygame.font.SysFont('', 35)
    score = 0
    score_info = 'Score='

    # 补给
    supply = Supply(bg_size)
    bomb_num = 0

    # 双倍子弹
    double_bullets_flag = False
    # 双倍子弹时间限制
    double_bullets_start = 0
    double_bullets_limit = 30


    while running:
        # 事件循环检测
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            # 检测按下了空格键,炸毁视野中的飞机
            space_down = pygame.key.get_pressed()
            if space_down[K_SPACE] and bomb_num > 0:
                bomb_num -= 1
                vis = 0
                for e in enemies:
                    if e.visible:
                        vis += 1
                        e.active = False

        key = pygame.key.get_pressed()
        # 方向操作
        if key[K_UP]:
            me.moveUp()
        if key[K_DOWN]:
            me.moveDown()
        if key[K_LEFT]:
            me.moveLeft()
        if key[K_RIGHT]:
            me.moveRight()

        # 控制飞机每五秒钟切换一次动画
        delay -= 1
        if not delay:
            delay = 100
        if not (delay % 5):
            switch_img = not switch_img
            me.active_flag = switch_img
        # 绘制背景
        screen.blit(background, origin)

        # 绘制我的飞机
        # 增加碰撞检测
        me_enemies_hit = pygame.sprite.spritecollide(me, enemies, False, pygame.sprite.collide_mask)
        if me_enemies_hit:
            me.active = False
            for e in me_enemies_hit:
                e.active = False
        if me.active:
            screen.blit(me.active_img, me.rect)
        else:
            me_down_sound.play()
            if not (delay % 3):
                screen.blit(me.destory_imgs[me.destory_index], me.rect)
                me.destory_index += 1
                if me.destory_index == len(me.destory_imgs):
                    me.destory_index = 0
                    me.active = True

        # 绘制敌机
        for e in enemies:
            if e.active:
                e.move()
                # 判断飞机类型绘画血条
                if e.type != 1:
                    draw_hp(screen, e)
                screen.blit(e.image, e.rect)
            else:
                if not (delay % 3):
                    if e.destory_index == 0:
                        enemy1_down_sound.play()
                    screen.blit(e.destory_imgs[e.destory_index], e.rect)
                    e.destory_index += 1
                    if e.destory_index == len(e.destory_imgs):
                        e.reset()
                        score += e.score

        if not double_bullets_flag:

            # 子弹重绘
            if not (delay % 10) and len(bullets) > 0:
                bullets[bullet_index].reset(me.rect.midtop)
                bullet_index = (bullet_index + 1) % bullet_num

            # 子弹
            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemies_hit:
                        # 子弹击中目标重置位置
                        b.reset(me.rect.midtop)
                        for e in enemies_hit:
                            # 击落敌机
                            if e.type == 1:
                                e.active = False
                            elif e.type == 2 or e.type == 3:
                                if e.hp > 0:
                                    e.hp -= 1
                                    e.is_hit = True
                                else:
                                    e.active = False
        else:
            # 子弹重绘
            if not (delay % 10):
                bullets_left[bullet_index].reset(me.rect.midtop)
                bullets_right[bullet_index].reset(me.rect.midtop)
                bullet_index = (bullet_index + 1) % bullet_num

            # 子弹
            for b, j in zip(bullets_left, bullets_right):
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemies_hit:
                        # 子弹击中目标重置位置
                        b.reset(me.rect.midtop)
                        for e in enemies_hit:
                            # 击落敌机
                            if e.type == 1:
                                e.active = False
                            elif e.type == 2 or e.type == 3:
                                if e.hp > 0:
                                    e.hp -= 1
                                    e.is_hit = True
                                else:
                                    e.active = False
                if j.active:
                    j.move()
                    screen.blit(j.image, j.rect)
                    enemies_hit = pygame.sprite.spritecollide(j, enemies, False, pygame.sprite.collide_mask)
                    if enemies_hit:
                        # 子弹击中目标重置位置
                        j.reset(me.rect.midtop)
                        for e in enemies_hit:
                            # 击落敌机
                            if e.type == 1:
                                e.active = False
                            elif e.type == 2 or e.type == 3:
                                if e.hp > 0:
                                    e.hp -= 1
                                    e.is_hit = True
                                else:
                                    e.active = False

        # 提供补给的粗略逻辑：
        # 每30秒钟以30%的概率出现一个补给
        if supply.active:
            supply.move()
            screen.blit(supply.image, supply.rect)
        else:
            supply.re_init()

        supply_get = pygame.sprite.collide_mask(me, supply)

        if supply_get:
            supply.active = False
            if supply.supply_type == 0:
                double_bullets_flag = True
                double_bullets_start = time.time()
                print(double_bullets_start)
                # 重置子弹的位置
                for b_l,b_r in zip(bullets_left,bullets_right):
                    b_l.reset(me.rect.midtop)
                    b_r.reset(me.rect.midtop)

            elif supply.supply_type == 1:
                if bomb_num < 3:
                    bomb_num += 1

        if double_bullets_flag:
            double_bullets_end = time.time()
            # 超过30秒后取消双倍子弹
            t = double_bullets_end - double_bullets_start
            if t > double_bullets_limit:
                double_bullets_flag = False
                for b in bullets:
                    b.reset(me.rect.midtop)

        draw_bomb(screen, bomb_num)

        score_sur = font.render(score_info + str(score), True, BLACK)
        screen.blit(score_sur, (10, 10))

        pygame.display.flip()
        # 设置一个帧数刷新率，没看懂这里的原理，官网文档设置了40，测试40有卡顿感觉
        clock.tick_busy_loop(60)


def draw_bomb(screen, bomb_num):
    if not bomb_num:
        return
    elif 1 <= bomb_num <= 3:
        for i in range(bomb_num):
            screen.blit(BOMB, (i * bomb_rect.width, bomb_draw_height))


def draw_hp(screen, enemy):
    start = (enemy.rect.left, enemy.rect.top - 5)
    width = enemy.hp / enemy.full_hp * (enemy.rect.width)
    end = (enemy.rect.left + width, enemy.rect.top - 5)
    color = GREEN if enemy.hp / enemy.full_hp > 0.2 else RED
    pygame.draw.line(screen, color, start, end, 2)


if __name__ == '__main__':
    main()
