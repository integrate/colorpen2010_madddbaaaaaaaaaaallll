import pygame, model

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

        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_UP:
            model.stena = pygame.Rect(0, 0, screen.get_width(), 150)
            model.storona = 'verh'
        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_DOWN:
            model.stena = pygame.Rect(0, screen.get_height() - 150, screen.get_width(), 150)
            model.storona = 'niz'
        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_LEFT:
            model.stena = pygame.Rect(0, 0, 150, screen.get_height())
            model.storona = 'levo'
        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_RIGHT:
            model.stena = pygame.Rect(screen.get_width() - 150, 0, 150, screen.get_height())
            model.storona = 'pravo'
