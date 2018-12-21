import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position, type=1, deviation=0):
        pygame.sprite.Sprite.__init__(self)
        self.type = type
        self.deviation = deviation
        if type == 1:
            self.image = pygame.image.load('image/bullet1.png').convert_alpha()
        elif type == 2:
            self.image = pygame.image.load('image/bullet2.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        if type == 2:
            if deviation == 1:
                self.rect.left -= 10
            elif deviation == 2:
                self.rect.left += 10
        self.speed = 11
        # 子弹碰撞即为false
        self.active = True
        pygame.mask.from_surface(self.image)

    def move(self):
        self.rect.top -= self.speed

    def reset(self, position):
        self.rect.left, self.rect.top = position
        if self.type == 2:
            if self.deviation == 1:
                self.rect.left -= 10
            elif self.deviation == 2:
                self.rect.left += 10
