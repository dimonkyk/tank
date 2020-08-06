import pygame, tank

# создаем игру и окно
pygame.init()
pygame.mixer.init()  # для звука
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("SurvivalTest")
clock = pygame.time.Clock()
group_sprite = pygame.sprite.Group()

p = tank.Tank()
group_sprite.add(p)


# Цикл игры
running = True
while running:
    clock.tick(60)

    # Ввод процесса (события)
    new_events = pygame.event.get()
    for event in new_events:

        # проверить закрытие окна
        if event.type == pygame.QUIT:
            running = False

    screen.fill((10, 50, 100))
    group_sprite.draw(screen)

    # После отрисовки всего, переворачиваем экран
    pygame.display.flip()
