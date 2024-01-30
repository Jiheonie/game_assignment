import pygame
import os
from dotenv import load_dotenv

load_dotenv()
PRIMARY_COLOR = os.environ["PRIMARY_COLOR"]

class Scoreboard(pygame.sprite.Sprite):
  def __init__(self, dx, dy) -> None:
    super().__init__()
    self.point = 0
    self.miss = 0
    self.font = pygame.font.Font('fonts/MinecraftRegular-Bmg3.otf', 32)
    self.rect_x = dx
    self.rect_y = dy

  def update(self, target_count): 
    if target_count > 0: self.point += 1
    else: self.miss += 1

  def draw(self, screen):
    point_text = self.font.render(f'Point: {self.point}', True, 'black', 'white')
    point_rect = point_text.get_rect()
    point_rect.x = self.rect_x
    point_rect.y = self.rect_y

    miss_text = self.font.render(f'Miss: {self.miss}', True, 'black', 'white')
    miss_rect = miss_text.get_rect()
    miss_rect.x = self.rect_x + 200
    miss_rect.y = self.rect_y

    screen.blit(point_text, point_rect)
    screen.blit(miss_text, miss_rect)


class TimeBar(pygame.sprite.Sprite):
  def __init__(self, dx, dy, t) -> None:
    super().__init__()
    self.rect_x = dx
    self.rect_y = dy
    self.time = t
    self.r_time = t

  def draw(self, screen):
    pygame.draw.rect(
      screen, 
      (211, 211, 211), 
      (self.rect_x - 1, self.rect_y - 1, self.time + 2, 23)
    )
    pygame.draw.rect(
      screen, 
      (95, 158, 160),
      (self.rect_x - 1, self.rect_y, self.r_time, 20)
    )

  def update(self):
    self.r_time -= 1


class DialogButton(pygame.sprite.Sprite):
  def __init__(self, dx, dy) -> None:
    super().__init__()
    self.rect_x = dx
    self.rect_y = dy
    self.rect = pygame.Rect(self.rect_x, self.rect_y, 60, 60)

  def draw(self, screen):
    pygame.draw.rect(
      screen,
      PRIMARY_COLOR,
      (self.rect_x, self.rect_y, 60, 60), 3, 4
    )
    pygame.draw.circle(screen, PRIMARY_COLOR, 
      (self.rect_x + 15, self.rect_y + 15), 4)
    pygame.draw.circle(screen, PRIMARY_COLOR, 
      (self.rect_x + 15, self.rect_y + 30), 4)
    pygame.draw.circle(screen, PRIMARY_COLOR, 
      (self.rect_x + 15, self.rect_y + 45), 4)
    pygame.draw.rect(screen, PRIMARY_COLOR, 
      (self.rect_x + 25, self.rect_y + 13, 25, 4))
    pygame.draw.rect(screen, PRIMARY_COLOR, 
      (self.rect_x + 25, self.rect_y + 28, 25, 4))
    pygame.draw.rect(screen, PRIMARY_COLOR, 
      (self.rect_x + 25, self.rect_y + 43, 25, 4))
    
  def click(self, pos):
    if self.rect.collidepoint(pos):
      return True
    return False


class Dialog(pygame.sprite.Sprite):
  def __init__(self, dx, dy) -> None:
    super().__init__()
    self.rect = pygame.Rect(dx, dy, 540, 480)

  def draw(self, screen): 
    pygame.draw.rect(screen, "white", self.rect, 0, 5)
    pygame.draw.rect(screen, PRIMARY_COLOR, self.rect, 5, 5)

  def update(self): pass


class BoongEffect(pygame.sprite.Sprite):
  def __init__(self, dx, dy) -> None:
    super().__init__()
    self.image = pygame.image.load('assets/boong.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (256, 144))

    self.rect = self.image.get_rect()
    self.rect.x = dx - 128
    self.rect.y = dy - 72

    self.lifetime = 10

  def draw(self, screen):
    screen.blit(self.image, self.rect)
    
  def update(self):
    self.lifetime -= 1


class MissEffect(pygame.sprite.Sprite):
  def __init__(self, dx, dy) -> None:
    super().__init__()
    self.image = pygame.image.load('assets/miss.png').convert_alpha()
    self.image = pygame.transform.scale(self.image, (256, 144))

    self.rect = self.image.get_rect()
    self.rect.x = dx - 128
    self.rect.y = dy - 72

    self.lifetime = 10

  def draw(self, screen):
    screen.blit(self.image, self.rect)
    
  def update(self):
    self.lifetime -= 1
