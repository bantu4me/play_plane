# 敌机

import pygame
from random import *


class Enermy(pygame.sprite.Sprite):

    def __init__(self, bg_size, type=1):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 2
        self.destory_index = 0
        self.active = True
        self.width, self.height = bg_size[0], bg_size[1]
        self.type = type
        if type == 1:
            self.init_normal_enermy_info()
        elif type == 2:
            self.init_mid_enermy_info()
        elif type == 3:
            self.init_big_enermy_info()
        pygame.mask.from_surface(self.image)
        self.visible = False



    def init_normal_enermy_info(self):
        self.image = pygame.image.load('image/enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-5 * self.height, 0)
        # 坠毁效果
        self.destory_imgs = [
            pygame.image.load('image/enemy1_down1.png').convert_alpha(),
            pygame.image.load('image/enemy1_down2.png').convert_alpha(),
            pygame.image.load('image/enemy1_down3.png').convert_alpha(),
            pygame.image.load('image/enemy1_down4.png').convert_alpha()
        ]
        self.hp = self.full_hp = 1
        self.score = 10

    def init_mid_enermy_info(self):
        self.image = pygame.image.load('image/enemy2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-10 * self.height, -self.height)
        self.destory_imgs = [
            pygame.image.load('image/enemy2_down1.png').convert_alpha(),
            pygame.image.load('image/enemy2_down2.png').convert_alpha(),
            pygame.image.load('image/enemy2_down3.png').convert_alpha(),
            pygame.image.load('image/enemy2_down4.png').convert_alpha()
        ]
        self.hp = self.full_hp = 5
        self.is_hit = False
        self.hit_img = pygame.image.load('image/enemy2_hit.png').convert_alpha()
        self.score = 30

    def init_big_enermy_info(self):
        self.image = pygame.image.load('image/enemy3_n1.png').convert_alpha()
        self.image2 = pygame.image.load('image/enemy3_n2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-15 * self.height, -5 * self.height)
        self.destory_imgs = [
            pygame.image.load('image/enemy3_down1.png').convert_alpha(),
            pygame.image.load('image/enemy3_down2.png').convert_alpha(),
            pygame.image.load('image/enemy3_down3.png').convert_alpha(),
            pygame.image.load('image/enemy3_down4.png').convert_alpha(),
            pygame.image.load('image/enemy3_down5.png').convert_alpha(),
            pygame.image.load('image/enemy3_down6.png').convert_alpha()
        ]
        self.hp = self.full_hp = 10
        self.is_hit = False
        self.hit_img = pygame.image.load('image/enemy3_hit.png').convert_alpha()
        self.score = 50

    def move(self):
        if self.rect.top > 0:
            self.visible = True
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-5 * self.height, 0)
        self.active = True
        self.destory_index = 0
        # 根据type类型增加hp
        self.hp = self.full_hp
        self.visible = False

if __name__ == '__main__':
    pass
