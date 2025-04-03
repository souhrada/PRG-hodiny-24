# Program momentálně není funkční, v příští hodině dokončíme přesouvání kódu a hru opět zprovozníme

import pygame
from sys import exit
from settings import *
from utility import image_cutter
from player import Player
from monster import Monster

# inicializuje hru - spustíme pygame
pygame.init()




    

# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))

# vytvoř hodiny
clock = pygame.time.Clock()

running = True

player = pygame.sprite.GroupSingle()
player.add(Player())

monsters = pygame.sprite.Group()
monsters.add(Monster())

# Vytvoření fontu k vykreslení životů - pokud nechcete vlastní font, použijte None (bez uvozovek) místo názvu fontu
font = pygame.font.Font("assets/fonts/PixelifySans-Regular.ttf", 25)






# Počáteční hodnota časomíry
elapsed_time = 0

# herní smyčka
while running:
    # kontroluje nám události, které se dějí v naší hře
    for event in pygame.event.get():
        # pokud dojde k události vypnout, vypne
        if event.type == pygame.QUIT:
            running = False
            exit()
    
    # proměnná key, pod ní schováme stisknutou klávesu
  

    # pokud je stisknutá klávesa w, pohni hráčem o (x, y)

  
    # obarví obrazovku na bílo
    screen.fill("white")

    # render fontu
    # text_lives = font.render(f"Lives: {player_lives}", False, "#000000") 
    # vykreslení textu na obrazovku
    # screen.blit(text_lives, (screen_width-100, 10))

    # na obrazovku vykresli - surface na rectangle (recntagle má souřadnice, viz výše)
    
    player.draw(screen)
    player.update()
    
    monsters.draw(screen)
    monsters.update()


    # zapni časomíru - pod proměnnou přidávej čas
    elapsed_time += clock.get_time()

    

    # pokud nastane kolize mezi hráčem a monstrem
    # if player_rect.colliderect(monster_rect):
    #     # pokud hráč není nesmrtelný - alternativa zápisu if invulnerability == False
    #     if not invulnerability:
    #         player_lives -= 1 # odeber život
    #         invulnerability = True # zapni nesmrtelnost
    #         elapsed_time = 0 # vynuluj časomíru

    # pokud uběhly 2 sekundy
    if elapsed_time > 2000:
        # vypni nesmrtelnost
        invulnerability = False



    # updatuje vše
    pygame.display.update()
    # pygame.display.flip() - alternativní funkce k .update

    # omez tickrate (rychlost hry) na 60fps, ať je to konzistentní napříč zařízeními
    clock.tick(60)