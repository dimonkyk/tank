import pygame
class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 151, 82)
        self.image = pygame.Surface([5,5])