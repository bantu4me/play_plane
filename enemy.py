# 敌机

import pygame
from random import *


class Enermy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/enemy1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.speed = 2
        self.rect.left, self.rect.top = randint(0, self.width - self.rect.width), \
                                        randint(-5 * self.height, 0)
        # 击落为False
        self.active = True
        # 坠毁效果
        self.destory_imgs = [
            pygame.image.load('image/enemy1_down1.png').convert_alpha(),
            pygame.image.load('image/enemy1_down2.png').convert_alpha(),
            pygame.image.load('image/enemy1_down3.png').convert_alpha(),
            pygame.image.load('image/enemy1_down4.png').convert_alpha()
        ]
        self.destory_index = 0

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
