import pygame
import sys
import os
from button import Button
from dotenv import load_dotenv

load_dotenv('.env')
PRIMARY_COLOR = os.environ["PRIMARY_COLOR"]

def show_result(win, score, miss, restart, home):

  def replay():
    restart(win=win)

  def return_home():
    home(win=win)

  clock = pygame.time.Clock()
  FPS = 60

  w, h = pygame.display.get_surface().get_size()

  font = pygame.font.Font('fonts/MinecraftRegular-Bmg3.otf', 142)
  text = font.render(str(score), True, PRIMARY_COLOR, "white")
  text_rect = text.get_rect()
  text_rect.center = (w/2, h/2-140)

  mini_font = pygame.font.Font('fonts/MinecraftRegular-Bmg3.otf', 48)
  miss_text = mini_font.render(
    f"Miss: {str(miss)}", True, PRIMARY_COLOR, "white")
  miss_text_rect = miss_text.get_rect()
  miss_text_rect.center = (w/2, h/2-48)

  btns = pygame.sprite.Group()
  restart_btn = Button(w/2, h/2+40, "restart", target=replay)
  btns.add(restart_btn)
  home_btn = Button(w/2, h/2+160, "home", target=return_home)
  btns.add(home_btn)

  showing = True

  while showing:
    win.fill("white")

    clock.tick(FPS)

    win.blit(text, text_rect)
    win.blit(miss_text, miss_text_rect)
    for b in btns:
      b.draw(win)

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
