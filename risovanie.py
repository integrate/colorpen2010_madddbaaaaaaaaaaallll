import pygame

pygame.init()

porgran = pygame.Rect(50, 50, 50, 50)
screen = pygame.display.set_mode([1500, 1000])
pygame.draw.rect(screen, [255, 50, 21], porgran)
import model

f = pygame.font.SysFont('arial', 100, True, True)


def hydozhnik():
    screen.fill([34, 56, 12])
    pygame.draw.ellipse(screen, [56, 98, 21], model.shar)

    pygame.draw.rect(screen, [255, 0, 0], model.stena)

    d = f.render('lives ' + str(model.lives), True, [255, 255, 255])
    screen.blit(d, [50, 50])

    d = f.render('hits ' + str(model.hits), True, [255, 255, 255])
    screen.blit(d, [50, 140])

    d = f.render('levels ' + str(model.levels), True, [255, 255, 255])
    screen.blit(d, [50, 240])

    pygame.display.flip()
