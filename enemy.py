# 敌机

import pygame
from random import *


class Enermy(pygame.sprite.Sprite):
    def __init__(self, bg_size, type=1):
        pygame.sprite.Sprite.__init__(self)
        self.destory_index = 0
        self.active = True
        self.width, self.height = bg_size[0], bg_size[1]
        if type == 1:
            self.init_normal_enermy_info()
        elif type == 2:
            self.init_mid_enermy_info()
        elif type == 3:
            self.init_big_enermy_info()

    def init_normal_enermy_info(self):
        self.image = pygame.image.load('image/enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-5 * self.height, 0)
        # 坠毁效果
        self.destory_imgs = [
            pygame.image.load('image/enemy1_down1.png').convert_alpha(),
            pygame.image.load('image/enemy1_down2.png').convert_alpha(),
            pygame.image.load('image/enemy1_down3.png').convert_alpha(),
            pygame.image.load('image/enemy1_down4.png').convert_alpha()
        ]

    def init_mid_enermy_info(self):
        self.image = pygame.image.load('image/enemy2.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 2
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-10 * self.height, -self.height)
        self.destory_imgs = [
            pygame.image.load('image/enemy2_down1.png').convert_alpha(),
            pygame.image.load('image/enemy2_down2.png').convert_alpha(),
            pygame.image.load('image/enemy2_down3.png').convert_alpha(),
            pygame.image.load('image/enemy2_down4.png').convert_alpha()
        ]

    def init_big_enermy_info(self):
        pass

    def move(self):
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-5 * self.height, 0)
        self.active = True
        self.destory_index = 0


if __name__ == '__main__':
    for _ in range(10):
        print(randint(0, 10))
