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

    d = f.render(str(model.lives), True, [255, 255, 255])
    screen.blit(d, [100 / 2, 100 / 2])

    pygame.draw.rect(screen, [255, 0, 0], model.stena)

    pygame.display.flip()
