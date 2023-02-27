import pygame

screen = pygame.display.get_surface()


def controlior():
    cods = pygame.event.get()
    for cosd in cods:
        if cosd.type == pygame.QUIT:
            exit()
        if screen.get_width() == 1500:
            if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_F11:
                fullscren = pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
        elif screen.get_width() != 1500:
            if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_F11:
                fullscren = pygame.display.set_mode([1500, 1000])
