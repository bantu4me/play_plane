import pygame
from pygame.locals import *
import sys

from bullet import Bullet
from myplane import MyPlane
from enemy import Enermy

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


# 新增敌机
def add_enemies(enemies, num):
    for i in range(num):
        e = Enermy(bg_size)
        enemies.add(e)
    return enemies


# 初始化子弹
def add_bullets(num, position):
    bullets = []
    for i in range(num):
        b = Bullet(position)
        bullets.append(b)
    return bullets


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
    # 初始化子弹
    bullet_index = 0
    bullet_num = 5
    bullets = add_bullets(bullet_num, me.rect.midtop)

    while True:
        # 事件循环检测
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
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
        screen.blit(me.active_img, me.rect)
        # 绘制敌机
        for e in enemies:
            if e.active:
                e.move()
                screen.blit(e.image, e.rect)
            else:
                if not (delay % 3):
                    if e.destory_index == 0:
                        enemy1_down_sound.play()
                    screen.blit(e.destory_imgs[e.destory_index], e.rect)
                    e.destory_index += 1
                    if e.destory_index == 4:
                        e.reset()

        # 子弹
        for b in bullets:
            if b.active:
                b.move()
                screen.blit(b.image, b.rect)
                enemies_hit = pygame.sprite.spritecollide(b, enemies, False)
                if enemies_hit:
                    # 子弹击中目标重置位置
                    b.reset(me.rect.midtop)
                    for e in enemies_hit:
                        # 击落敌机
                        e.active = False

        # 子弹重绘
        if not (delay % 10):
            bullets[bullet_index].reset(me.rect.midtop)
            bullet_index = (bullet_index + 1) % bullet_num

        pygame.display.flip()
        # 设置一个帧数刷新率，没看懂这里的原理，官网文档设置了40，测试40有卡顿感觉
        clock.tick_busy_loop(60)


if __name__ == '__main__':
    main()
