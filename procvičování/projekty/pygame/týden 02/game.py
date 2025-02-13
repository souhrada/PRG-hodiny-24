import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

# naše proměnné, které udávají výšku a šířku
screen_height = 600
screen_width = 800

# vytvoříme obraz
screen = pygame.display.set_mode((screen_width, screen_height))

# vytvoř hodiny
clock = pygame.time.Clock()

running = True

# Spoiler - animace monstra, bude probíráno 13.2.
# def monster_animation():
#     global monster_surf, monster_index
#     monster_index += 0.1

#     if monster_index > len(monster_walk):
#         monster_index = 0
#     monster_surf = monster_walk[int(monster_index)]

# vytvoření hráče
# nahrání obrázku
player_surf = pygame.image.load("arnost.png").convert_alpha()
# zvětšení obrázku (rotozoom umí i rototovat, to my nechceme, proto hodnota 0)
player_surf = pygame.transform.rotozoom(player_surf, 0, 1.5)
player_x = 150
player_y = 150
# vytvoření rectangle, který nám umožní sledovat kolize a přesněji umístit obrázek do herní plochy
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))
player_speed = 10
player_lives = 3
# Počáteční nastavení nesmrtelnosti
invulnerability = False


# Vytvoření fontu k vykreslení životů - pokud nechcete vlastní font, použijte None (bez uvozovek) místo názvu fontu
font = pygame.font.Font("PixelifySans-Regular.ttf", 25)


# vytvoření monstra
monster_run1 = pygame.image.load("monstrum.png").convert_alpha()
monster_run2 = pygame.image.load("monstrum_run.png").convert_alpha()
monster_run_all = [monster_run1, monster_run2] 
# monster_surf = pygame.transform.rotozoom(monster_surf, 0, 5)
monster_index = 0
monster_surf = monster_run_all[monster_index]

monster_x = screen_width - 100
monster_y = 300
monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))
monster_speed = 1



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
    key = pygame.key.get_pressed()

    # pokud je stisknutá klávesa w, pohni hráčem o (x, y)
    if key[pygame.K_w]:
        player_rect.top -= player_speed
    if key[pygame.K_a]:
        player_rect.left -= player_speed
    if key[pygame.K_s]:
        player_rect.bottom += player_speed
    if key[pygame.K_d]:
        player_rect.right += player_speed

  
    # obarví obrazovku na bílo
    screen.fill("white")

    # render fontu
    text_lives = font.render(f"Lives: {player_lives}", False, "#000000") 
    # vykreslení textu na obrazovku
    screen.blit(text_lives, (screen_width-100, 10))

    # na obrazovku vykresli - surface na rectangle (recntagle má souřadnice, viz výše)
    screen.blit(player_surf, player_rect)

    # monstrum se pohybuje zprava doleva
    monster_rect.left -= monster_speed
    screen.blit(monster_surf, monster_rect)

    # zapni časomíru - pod proměnnou přidávej čas
    elapsed_time += clock.get_time()

    

    # pokud nastane kolize mezi hráčem a monstrem
    if player_rect.colliderect(monster_rect):
        # pokud hráč není nesmrtelný - alternativa zápisu if invulnerability == False
        if not invulnerability:
            player_lives -= 1 # odeber život
            invulnerability = True # zapni nesmrtelnost
            elapsed_time = 0 # vynuluj časomíru

    # pokud uběhly 2 sekundy
    if elapsed_time > 2000:
        # vypni nesmrtelnost
        invulnerability = False

    print(player_lives)


    # updatuje vše
    pygame.display.update()
    # pygame.display.flip() - alternativní funkce k .update

    # omez tickrate (rychlost hry) na 60fps, ať je to konzistentní napříč zařízeními
    clock.tick(60)