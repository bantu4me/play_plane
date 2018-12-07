import pygame
from pygame.locals import *
import sys
from myplane import MyPlane

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

def main():
    # 播放背景音乐
    pygame.mixer.music.play(-1)

    # 创建我的飞机
    me = MyPlane(bg_size)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        key = pygame.key.get_pressed()
        if key[K_UP]:
            me.moveUp()
        if key[K_DOWN]:
            me.moveDown()
        if key[K_LEFT]:
            me.moveLeft()
        if key[K_RIGHT]:
            me.moveRight()


        screen.blit(background, origin)
        screen.blit(me.image, me.rect)
        pygame.display.flip()
        # 设置一个帧数刷新率，没看懂这里的原理，官网文档设置了40，测试40有卡顿感觉
        clock.tick_busy_loop(60)


if __name__ == '__main__':
    main()
