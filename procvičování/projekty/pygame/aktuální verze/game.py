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

# vytvoření hráče
# nahrání obrázku
player_surf = pygame.image.load("arnost.png").convert_alpha()
# zvětšení obrázku (rotozoom umí i rototovat, to my nechceme, proto hodnota 0)
player_surf = pygame.transform.rotozoom(player_surf, 0, 2)
player_x = 150
player_y = 50
# vytvoření rectangle, který nám umožní sledovat kolize a přesněji umístit obrázek do herní plochy
player_rect = player_surf.get_rect(midbottom=(player_x, player_y))
player_speed = 10
player_lives = 3

# vytvoření monstra
monster_surf = pygame.image.load("monstrum.png").convert_alpha()
monster_surf = pygame.transform.rotozoom(monster_surf, 0, 10)
monster_x = screen_width - 10
monster_y = 300
monster_rect = monster_surf.get_rect(midbottom=(monster_x, monster_y))
monster_speed = 1


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

    # na obrazovku vykresli - surface na rectangle (recntagle má souřadnice, viz výše)
    screen.blit(player_surf, player_rect)

    # monstrum se pohybuje zprava doleva
    monster_x -= monster_speed
    screen.blit(monster_surf, monster_rect)

    # pokud nastane kolize mezi hráčem a monstrem, odeber životy
    if player_rect.colliderect(monster_rect):
        player_lives -= 1



    # updatuje vše
    pygame.display.update()
    # pygame.display.flip() - alternativní funkce k .update

    # omez tickrate (rychlost hry) na 60fps, ať je to konzistentní napříč zařízeními
    clock.tick(60)