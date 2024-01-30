import pygame
import os
from start import start

pygame.init()

win = pygame.display.set_mode((1280, 720))
# #2F4F4F
# os.environ["PRIMARY_COLOR"] = str([47, 79, 79])
# print(os.environ["PRIMARY_COLOR"])

pygame.display.set_caption("Zombie Pound!")

start(win=win)

pygame.quit()
