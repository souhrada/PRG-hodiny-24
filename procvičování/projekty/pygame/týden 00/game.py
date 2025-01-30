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

# vytvoření hráče - hráč = obdélník - x, y, šířka, výška
player = pygame.Rect((50, 100, 50, 50))

speed = 10

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
        player.move_ip(0, -speed)
    if key[pygame.K_a]:
        player.move_ip(-speed, 0)
    if key[pygame.K_s]:
        player.move_ip(0, speed)
    if key[pygame.K_d]:
        player.move_ip(speed, 0)



    # obarví obrazovku na zeleno
    screen.fill("green")

    # nakreslí vytvořený obdélník - na obrazovku, červenou barvou, obdélník-hráč
    pygame.draw.rect(screen, (255,0,0), player)

    # updatuje vše
    pygame.display.update()
    # pygame.display.flip() - alternativní funkce k .update

    # omez tickrate (rychlost hry) na 60fps, ať je to konzistentní napříč zařízeními
    clock.tick(60)