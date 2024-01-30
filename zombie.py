import pygame
import random

class Zombie(pygame.sprite.Sprite):   
  def __init__(self, dx, dy) -> None:
    super().__init__()
    self.image = pygame.image.load('assets/zombie.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (256, 256))

    self.rect = self.image.get_rect()
    self.rect.x = dx
    self.rect.y = dy - 60

    self.is_up = False
    self.time = random.randint(10, 50)
    self.frame = 0
    self.move_done = False

  def draw(self, screen):
    screen.blit(self.image, self.rect)
    if self.time > 0:
      self.time -= 1
      self.move_done = False
    else: 
      if self.move_done:
        if self.is_up:
          self.turn_down()
        else: 
          self.turn_up()
      else: pass
    
  def update(self):
    pass

  def turn_down(self):
    self.is_up = False
    self.time = random.randint(100, 300)

  def turn_up(self):
    self.is_up = True
    self.time = 100

  def click(self, pos):
    if self.rect.collidepoint(pos) and self.is_up:
      # self.rect.move_ip(0, 60)
      self.time = 0
      if self.frame > 0:
        self.rect.move_ip(0, 10)
        self.frame -= 10
      else:
        self.move_done = True
      print("zombie clicked down")
      return True

  def raise_random(self):
    if self.time == 0:
      if not self.is_up:
        if self.frame < 60:
          self.rect.move_ip(0, -10)
          self.frame += 10
        else:
          self.move_done = True
        # self.rect.move_ip(0, -60)
      else:
        if self.frame > 0:
          self.rect.move_ip(0, 10)
          self.frame -= 10
        else:
          self.move_done = True
        # self.rect.move_ip(0, 60)

