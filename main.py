import pygame
import os
import button

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT= 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Card Memory Game')

# Global Variables
start_game = False
score = 0

# Main Menu
start_img = pygame.image.load('buttons/start_btn.png')
exit_img = pygame.image.load('buttons/exit_btn.png')


class Card:
  def __init__(self, x, y, image, scale):
    self.frame_index = 0
    self.card_list = []

    num_of_images = len(os.listdir(f'Cards'))
    for num in range(num_of_images):
      image = pygame.image.load(f'Cards/{num}.png')
      image = pygame.transform.scale(image, (int(self.width * scale), int(self.height * scale)))
      self.card_list.append(image)

    self.image = self.card_list[self.frame_index]
    self.rect = self.image.get_rect()
    self.rect.center = (x, y)
    self.width = self.image.get_width()
    self.height = self.image.get_height()


    
  def draw(self):
    screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

  def update(self):
    pass









# button creations
start_button = button.Button(SCREEN_WIDTH // 2 - 130, SCREEN_HEIGHT // 2 - 150, start_img, 1)
exit_button = button.Button(SCREEN_WIDTH // 2 - 110, SCREEN_HEIGHT // 2 + 50, exit_img, 1)




run = True
clock = pygame.time.Clock()

while run:
  clock.tick(60)
  
  if start_game == False:
    screen.fill((242, 222, 139))
    if start_button.draw(screen):
      start_game = True
    if exit_button.draw(screen):
      run = False

  else: 
    screen.fill((242, 222, 139))
 
    

  # Does not change
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
  
  pygame.display.update()
  

pygame.quit()