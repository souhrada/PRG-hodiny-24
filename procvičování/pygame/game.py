# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True


player_x = 50
player_y = 150

player_rect = pygame.Rect(player_x, player_y, 100, 100)
player_surface = pygame.Surface((player_rect.width, player_rect.height))
player_surface.fill((0, 255, 0))

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

    # pygame.draw.rect(screen, "blue", (player_x, player_y, 100, 100))
    screen.blit(player_surface, player_rect)

    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()