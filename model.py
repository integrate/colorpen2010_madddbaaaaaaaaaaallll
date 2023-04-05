import pygame

resultat=0
screen = pygame.display.get_surface()
shar = pygame.Rect(400, 290, 80, 80)
shar.centerx = 750
shar.centery = 500
left_stena = 0
upstena = 0
skorost = 7
stena = pygame.Rect(50, 50, 50, 50)
storona = None
lives = 3
hits = 10
levels = 0

igra_or_menu = 'menu'


def live():
    global lives, igra_or_menu, skorost, levels, hits,resultat
    lives -= 1
    if lives == -1:
        if levels>resultat:
            resultat=levels
        hits = 10
        levels = 0
        shar.centerx = 750
        shar.centery = 500
        lives = 3
        skorost = 7
        igra_or_menu = 'menu'


def hit():
    global hits
    hits -= 1
    level()


def level():
    global hits, levels, skorost
    if hits == 0:
        levels += 1
        hits = 10
        skorost += 1


def model():
    otbifka_ot_steni()
    otbivka_ot_graniz_ecrana()
    peredveshenie()


def otbivka_ot_graniz_ecrana():
    global left_stena, upstena, lives
    if shar.right >= screen.get_width():
        shar.right -= skorost
        left_stena = 1
        live()

    if shar.left <= 0:
        shar.left += skorost
        left_stena = 0
        live()

    if shar.bottom >= screen.get_height():
        shar.bottom -= skorost
        upstena = 1
        live()

    if shar.top <= 0:
        shar.top += skorost
        upstena = 0
        live()


def otbifka_ot_steni():
    global left_stena, upstena, hits
    if shar.colliderect(stena):
        if shar.left <= stena.right and storona == 'levo':
            shar.left = stena.right
            left_stena = 0
            hit()
        if shar.bottom >= stena.top and storona == 'niz':
            shar.bottom = stena.top
            upstena = 1
            hit()
        if shar.top <= stena.bottom and storona == 'verh':
            shar.top = stena.bottom
            upstena = 0
            hit()
        if shar.right >= stena.left and storona == 'pravo':
            shar.right = stena.left
            left_stena = 1
            hit()


def peredveshenie():
    if left_stena == 0:
        shar.centerx += skorost
    elif left_stena == 1:
        shar.centerx -= skorost

    if upstena == 0:
        shar.centery += skorost
    elif upstena == 1:
        shar.centery -= skorost


def peredeshenie_steni_verh():
    global stena, storona
    stena = pygame.Rect(0, 0, screen.get_width(), 150)
    storona = 'verh'


def peredeshenie_steni_niz():
    global stena, storona
    stena = pygame.Rect(0, screen.get_height() - 150, screen.get_width(), 150)
    storona = 'niz'


def peredeshenie_steni_levo():
    global stena, storona
    stena = pygame.Rect(0, 0, 150, screen.get_height())
    storona = 'levo'


def peredeshenie_steni_pravo():
    global stena, storona
    stena = pygame.Rect(screen.get_width() - 150, 0, 150, screen.get_height())
    storona = 'pravo'


def full_screen():
    if screen.get_width() == 1500:
        pygame.display.set_mode([0, 0], pygame.FULLSCREEN)
    else:
        pygame.display.set_mode([1500, 1000])
