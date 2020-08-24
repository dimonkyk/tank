import pygame, options


class Tank(pygame.sprite.Sprite):
    def __init__(self, x, y, ):
        pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(x, y, 151, 82)
        self.image = pygame.image.load("navarot/kartinki/plta.png")
        self.speedx = 0
        self.speedy = 0
        self.rect.left=500

    def move(self):
        self.rect.top += self.speedy
        self.rect.right += self.speedx
        if self.rect.right>options.SCREEN_X:
            self.rect.right=options.SCREEN_X

        if self.rect.left<0:
            self.rect.left=0

        if self.rect.bottom > options.SCREEN_Y:
            self.rect.bottom = options.SCREEN_Y

        if self.rect.top < 0:
            self.rect.top = 0
