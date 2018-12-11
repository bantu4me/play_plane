import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('image/bullet1.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 12

    def move(self):
        self.rect.top -= self.speed

    def reset(self, position):
        self.rect.left, self.rect.top = position
