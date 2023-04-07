import pygame
import pygame_menu
from menu import Title_screen
from objects.grille import Grille

pygame.init()

screen = pygame.display.set_mode((400,400))


play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

pygame.quit()

