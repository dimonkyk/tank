import pygame


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 151, 82)
        self.image = pygame.image.load("C:/Users/H P/PycharmProjects/pygamea/navarot/kartinki/plta.png")
        self.speedx = 0
        self.speedy = 0
        self.rect.left=500

    def move(self):
        self.rect.top += self.speedy
        self.rect.right += self.speedx
        if self.rect.right>1000:
            self.rect.right=1000

        if self.rect.left<0:
            self.rect.left=0

        if self.rect.bottom > 500:
            self.rect.bottom = 500

        if self.rect.top < 0:
            self.rect.top = 0
