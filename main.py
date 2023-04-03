import time, pygame
import risovanie, risovanie_menu

import controller, model, controler_menu

while True:
    time.sleep(1 / 60)
    if model.igra_or_menu == 'menu':
        risovanie_menu.viewer()
        controler_menu.control()
    elif model.igra_or_menu == 'igra':
        risovanie.hydozhnik()
        controller.controlior()
        model.model()
