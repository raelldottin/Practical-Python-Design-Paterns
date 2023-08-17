import pygame
import time

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.draw.rect(screen, (255, 0, 34), pygame.Rect(42, 15, 40, 32))
pygame.display.flip()

time.sleep(10)
