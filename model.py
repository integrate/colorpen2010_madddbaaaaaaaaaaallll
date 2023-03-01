import pygame
kk = pygame.Rect(400, 290, 80, 69)
kk.centerx = 750
kk.centery = 500

def model():
    if left_stena == 0:
        kk.centerx += 1
    elif left_stena == 1:
        kk.centerx += -1

    # kk.centery += 1