import time, pygame

screen = pygame.display.set_mode([1500, 1000])
import controller

kk = pygame.Rect(400, 290, 80, 69)
kk.centerx = 750
kk.centery = 500
while True:
    time.sleep(1 / 60)
    controller.controlior()
    kk.centerx += 1

    screen.fill([34, 56, 12])
    pygame.draw.rect(screen, [56, 98, 21], kk)
    pygame.display.flip()
