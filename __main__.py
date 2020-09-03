import pygame, time, tank_player, options, ball

pygame.init()
shr=pygame.font.SysFont("arial",10,True)
clock=pygame.time.Clock()
tims=-3000
s = 0
screen = pygame.display.set_mode([options.SCREEN_X,options.SCREEN_Y])
tank = tank_player.Tank(0, 209)
groopa = pygame.sprite.Group()
groopa.add(tank)
while 1 == 1:
    tank.move()
    clock.tick(60)
    a = pygame.event.get()
    for d in a:
        if d.type == 12:
            exit()
        if d.type == pygame.KEYDOWN and d.key == pygame.K_RIGHT:
            tank.speedx = 1
            tank.speedy = 0
        if d.type == pygame.KEYUP and d.key == pygame.K_RIGHT:
            tank.speedx = 0
        if d.type == pygame.KEYDOWN and d.key == pygame.K_LEFT:
            tank.speedx = -1
            tank.speedy = 0
        if d.type == pygame.KEYUP and d.key == pygame.K_LEFT:
            tank.speedx = 0

        if d.type == pygame.KEYDOWN and d.key == pygame.K_DOWN:
            tank.speedy = 1
            tank.speedx = 0
        if d.type == pygame.KEYUP and d.key == pygame.K_DOWN:
            tank.speedy = 0
        if d.type == pygame.KEYDOWN and d.key == pygame.K_UP:
            tank.speedy = -1
            tank.speedx = 0
        if d.type == pygame.KEYUP and d.key == pygame.K_UP:
            tank.speedy = 0

        vrem = pygame.time.get_ticks()
        rasn = vrem - tims
        if d.type == pygame.KEYDOWN and d.key == pygame.K_SPACE:
            if rasn>=3000:
                tims = pygame.time.get_ticks()
                ballpy = ball.Ball(tank.rect.right, tank.rect.centery - 2)
                groopa.add(ballpy)

    groopa.update()

    screen.fill([s, 164, 231])
    if s < 255:
        s += 1

    i=clock.get_fps()
    i=str(i)
    fps=shr.render(i,False,[0,0,0])
    screen.blit(fps,[0,0])

    groopa.draw(screen)
    pygame.display.flip()
