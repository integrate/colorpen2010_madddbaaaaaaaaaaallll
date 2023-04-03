import pygame, model

fon = pygame.image.load('fon_menu.jpg')
screen = pygame.display.get_surface()
f = pygame.font.SysFont('arial', 100, True, True)
pygame.init()


def viewer():
    screen.blit(fon, [0, 0])
    d = f.render('нажмите прoбел чтобы начать', True, [255, 255, 255])
    screen.blit(d, [50, 500])

    pygame.display.flip()
