import pygame
from sys import exit

# inicializuje hru - spustíme pygame
pygame.init()

# vytvoření animace monstra
def monster_animation():
    # importujeme globální proměnné, které jsme si pro monstrum vytvořili
    global monster_surf, monster_index, monster_run_all

    # animace zjednodušeně - máme list (seznam), ve kterém jsou obrázky v různé fázi pohybu
    # vykreslujeme vždy jeden z obrázků z listu
    # posouváním indexu zvolíme, který obrázek se vykresluje
    monster_index += 0.1 # index měníme pouze o 0.1, aby animace byla pomalejší

    # pokud je index větší, než množství obrázků v listu, vyresetujeme index
    if monster_index > len(monster_run_all):
        monster_index = 0
    
    # surface blitujeme v herní smyčce na obrozovku
    # zde zvolíme, co bude surface, aneb co budeme vykreslovat na obrozovku
    # Pozn.: jelikož měníme index o destinná čísla výše, 
    # je potřeba jej zaokrouhlit zpět na celé číslo pomocí funkce int(), která vždy zaokrouhluje dolu
    monster_surf = monster_run_all[int(monster_index)] 

# funkce na animování hráče, přijímá parametr direction, čímž měníme řadu, ze které vyřezáváme, viz funkce image_cutter
# v našem spritesheetu řada udává směr animace panáčka
# zbytek funkce je podobný funkci animování monstra, s výjimkou, že musíme manuálně napsat, kolik máme framů (nelze to odvodit z velikosti listu, jako to bylo výše)
def animation(direction):
    global player_index, player_img
    frame_count = 3

    player_index += 0.1
    if player_index >= frame_count:
        player_index = 0
    
    player_img = image_cutter(player_spritesheet, int(player_index), direction, 15, 16, 3)

    
# funkce na vyřezávání obrázku ze spritesheetu (spritesheet je obrázek se všemi framy, ze kterých se skládá animace)
# funkce přijímá parametry - spritesheet, začátek vyřezávání na x, začátek vyřezávání na y, šířku, výšku a zvětšení
def image_cutter(sheet, frame_x, frame_y, width, height, scale):
    img = pygame.Surface((width, height)).convert_alpha() # nejprve vytvoříme Surface, na který poté vykreslíme správnou část spritesheetu
    # na surface blitneme část spritesheetu, na surface blitujeme z 0,0
    # frame_x je číslo, kterým budeme manipulovat a určuje, kde na ose x vyřezáváme - násobíme jej vždy šířkou - např. 2 * šířka začne vyřezávat ve třetím sloupci framů  (např. 2*15 začne vyřezávat z 30 pixelu na x, takže ignoruje první dva framy)
    # frame_y je číslo, kterým budeme manipulovat a určuje, kde na ose y vyřezáváme - násobíme jej vždy výškou - např. 3 * výška začne vyřezávat ve čtvrté řadě spritesheetu framů (např. 3*15 začne vyřezávat z 45 pixelu na y, takže ignoruje první tři řady)
    # výška a šířka udává velikost vyřezávátka
    img.blit(sheet, (0,0), ((frame_x * width), (frame_y * height), width, height))
    img = pygame.transform.scale(img, (width*scale, height*scale)) # obrázek zvětšíme, pokud je potřeba
    img.set_colorkey((0, 0, 0)) # tento údaj změní černou barvu na průhlednou, což je potřeba pro správné vykreslení průhlednosti
    return img # funkce vrátí vytvořený obrázek




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
# player_surf = pygame.image.load("arnost.png").convert_alpha()
# zvětšení obrázku (rotozoom umí i rototovat, to my nechceme, proto hodnota 0)
player_x = 150
player_y = 150
# načtení souboru se spritesheetem
player_spritesheet = pygame.image.load("man_brownhair_run.png").convert_alpha()
# první zavolání funkce image_cutter, která nám vykreslí výchozí obrázek pro hráče
player_img = image_cutter(player_spritesheet, 0, 0, 15, 16, 3)
# vytvoření rectangle, který nám umožní sledovat kolize a přesněji umístit obrázek do herní plochy
player_rect = player_img.get_rect(midbottom=(player_x, player_y))
player_index = 0
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
        animation(1)
        player_rect.top -= player_speed
    if key[pygame.K_a]:
        animation(2)
        player_rect.left -= player_speed
    if key[pygame.K_s]:
        animation(0)
        player_rect.bottom += player_speed
    if key[pygame.K_d]:
        animation(3)
        player_rect.right += player_speed

  
    # obarví obrazovku na bílo
    screen.fill("white")

    # render fontu
    text_lives = font.render(f"Lives: {player_lives}", False, "#000000") 
    # vykreslení textu na obrazovku
    screen.blit(text_lives, (screen_width-100, 10))

    # na obrazovku vykresli - surface na rectangle (recntagle má souřadnice, viz výše)
    screen.blit(player_img, player_rect)

    # monstrum se pohybuje zprava doleva
    monster_rect.left -= monster_speed
    # zde spouštíme animaci
    monster_animation()
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



    # updatuje vše
    pygame.display.update()
    # pygame.display.flip() - alternativní funkce k .update

    # omez tickrate (rychlost hry) na 60fps, ať je to konzistentní napříč zařízeními
    clock.tick(60)