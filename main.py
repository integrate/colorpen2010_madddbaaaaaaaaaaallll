import time, pygame
import model,risovanie

import controller


while True:
    time.sleep(1 / 60)
    controller.controlior()
    model.model()

    risovanie.hydozhnik()
    risovanie.updater()