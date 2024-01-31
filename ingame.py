import pygame
from pygame import mixer
import sys
import os
from game_manager import Scoreboard, DialogButton, TimeBar, BoongEffect, MissEffect
from zombie_hole import ZombieHole
from pause_dialog import pause
from result import show_result

mixer.init()
bg_sound = mixer.Sound('audios/game_playing.mp3')

def in_game(win, home):

  clock = pygame.time.Clock()
  FPS = 60

  w, h = pygame.display.get_surface().get_size()

  bg_sound.play(-1)

  # in-game
  time = 1000

  scoreboard = Scoreboard(dx=850, dy=70)

  time_bar = TimeBar(dx=w/2-time/2, dy=20, t=time)

  dialog_btn = DialogButton(dx=w-20-60, dy=20)

  holes = pygame.sprite.Group()
  holes.add(ZombieHole(50 , 250))
  holes.add(ZombieHole(50 , 550))
  holes.add(ZombieHole(350 , 400))
  holes.add(ZombieHole(650 , 250))
  holes.add(ZombieHole(650 , 550))
  holes.add(ZombieHole(950 , 400))

  effects = pygame.sprite.Group()

  while time > 0:
    # pygame.time.delay(100)

    clock.tick(FPS)

    # clear screen before updating
    win.fill("white")

    holes.update()

    time_bar.draw(win)
    scoreboard.draw(win)
    dialog_btn.draw(win)
    for hole in holes: 
      hole.draw(win)
    effects.draw(win)
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        dx = pos[0]
        dy = pos[1]
        print(pos)

        # pause dialog
        if dialog_btn.click(pos=pos):
          pause(win=win, restart=in_game, home=home)

        else:
          target_count = 0
          for zomb_hole in holes:
            target = zomb_hole.zombie.click(pos)
            if target: target_count += 1
          scoreboard.update(target_count)
          if target_count > 0:
            effects.add(BoongEffect(dx, dy))
          else:
            effects.add(MissEffect(dx, dy))

    for e in effects:
      if e.lifetime == 0:
        effects.remove(e)
      
    for e in effects:
      e.update()

    time -= 1
    time_bar.update()

    keys = pygame.key.get_pressed()

    if time == 0:
      show_result(win=win, score=scoreboard.point, miss=scoreboard.miss, restart=in_game, home=home)

    pygame.display.update()
