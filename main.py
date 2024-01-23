import pygame
import os
import sys
import time
import button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT= 640
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Card Memory Game')

# Global Variables
start_game = False
score = 0
correct = []
rows = 3
cols = 4

# Colors
BG = (242, 222, 139)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
ORANGE= (255, 127, 0)
BLACK = (0, 0, 0)

# Main Menu
start_img = pygame.image.load('buttons/start_btn.png')
exit_img = pygame.image.load('buttons/exit_btn.png')

# Text
title_font = pygame.font.SysFont('Cochin', 50)
title = title_font.render('Memory Game!', True, (0, 0, 0))
# sub_font= pygame.font.SysFont('Cochin', 25)
# sub_title = sub_font.render('')
score_font = pygame.font.SysFont('Cochin', 30)
score_text = score_font.render(f'Score: {score}', True, (0, 0, 0))


class Card:
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
  
    self.frame_index = 0
    self.card_list = []

    num_of_images = len(os.listdir(f'Cards/'))
    for num in range(num_of_images):
      image = pygame.image.load(f'Cards/{num}.png')
      image = pygame.transform.scale(image, (100, 100))
    self.card_list.append(image)

    self.image = self.card_list[self.frame_index]
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.width = self.image.get_width()
    self.height = self.image.get_height()
    
  def draw(self):
    screen.blit(self.image, self.rect)






class Timer:
    def __init__(self, x, y, timer):
        self.x = x
        self.y = y
        self.timer = timer
        self.start_time = pygame.time.get_ticks() / 1000 

    def update(self):
        elapsed_time = pygame.time.get_ticks() / 1000 - self.start_time  
        self.countdown = max(0, self.timer - elapsed_time)

    def draw(self):
        ratio = self.countdown / self.timer

        pygame.draw.rect(screen, BLACK, (self.x - 2, self.y - 2, 654, 24))
        pygame.draw.rect(screen, RED, (self.x, self.y, 650, 20))
        pygame.draw.rect(screen, ORANGE, (self.x, self.y, 650 * ratio, 20))




# Button Creations
start_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 150, start_img, 1)
exit_button = button.Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 50, exit_img, 1)

# Class Builders
card1 = Card(400, 300)
timer_count = Timer(75, 560, 60)


# Game Runners
run = True
clock = pygame.time.Clock()

while run:
  clock.tick(60)
  
  if start_game == False:
    screen.fill(BG)
    screen.blit(title, (250, 50))
    if start_button.draw(screen):
      start_game = True
    if exit_button.draw(screen):
      run = False

  else: 
    screen.fill(BG)
    screen.blit(score_text, (25, 25))
    card1.draw()
    timer_count.update()
    timer_count.draw()
    
    
    

  # Does not change
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()
  

pygame.quit()