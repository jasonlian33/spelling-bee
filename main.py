import pygame
import button

pygame.init()

# game dimension
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Spelling Bee Game') # caption for the game

run = True
while run:
    yellow_screen = (255, 255, 187)
    screen.fill(yellow_screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()