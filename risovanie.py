import pygame

porgran = pygame.Rect(50, 50, 50, 50)
screen = pygame.display.set_mode([1500, 1000])
pygame.draw.rect(screen, [255, 50, 21], porgran)
import model


def hydozhnik():
    screen.fill([34, 56, 12])
    pygame.draw.ellipse(screen, [56, 98, 21], model.shar)

    pygame.draw.rect(screen, [255, 0, 0], model.stena)

    pygame.display.flip()
