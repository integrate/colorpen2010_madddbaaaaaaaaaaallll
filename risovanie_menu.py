import pygame, model

fon = pygame.image.load('fon_menu.jpg')
screen = pygame.display.get_surface()
f = pygame.font.SysFont('arial', 40, True, True)
h = pygame.font.SysFont('arial', 25, True, True)
pygame.init()


def viewer():
    screen.blit(fon, [0, 0])
    b = h.render('лучший результат ' +str(model.resultat), True, [255, 255, 255])
    d = f.render('нажмите прoбел чтобы начать', True, [255, 255, 255])
    screen.blit(d, [25, 250])
    screen.blit(b, [25, 325])

    pygame.display.flip()
