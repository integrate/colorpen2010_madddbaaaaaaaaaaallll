import pygame, model

screen = pygame.display.get_surface()


def controlior():
    cods = pygame.event.get()
    for cosd in cods:
        if cosd.type == pygame.QUIT:
            exit()

        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_F11:
            model.full_screen()

        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_UP:
            model.peredeshenie_steni_verh()
        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_DOWN:
            model.peredeshenie_steni_niz()
        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_LEFT:
            model.peredeshenie_steni_levo()
        if cosd.type == pygame.KEYDOWN and cosd.key == pygame.K_RIGHT:
            model.peredeshenie_steni_pravo()
