import pygame
screen=pygame.display.set_mode([1500,1000])
while True:
    cods = pygame.event.get()

    for cosd in cods:
        if cosd.type == pygame.QUIT:
            exit()
        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_F11:
            fullscren = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)

    screen.fill([34,56,12])
    pygame.display.flip()

