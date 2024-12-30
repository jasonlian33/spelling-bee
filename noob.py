import pygame, sys
from button import Button
from game_manager import screen, get_font
from pydub import AudioSegment
import random



noob_dict = {
    "snake": AudioSegment.from_file("audio/snake.m4a", format = "m4a")
}



def Noob():
    base_font = pygame.font.Font(None, 50)
    base1_font = pygame.font.Font(None, 30)
    user_text = ''
    type_here = 'Click and Type: '
    player_score = 0 # keeps track of the players score

    # dimension and color of the text box 
    input_rect = pygame.Rect(250,300, 350, 50) # (x,y, x-dimension, y-dimension)
    color_active = "White"
    color_passive = "Black"
    color = color_passive

    active = False


    while True:
        noob_mouse_pos = pygame.mouse.get_pos()

        # fills background to desire color
        screen.fill("#cfb825") 
        noob_text = get_font(35).render("Difficulty: Noob", True, "White")
        noob_rect = noob_text.get_rect(center=(400, 50))
        screen.blit(noob_text, noob_rect)

        # back button that goes back to main menu
        noob_back = Button(image=None, pos=(75, 550), 
                            text_input="BACK", font=get_font(20), base_color="White", hovering_color="Green")

        noob_back.changeColor(noob_mouse_pos)
        noob_back.update(screen)

        # gets a random word from the noob dictionary
        random_word = random.choice(list(noob_dict.keys())) 
        word_audio = noob_dict[random_word] # gets the audio from the selected word 

        for event in pygame.event.get():
           # when playes clicks out of the tab
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # when player clicks on back button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if noob_back.checkForInput(noob_mouse_pos):
                    return
                if input_rect.collidepoint(event.pos):
                    active = True
                else: 
                    active = False
                    

            # any other inputs    
            if event.type == pygame.KEYDOWN:
                if active == True:
                    if event.key == pygame.K_BACKSPACE: # if player deletes a letter
                        user_text = user_text[:-1] # index to remove last letter
                    elif event.key == pygame.K_RETURN:
                        # code that checks whether the code is right or not
                        if user_text.strip().lower() == random_word:
                            print("correct!")
                    else:
                        user_text += event.unicode


        if active:
            color = color_active
        else:
            color = color_passive

        # displays the user text
        pygame.draw.rect(screen, color, input_rect, 2)
        text_surface = base_font.render(user_text, True, "White")
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(225, text_surface.get_width() + 10)

        text1_surface = base1_font.render(type_here, True, "White")
        screen.blit(text1_surface, (input_rect.x -50,input_rect.y - 10))

        pygame.display.update()
