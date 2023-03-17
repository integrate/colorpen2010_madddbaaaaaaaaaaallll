import pygame

screen = pygame.display.get_surface()
shar = pygame.Rect(400, 290, 80, 69)
shar.centerx = 750
shar.centery = 500
left_stena = 0
upstena = 0
skorost = 7
stena = pygame.Rect(50, 50, 50, 50)
storona = None


def model():
    otbifka_ot_steni()
    otbivka_ot_graniz_ecrana()
    peredveshenie()


def otbivka_ot_graniz_ecrana():
    global left_stena, upstena
    if shar.right >= screen.get_width():
        shar.right -= skorost
        left_stena = 1

    if shar.left <= 0:
        shar.left += skorost
        left_stena = 0

    if shar.bottom >= 1000:
        shar.bottom -= skorost
        upstena = 1

    if shar.top <= 0:
        shar.top += skorost
        upstena = 0


def otbifka_ot_steni():
    global left_stena, upstena
    if shar.colliderect(stena):
        if shar.left <= stena.right and storona == 'levo':
            shar.right += skorost
            left_stena = 0
        if shar.bottom >= stena.top and storona == 'niz':
            shar.top -= skorost
            upstena = 1
        if shar.top <= stena.bottom and storona == 'verh':
            shar.bottom += skorost
            upstena = 0
        if shar.right >= stena.left and storona == 'pravo':
            shar.right -= skorost
            left_stena = 1


def peredveshenie():
    if left_stena == 0:
        shar.centerx += skorost
    elif left_stena == 1:
        shar.centerx -= skorost

    if upstena == 0:
        shar.centery += skorost
    elif upstena == 1:
        shar.centery -= skorost
