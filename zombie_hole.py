import pygame
from zombie import Zombie

class ZombieHole(pygame.sprite.Sprite):
  def __init__(self, dx, dy):
    super().__init__()
    self.zombie = Zombie(dx, dy)
    self.hole_bottom = pygame.image.load('assets/hole_bottom.png').convert_alpha()
    self.hole_top = pygame.image.load('assets/hole_top.png').convert_alpha()
    self.bottom_rect = self.hole_bottom.get_rect()
    self.bottom_rect.x = dx - 7
    self.bottom_rect.y = dy + 20
    self.top_rect = self.hole_top.get_rect()
    self.top_rect.x = dx - 7
    self.top_rect.y = dy - 42

  def draw(self, screen):
    screen.blit(self.hole_top, self.top_rect)
    self.zombie.draw(screen)
    screen.blit(self.hole_bottom, self.bottom_rect)

  def update(self):
    self.zombie.raise_random()