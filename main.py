import pygame
import button

pygame.init()

# game dimension
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Spelling Bee Game') # caption for the game


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size) 


run = True
while run:
    yellow_screen = (255, 255, 187)
    screen.fill(yellow_screen)
    
    mouse_pos = pygame.mouse.get_pos() # gets mouse input/coordinates
    
    menu_text = get_font(50).render("Select Level", True, "#9c6c0b")
    menu_rect = menu_text.get_rect(center = (400, 75))

    screen.blit(menu_text, menu_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()