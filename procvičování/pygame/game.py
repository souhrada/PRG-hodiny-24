# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


player_x = 50
player_y = 150

# player_surface = pygame.Surface((player_rect.width, player_rect.height))
# player_surface.fill((0, 255, 0))

player_image = pygame.image.load("player.png").convert_alpha()
player_rect = player_image.get_rect(center=(player_x, player_y))

enemy_image = pygame.image.load("enemy.png").convert_alpha()
enemy_rect = enemy_image.get_rect(center=(200, 200))

enemy_speed = 5

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_rect.y -= 3
    if keys[pygame.K_s]:
        player_rect.y += 3
    if keys[pygame.K_a]:
        player_rect.x -= 3
    if keys[pygame.K_d]:
        player_rect.x += 3

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")


    # RENDER YOUR GAME HERE

    # pygame.draw.rect(screen, "blue", (player_x, player_y, 100, 100))
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)

    enemy_rect.y += enemy_speed

    if enemy_rect.bottom > screen.get_height() or enemy_rect.top < 0:
        enemy_speed *= -1

    if player_rect.colliderect(enemy_rect):
        print("Auuu!")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()