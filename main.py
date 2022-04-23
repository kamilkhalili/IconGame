import pygame
import random
import sys
import time

successes, failures = pygame.init()
print("{0} successes and {1} failures". format(successes,failures))

playerImg= pygame.image.load('picnic-basket.png')

WIDTH = 300
HEIGHT = 300

BLACK = (0,0,0)
YELLOW = (255,255,0)
WHITE = (255,255,255)
VIOLET = (128,0,255)
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
fps = 30

game_over = False



# Player
player_size=30
player_pos= [WIDTH/2,HEIGHT-3*player_size]
screen.blit(playerImg,(player_pos[0],player_pos[1]))

# Enemy
RED = (255,0,0)
enemy_size = 10
enemy_pos= [random.randint(0, WIDTH-enemy_size),0]

SPEED = 10

score = 0

myFont = pygame.font.SysFont ("monospace",25)
YELLOW = (255,255,0)

def detect_collision(player_pos,enemy_pos):
  p_x = player_pos[0]
  p_y = player_pos[1]
  e_x = enemy_pos[0]
  e_y = enemy_pos[1]
  ps = player_size
  es = enemy_size

  if (e_x>=p_x and e_x<(p_x+ps)) or (p_x>=e_x and p_x<(e_x+es)):
    if (e_y>=p_y) and e_y<(p_y+ps) or ((p_y>=e_y) and p_y<(e_y+es)):
      return True
    return False

init_time=time.time()
cur_time=time.time()
timer=cur_time-init_time
    
while not game_over:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size
            elif event.key == pygame.K_RIGHT:
                x += player_size
            player_pos = [x,y]
  screen.fill(BLACK)
  screen.blit(playerImg,(player_pos[0],player_pos[1]))
  #pygame.draw.rect(screen,GREEN,(player_pos[0],player_pos[1],player_size,player_size))
  pygame.draw.rect(screen, RED,(enemy_pos[0],enemy_pos[1],enemy_size,enemy_size))

  text = "Score=" + str(score)
  label = myFont.render(text,1,YELLOW)
  screen.blit(label,(WIDTH-300,HEIGHT-40))

  text = "Time:" + str(timer)
  label = myFont.render(text,1,YELLOW)
  screen.blit(label,(WIDTH-100,HEIGHT-40))

  if enemy_pos[1] >=0 and enemy_pos[1]<HEIGHT:
      enemy_pos[1] += SPEED
  else :
    enemy_pos[0] = random.randint(0,WIDTH-enemy_size)
    enemy_pos[1] = 0
  if detect_collision(player_pos,enemy_pos):
      score +=1
  clock.tick(fps)
  pygame.display.update()
  timer=time.time()-init_time

  if timer>60:
      screen.fill(BLACK)
      text = "Game Over"
      textScore = "Score:"+str(score)
      label = myFont.render(text,1,YELLOW)
      labelScore = myFont.render(textScore,1,YELLOW)
      screen.blit(label,(WIDTH-210,HEIGHT-200))
      screen.blit(labelScore,(WIDTH-195,HEIGHT-150))
      pygame.display.update()
      time.sleep(1000)