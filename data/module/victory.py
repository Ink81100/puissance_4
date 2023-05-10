import pygame
import math
from pygame.locals import *

class Victory():

    def __init__(self,screen,grille,gagnant) -> None:
        
        ###Vérification des arguments
        #types
        print(type(gagnant))
        assert type(gagnant) == pygame.Surface,'Gagnant est pas sprite'
        #Attributs
        self.screen = screen
        self.grille = grille
        self.sprite_gagnant = gagnant
        self.running = True
        #Rectangle
        self.rectangle = pygame.Rect(self.grille.marge[0],
                                     self.grille.marge[1],
                                     self.grille.size()[0] * self.grille.largeur_tab(),
                                     self.grille.size()[1] * self.grille.hauteur_tab())

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def display(self):
        pygame.draw.rect(self.screen,'Orange',self.rectangle)
        self.screen.blit(self.sprite_gagnant,(self.rectangle.left + math.ceil(self.rectangle.width/2) - math.ceil(self.sprite_gagnant.get_width()/2),
                                              self.rectangle.top + math.ceil(self.rectangle.height/2) - math.ceil(self.sprite_gagnant.get_height()/2)))
        pygame.display.update()
        pygame.time.wait(5000)
        self.running = False
        
    def run(self):
        while self.running:
            self.event()
            self.display()
