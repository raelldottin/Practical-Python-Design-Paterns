import pygame

window_dimensions = 800, 600
screen = pygame.display.set_mode(window_dimensions)

player_quits = False


while not player_quits:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            player_quits = True

    pygame.display.flip()
