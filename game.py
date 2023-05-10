import pygame
from pygame.locals import *
from data.objects.grille import Grille
from data.module.selection import Selection
from data.module.victory import Victory
import random

class Game():
    
    def __init__(self,screen,size,sprite_1,sprite_2) -> None:
        """
        Initialise une partie

        Args:
            screen (pygame.display): Ecran du jeu
        
        Attributes:
            running (bool): 
                True:partie en cours
                False:patie fini
            screen (pygame.display): Ecran du jeu 
            self.grille ()
            
        """
        pygame.display.set_caption('Pyssance 4')
        pygame.display.set_icon(pygame.image.load('data/image/logo/logo.png'))
        #Attributes
        self.running = True
        self.screen = screen
        self.sprite_1 = sprite_1
        self.sprite_2 = sprite_2
        self.grille = Grille(self.screen,size,4,sprite_1,sprite_2)
        self.clock = pygame.time.Clock()
        print(type(self.grille))
        self.selection = None #Si la sourie survole une colone
        self.gagnant = None
        #Affichage selection du premier joueur
        self.joueur = Selection(self.screen,self.clock,self.sprite_1,self.sprite_2,self.grille).run()
        self.colone = None
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
                    if self.colone != (pygame.mouse.get_pos()[0] - self.grille.marge[0])//self.grille.size()[0]: 
                        self.colone = (pygame.mouse.get_pos()[0] - self.grille.marge[0])//self.grille.size()[0]    
                        print('colone %s' % ((pygame.mouse.get_pos()[0] - self.grille.marge[0])//self.grille.size()[0]))
                    #Stockage de la colonne où est la sourie
                    self.selection = (pygame.mouse.get_pos()[0] - self.grille.marge[0])//self.grille.size()[0]
                    #Si il clic, ajoute un  jeton sur la colonne selectionnée
                    if event.type == pygame.MOUSEBUTTONUP:
                        if self.grille.pleine(self.selection):
                            print('colonne %s pleine' % self.selection)
                        else:
                            self.selection = self.selection
                            self.grille.ajout_jeton(self.selection,self.joueur)
                            if self.joueur == 1:
                                self.joueur = 2
                            else:
                                self.joueur = 1
                            print('Au tour du joueur %s' % self.joueur)
            else:
                self.selection = None
        
        #Victoire
        if self.grille.gagne():
            self.running = False
            self.gagnant = self.grille.gagne()[1]
            print('Le joueur %s à gagner' % self.grille.gagne()[1])

        #Egalité
        elif self.grille.grille_pleine() and self.grille.gagne() != True:
            self.running = False
            self.gagnant = 0

    def display(self) -> None:
        """Affichage du jeu"""
        self.clock.tick()
        #Fond Blanc
        self.screen.fill('white')
        #Afffiche la grille
        self.grille.display()
        if self.selection != None:
            #Dessine le rectangle de sélection
            pygame.draw.rect(self.screen,'black',(self.grille.marge[0] + self.grille.size()[0] * self.selection,
                                                  self.grille.marge[1],
                                                  self.grille.size()[0],
                                                  self.grille.size()[1] * self.grille.hauteur_tab()),
                                                  5)
        
        pygame.display.update()
        #Affichage de l'écrna de victoire
        if self.gagnant != None:
            pygame.time.wait(750)
            if self.gagnant == 1:
                ecran_victoire = Victory(self.screen,self.grille,self.sprite_1)
                ecran_victoire.run()
            if self.gagnant == 2:
                ecran_victoire = Victory(self.screen,self.grille,self.sprite_2)
                ecran_victoire.run()

    def run(self) -> None:
        """Boucle du jeu"""
        while self.running:
            self.clock.tick(30)
            self.event()
            self.display()

pygame.init()
pygame.font.init()


ecrans = pygame.display.Info()
ecran_Info = (ecrans.current_w,ecrans.current_h)

sprite_1 = pygame.image.load('data/image/jetons/jeton_Kirby.png')
sprite_2 = pygame.image.load('data/image/jetons/jeton_MetaKnight.png')



g = Game(pygame.display.set_mode((800,500)),(7,6),
         sprite_1,
         sprite_2)
g.run()

pygame.quit()
