import pygame
screen = pygame.display.get_surface()
kk = pygame.Rect(400, 290, 80, 69)
kk.centerx = 750
kk.centery = 500
left_stena=0
upstena=0
skorost=7
stena=pygame.Rect(50,50,50,50)
def model():
    global left_stena,upstena
    if kk.right >=screen.get_width():
        kk.right-=skorost
        left_stena=1

    if kk.left <= 0:
        kk.left+=skorost
        left_stena=0

    if kk.bottom >= 1000:
        kk.bottom-=skorost
        upstena=1

    if kk.top <= 0:
        kk.top+=skorost
        upstena=0


    if kk.colliderect(stena):
        if kk.left <= stena.right:
            kk.right+=skorost
            left_stena=0
        if kk.bottom >= stena.top:
            kk.top-=skorost
            upstena=1
    #
    # if stena.left <= 0:
    #     kk.left+=skorost
    #     left_stena=0
    #
    # if kk.bottom >= 1000:
    #     kk.bottom-=skorost
    #     upstena=1
    #
    # if kk.top <= 0:
    #     kk.top+=skorost
    #     upstena=0


    if left_stena == 0:
        kk.centerx += skorost
    elif left_stena == 1:
        kk.centerx -= skorost

    if upstena == 0:
        kk.centery += skorost
    elif upstena == 1:
        kk.centery -= skorost