import pygame
import sys
import os
from button import Button
from ingame import in_game
from dotenv import load_dotenv

load_dotenv('.env')
PRIMARY_COLOR = os.environ["PRIMARY_COLOR"]
print(PRIMARY_COLOR)

def start(win):

  def play():
    in_game(win=win, home=start)

  clock = pygame.time.Clock()
  FPS = 60

  w, h = pygame.display.get_surface().get_size()

  text_font = pygame.font.Font('fonts/MinecraftRegular-Bmg3.otf', 128)
  title = text_font.render("Zombie Pound", True, PRIMARY_COLOR, "white")
  title_rect = title.get_rect()
  title_rect.center = (w/2, h/2 - 48)

  btns = pygame.sprite.Group()
  play_btn = Button(w/2, h/2+80, "play", target=play)
  btns.add(play_btn)

  while True:
    clock.tick(FPS)

    win.fill("white")

    win.blit(title, title_rect)
    play_btn.draw(win)

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        print(pos)
        for b in btns:
          b.click(pos=pos)

    btns.update()

    keys = pygame.key.get_pressed()

    pygame.display.update()
    