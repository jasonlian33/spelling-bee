import pygame, sys
from button import Button
from noob import Noob 
from game_manager import screen, get_font

pygame.init()

def main():
    run = True
    while run:
        yellow_screen = (255, 255, 187)
        screen.fill(yellow_screen)
        
        mouse_pos = pygame.mouse.get_pos() # gets mouse input/coordinates
        
        # Main Screen Text 
        menu_text = get_font(50).render("Select Level", True, "#9c6c0b")
        menu_rect = menu_text.get_rect(center = (400, 50))
        screen.blit(menu_text, menu_rect)


        # buttons for each level/difficutlies
        Noob_button = Button(image = pygame.image.load("assets/Effortless Rect.png"), pos = (400, 150), 
                                text_input = "Noob", font = get_font(25), base_color="#d7fcd4", hovering_color= "White", scale = 0.8)                           

        Easy_button = Button(image = pygame.image.load("assets/Easy Rect.png"), pos = (400, 250), 
                                    text_input = "Easy", font = get_font(25), base_color="#d7fcd4", hovering_color= "White", scale = 0.8)                           

        Moderate_button = Button(image = pygame.image.load("assets/Moderate Rect.png"), pos = (400, 350), 
                                text_input = "Moderate", font = get_font(25), base_color="#d7fcd4", hovering_color= "White", scale = 0.8)                           

        Hard_button = Button(image = pygame.image.load("assets/Hard Rect.png"), pos = (400, 450), 
                                text_input = "Hard", font = get_font(25), base_color="#d7fcd4", hovering_color= "White", scale = 0.8)                           

        Expert_button = Button(image = pygame.image.load("assets/Expert Rect.png"), pos = (400, 550), 
                                text_input = "Expert", font = get_font(25), base_color="#d7fcd4", hovering_color= "White", scale = 0.8)                           
            
        # shows the button on the screen
        for button in [Noob_button, Easy_button, Moderate_button, Hard_button, Expert_button]:
                button.changeColor(mouse_pos)
                button.update(screen)
            
        # game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Noob_button.checkForInput(mouse_pos):
                    Noob()

        pygame.display.update()

    pygame.quit()

main()