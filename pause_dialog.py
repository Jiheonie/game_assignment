from game_manager import Dialog
from button import Button
import pygame
import sys

def pause(win, restart, home):
  pausing = True

  def resume(): 
    nonlocal pausing
    pausing = False

  def replay():
    pygame.mixer.pause()
    restart(win=win, home=home)

  def return_home():
    pygame.mixer.pause()
    home(win=win)

  clock = pygame.time.Clock()
  FPS = 60

  w, h = pygame.display.get_surface().get_size()

  dialog = Dialog(w/2 - 270, h/2 - 240)

  btns = pygame.sprite.Group()
  resume_btn = Button(w/2, h/2-120, "resume", target=resume)
  btns.add(resume_btn)
  restart_btn = Button(w/2, h/2, "restart", target=replay)
  btns.add(restart_btn)
  home_btn = Button(w/2, h/2+120, "home", target=return_home)
  btns.add(home_btn)

  while pausing:
    clock.tick(FPS)
    
    dialog.draw(win)
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