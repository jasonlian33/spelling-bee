import pygame, sys
from button import Button
from game_manager import screen, get_font
import random

# dictionary that holds each word's audio
original_noob_dict = {
    "snake":  [pygame.mixer.Sound("audio/snake.wav"), "The ??? bit the boy."],
    "climb": [pygame.mixer.Sound("audio/climb.wav"), "Monkey ??? trees."],
    "credit": [pygame.mixer.Sound("audio/credit.wav"), "I used ??? to pay for my food."],
    "crown": [pygame.mixer.Sound("audio/crown.wav"), "The king put on his ???."],
    "float": [pygame.mixer.Sound("audio/float.wav"), "That serve had a lot of ??? to it."], 
    "ground": [pygame.mixer.Sound("audio/ground.wav"), "The ??? was very hard."],
    "ladder": [pygame.mixer.Sound("audio/ladder.wav"), "The ??? helped me reach the shelf."],
    "music": [pygame.mixer.Sound("audio/music.wav"), "I listen to ??? everyday."],
    "second": [pygame.mixer.Sound("audio/second.wav"), "I never come in ??? place"],
    "whisper": [pygame.mixer.Sound("audio/whisper.wav"), "They told us to ??? in the library."]
}

def Noob():
    copy_noob_dict = original_noob_dict.copy()

    # gets a random word from the noob dictionary
    random_word = random.choice(list(copy_noob_dict.keys())) 
    word_audio = copy_noob_dict[random_word][0] # gets the audio from the selected word 

    player_score = 0 # keeps track of the players score

    base_font = pygame.font.Font(None, 50)
    base1_font = pygame.font.Font(None, 30)
    user_text = ''

    # dimension and color of the text box 
    input_rect = pygame.Rect(250, 350, 350, 50) # (x,y, x-dimension, y-dimension)
    color_active = "Green"
    color_passive = "Black"
    color = color_passive

    # turns to true when player clicks inside the text box
    active = False

    while player_score < len(original_noob_dict):
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

        # reset button that resets player score to 0
        noob_reset = Button(image=None, pos=(375, 550), 
                            text_input="RESET", font=get_font(20), base_color="White", hovering_color="Green")

        noob_reset.changeColor(noob_mouse_pos)
        noob_reset.update(screen)

        # Keep track of player's score
        score_keeper = Button(image=None, pos=(650, 550), 
                            text_input= "SCORE: " + str(player_score) + "/" + str(len(original_noob_dict)), font=get_font(20), base_color="White", hovering_color="Green")

        score_keeper.changeColor(noob_mouse_pos)
        score_keeper.update(screen)



        # button for playing word_audio
        play_audio = Button(image = pygame.image.load("assets/bee1.png"), pos = (500, 150),
                            text_input= 'hi', font= get_font(1), base_color= "White", hovering_color= "White", scale= 0.02)

        play_audio.update(screen)


        for event in pygame.event.get():
           # when playes clicks out of the tab
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # when player clicks on mouse button
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_audio.checkForInput(noob_mouse_pos):
                        word_audio.play()
                if noob_back.checkForInput(noob_mouse_pos):
                    return
                if noob_reset.checkForInput(noob_mouse_pos):
                    player_score = 0
                    copy_noob_dict = original_noob_dict.copy()
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
                        if user_text.strip().lower() == random_word:
                            print("correct!")
                            player_score += 1 # adds one to player score
                            del copy_noob_dict[random_word]
                            if copy_noob_dict:
                                random_word = random.choice(list(copy_noob_dict.keys())) # gets a new word from the dictionary
                                word_audio = copy_noob_dict[random_word][0] # gets the audio from the selected word 
                                user_text = ''
                            else:
                                print("Congratulations! You have completed the level.")
                                return
                        else:
                            print("that is incorrect!")
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

        # Click and Type Message
        type_here = 'Click and Type: '
        text1_surface = base1_font.render(type_here, True, "White")
        screen.blit(text1_surface, (input_rect.x - 175, input_rect.y + 15))

        # Click on me for word message
        play_word = 'Click on me to play the word!'
        text2_surface = base1_font.render(play_word, True, "White")
        screen.blit(text2_surface, (input_rect.x - 85, input_rect.y - 200 ))

        # Sentence for each word
        sentence = copy_noob_dict[random_word][1]
        text3_surface = base1_font.render(sentence, True, "White")
        screen.blit(text3_surface, (input_rect.x - 85, input_rect.y - 100))




        pygame.display.update()
