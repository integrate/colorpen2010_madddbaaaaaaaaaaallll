import pygame

import model

pygame.key.set_repeat(50)


def control():
    sobitie = pygame.event.get()
    for k in sobitie:
        if k.type == pygame.QUIT:
            exit()
        if k.type == pygame.KEYDOWN and k.key == pygame.K_SPACE:
            model.igra_or_menu = 'igra'
