import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y,):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 151, 82)
        self.image = pygame.image.load("C:/Users/H P/PycharmProjects/pygamea/navarot/kartinki/plta.png")
        self.speedx = 0
        self.speedy = 0

    def move(self):
        self.rect.right += self.speedx
        self.rect.top += self.speedy

