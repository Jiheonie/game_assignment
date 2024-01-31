import pygame
from start import start

pygame.init()

win = pygame.display.set_mode((1280, 720))

pygame.display.set_caption("Zombie Pound!")

start(win=win)

pygame.quit()
