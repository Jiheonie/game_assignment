import pygame
import os
from dotenv import load_dotenv

load_dotenv('.env')
PRIMARY_COLOR = os.environ["PRIMARY_COLOR"]

class Button(pygame.sprite.Sprite):
  def __init__(self, dx, dy, text, target, args:tuple=None) -> None:
    super().__init__()
    self.rect = pygame.Rect(dx-120, dy-40, 240, 80)
    self.font = pygame.font.Font('fonts/MinecraftRegular-Bmg3.otf', 48)
    self.text = text
    self.target = target
    self.args = args

    self.color = PRIMARY_COLOR

  def update(self):
    pos = pygame.mouse.get_pos()
    hit = self.rect.collidepoint(pos)
    self.color = "black" if hit else PRIMARY_COLOR

  def draw(self, screen):
    pygame.draw.rect(screen, self.color, self.rect, 5, 5)

    text = self.font.render(self.text, True, self.color, "white")
    text_rect = text.get_rect()
    text_rect.center = (self.rect.x + 120, self.rect.y + 40)
    screen.blit(text, text_rect)

  def click(self, pos):
    if self.rect.collidepoint(pos):
      if not self.args:
        return self.target()
      return self.target(self.args)