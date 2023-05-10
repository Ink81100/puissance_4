import pygame
import sys
from data.module.hasard import Hasard

class Selection():
    def __init__(self, screen,clock, sprite_J1, sprite_J2, grille):
        """
        Initialise un menu de selection

        Args:
            screen (pygame.Surface): Ecran du jeu 
            sprite_J1/J2 (pygame.Surface): Sprites des jetons des joueur
            grille (Class.Grille): Grille du jeu
        """
        self.screen = screen
        self.grille = grille
        self.running = True
        self.premier_joueur = 0
        self.clock = clock

        # Sprites
        self.sprite_J1 = pygame.transform.scale(sprite_J1, self.grille.size())
        self.sprite_J2 = pygame.transform.scale(sprite_J2, self.grille.size())
        self.sprite_H = pygame.transform.scale(pygame.image.load('data/image/jetons/jeton_Placebo.png'), self.grille.size())

        # Boîtes de collision
        self.hitbox_J1 = pygame.Rect(self.screen.get_width() // 2 - self.sprite_J1.get_width() - self.sprite_J1.get_width() * 0.1 - self.sprite_J1.get_width(),
                                     self.screen.get_height() // 2 + self.sprite_J1.get_height() // 2,
                                     self.sprite_J1.get_width(),
                                     self.sprite_J1.get_height())

        self.hitbox_J2 = pygame.Rect(self.screen.get_width() // 2 + self.sprite_J2.get_width() + self.sprite_J2.get_width() * 0.1,
                                     self.screen.get_height() // 2 + self.sprite_J2.get_height() // 2,
                                     self.sprite_J2.get_width(),
                                     self.sprite_J2.get_height())

        self.hitbox_H = pygame.Rect(self.screen.get_width() / 2 - self.sprite_H.get_width() / 2,
                                    self.screen.get_height() /2 + self.sprite_H.get_height() // 2,
                                    self.sprite_H.get_width(),
                                    self.sprite_H.get_height())

    def event(self):
        #Fermer la fenetre
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                sys.exit()
            #Clic sur les jetons 
            elif event.type == pygame.MOUSEBUTTONUP:
                    print('clic')
                    if self.hitbox_J1.collidepoint(pygame.mouse.get_pos()):
                        print('clic sur la boîte de J1')
                        self.premier_joueur = 1
                    elif self.hitbox_J2.collidepoint(pygame.mouse.get_pos()):
                        print('clic sur la boîte de J2')
                        self.premier_joueur = 2
                    elif self.hitbox_H.collidepoint(pygame.mouse.get_pos()):
                        print('clic sur le jeton hasard')
                        self.premier_joueur = Hasard(self.screen,self.clock,self.grille,self.sprite_J1,self.sprite_J2).run()
                    self.running = False

    def display(self):
        # Affichage des sprites
        self.screen.blit(self.sprite_J1, self.hitbox_J1)
        self.screen.blit(self.sprite_J2, self.hitbox_J2)
        self.screen.blit(self.sprite_H, self.hitbox_H)
        # Mise à jour de l'écran
        pygame.display.update()

    def run(self):
        while self.running:
            self.event()
            self.display()
        return self.premier_joueur