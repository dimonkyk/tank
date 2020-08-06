import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([20, 30])
        self.rect = pygame.Rect(100, 100, 20, 30)