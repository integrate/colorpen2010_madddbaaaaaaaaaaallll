import pygame,model

screen = pygame.display.set_mode([1500, 1000])

def hydozhnik():
    screen.fill([34, 56, 12])
    pygame.draw.rect(screen, [56, 98, 21],model.kk)
def updater():
    pygame.display.flip()