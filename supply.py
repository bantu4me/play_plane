# -*- coding: utf-8 -*-# 
# @Time: 2018/12/17 19:37
# @Author: lijie
# @Desc:
# 补给。初始化通过随机数确定补给类型。1-双倍子弹 2-炸弹
# 补给出现策略，每三十秒钟 30%概率出现补给


import pygame
from random import randint


class Supply(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        self.speed = 5
        self.width, self.height = bg_size[0], bg_size[1]
        self.re_init()

    def re_init(self):
        supply_type = randint(0, 1)
        supply_type = 0
        self.supply_type = supply_type
        if supply_type == 0:
            self.__init_double_bullet()
        elif supply_type == 1:
            self.__init_bomb()
        self.rect = self.image.get_rect()
        self.rect.left = randint(0, self.width - self.rect.width)
        self.rect.top = randint(-3 * self.height, 0 * self.height)
        self.active = True
        pygame.mask.from_surface(self.image)

    def __init_double_bullet(self):
        self.image = pygame.image.load('image/ufo1.png').convert_alpha()

    def __init_bomb(self):
        self.image = pygame.image.load('image/ufo2.png').convert_alpha()

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.active = False



if __name__ == '__main__':
    print(randint(0, 1))
