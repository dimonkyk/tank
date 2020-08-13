import pygame, time, tank_player

pygame.init()
s=0
screen=pygame.display.set_mode([1000,500])
tank=tank_player.Tank(0, 209)
groopa=pygame.sprite.Group()
groopa.add(tank,)
while 1==1:
    tank.move()
    time.sleep(1/60)
    a=pygame.event.get()
    for d in a:
        if d.type==12:
            exit()
        if d.type==pygame.KEYDOWN:
            tank.speedx=1
        if d.type==pygame.KEYUP:
            tank.speedx=0
    screen.fill([s,164,231])
    if s<255:
        s+=1
    groopa.draw(screen)
    pygame.display.flip()

