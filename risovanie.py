import pygame,model
porgran=pygame.Rect(50,50,50,50)
screen = pygame.display.set_mode([1500, 1000])
pygame.draw.rect(screen,[255, 50,21],porgran)
def hydozhnik():
    screen.fill([34, 56, 12])
    pygame.draw.rect(screen, [56, 98, 21],model.kk)
def updater():
    pygame.display.flip()
# def pogranichnik():
    # if porgran.width ==