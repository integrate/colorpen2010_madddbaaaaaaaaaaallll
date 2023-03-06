import time, pygame
import risovanie

import controller,model


while True:
    time.sleep(1 / 60)
    controller.controlior()
    model.model()

    risovanie.hydozhnik()
    risovanie.updater()