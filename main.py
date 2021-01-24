import os.path
import pygame
import pygame.freetype  # Import the freetype module.
import time
import threading
import tts

pygame.init()
screen = pygame.display.set_mode((800, 600))
GAME_FONT = pygame.freetype.Font("resources/Basic-Regular.ttf", 96)
running =  True
read = True

WORDS = open("resources/words.txt").readlines()

word_idx = 0

def play_token(token):
    token = token.strip()
    filename = "samples/"+token+".wav"
    if not os.path.isfile(filename):
        tts.text_to_wav(token, filename)
    sound = pygame.mixer.Sound(filename)
    sound.play()
    while pygame.mixer.get_busy():
        time.sleep(0.1)

def read_word(word):

    tokens = word.strip().split("|")
    for token in tokens: 
        token = token.replace("*","")
        play_token(token)
        print(token)
        time.sleep(0.3)
        
    if len(tokens) > 1:
        token = word.strip().replace("*","").replace("|","")
        print(token)
        play_token(token)

def read_sentence(word):
    tokens = word.split(" ")
    for token in tokens:
        read_word(token)
        time.sleep(0.5)

    if len(tokens)>1:
        play_token(word.strip().replace("*","").replace("|",""))

def render_word(word):

    colors = [ (0,0,0), (255, 0, 0)]

    tokens = word.strip().split("|")
    idx = 0
    offset = 0

    ret = pygame.Surface((800, 100), pygame.SRCALPHA)

    for token in tokens: 
        if token.startswith("*"):
            color = (255, 0, 0)
            token = token.replace("*","")
        else:
            color = (0, 0, 0)

        surface, rect = GAME_FONT.render(token, color)
        ret.blit(surface, (rect[0] + offset, 0))
        idx += 1
        #w, h = pygame.font.Font.size(GAME_FONT, token)
        offset += rect[0] + rect[2]

    return ret  #GAME_FONT.render(word, (0, 0, 0))


while running:

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                print("Next word")
                word_idx = word_idx + 1
                read = True
            if event.key == pygame.K_LEFT:
                print("Prev word")
                word_idx = word_idx - 1
                read = True
            if event.key == pygame.K_SPACE:
                read = True

        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    # You can use `render` and then blit the text surface ...
    text_surface = render_word(WORDS[word_idx])
    screen.blit(text_surface, (40, 250))

    if read:
        read = False
        x = threading.Thread(target=read_sentence, args = (WORDS[word_idx],))
        x.start() #read_word(WORDS[word_idx])
    
    pygame.display.flip()

pygame.quit()