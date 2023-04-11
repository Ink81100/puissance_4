import pygame
from pygame.locals import *
from data.objects.grille import Grille
import random

class Game():

    def __init__(self,screen = pygame.display.set_mode((900,500))) -> None:

        #Attributes
        self.running = True
        self.screen = screen
        self.grille = Grille(self.screen)
        self.selection = (False,0) #Si la sourie survole une colone
        self.joueur = random.randint(1,2)
        print('le joueur %s demarre en premier' % self.joueur)
    
    def event(self) -> None:
        """Boucle  d'évènement"""
        for event in pygame.event.get():
            #Fermeture de la fenêtre
            if event.type == pygame.QUIT:
                self.running = False
            ###Vérification si la sourie survole la grille
            #Largeur
            if pygame.mouse.get_pos()[0] >= self.grille.marge[0] and pygame.mouse.get_pos()[0] < self.grille.marge[0] + self.grille.size()[0] * self.grille.largeur_tab():
                #Hauteur
                if pygame.mouse.get_pos()[1] >= self.grille.marge[1] and pygame.mouse.get_pos()[1] <= self.grille.marge[1] + self.grille.size()[1] * self.grille.hauteur_tab():
                    print('colone %s' % ((pygame.mouse.get_pos()[0] - self.grille.marge[0])//self.grille.size()[0]))
                    #Stockage de la colonne où est la sourie
                    self.selection = (True,(pygame.mouse.get_pos()[0] - self.grille.marge[0])//self.grille.size()[0])
                    #Si il clic, ajoute un  jeton sur la colonne selectionnée
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.grille.ajout_jeton(self.selection[1],self.joueur)
                        if self.joueur == 1:
                            self.joueur = 2
                        else:
                            self.joueur = 1
                        print('Au tour du joueur %s' % self.joueur)
            else:
                self.selection = (False,None)
            #Vérification de 

        if self.grille.gagne():
            self.running = False
            print('Le joueur %s à gagner' % self.grille.gagne()[1])


    def display(self):
        """Affichage du jeu"""
        #Fond Blanc
        self.screen.fill('white')
        #Afffiche la grille
        self.grille.display()
        if self.selection[0]:
            #Dessine le rectangle de sélection
            pygame.draw.rect(self.screen,'black',(self.grille.marge[0] + self.grille.size()[0] * self.selection[1],
                                                  self.grille.marge[1],
                                                  self.grille.size()[0],
                                                  self.grille.size()[1] * self.grille.hauteur_tab()),
                                                  5)
        #Mis à jour de l'écran
        pygame.display.update()


    def run(self):
        while self.running:
            #print(pygame.mouse.get_pos())
            self.event()
            self.display()

pygame.init()

g = Game()
g.run()

pygame.quit
