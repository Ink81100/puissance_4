import pygame
from pygame.locals import *
from data.objects.grille import Grille
import random

class Hasard():

    def __init__(self,screen,clock,grille,sprite_1,sprite_2) -> None:
        
        ###Arguments
        #Stockage des Arguments en attributs
        self.screen = screen
        self.clock = clock
        self.grille = grille
        #Rectangle
        self.rectangle = pygame.rect.Rect(self.grille.marge[0],
                                          self.grille.marge[1],
                                          self.grille.size()[0] * self.grille.largeur_tab(),
                                          self.grille.size()[1] * self.grille.hauteur_tab())
        print(self.rectangle.size)
        #Sprites
        self.sprite_J1 = pygame.transform.scale(sprite_1,self.grille.size())
        self.sprite_J2 = pygame.transform.scale(sprite_2,self.grille.size())
        #Attributs
        self.contdown = random.randint(3,5)
        self.running = True
        self.choix = random.randint(1,2)
        self.afficher = 0
        self.select_sprite = 1
        #Texte
        self.police = pygame.font.SysFont('Arial',30)
        self.text = self.police.render('Le joueur %s démarre' % self.choix,
                               False,
                               (0,0,0))
        #Event du timer
        self.timer_event =  pygame.USEREVENT+1
        pygame.time.set_timer(self.timer_event,1000)

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == self.timer_event:
                self.contdown -= 1
                if self.contdown == 0:
                    self.running = False
    
    def display(self):
        self.clock.tick(60)
        self.screen.fill('white')

        if self.contdown != 0:
            if self.select_sprite == 1:
                self.select_sprite += 1
                self.screen.blit(self.sprite_J1,
                                   (self.rectangle.size[0]//2+self.grille.marge[0]-self.sprite_J1.get_width()//2,
                                    self.rectangle.size[1]//2+self.grille.marge[1]-self.sprite_J1.get_height()//2))
            else:
                self.select_sprite -= 1
                self.screen.blit(self.sprite_J2,
                                (self.rectangle.size[0]//2+self.grille.marge[0]-self.sprite_J1.get_width()//2,
                                 self.rectangle.size[1]//2+self.grille.marge[1]-self.sprite_J1.get_height()//2))

        elif self.contdown == 0:
            if self.choix == 1:
                self.screen.blit(self.sprite_J1,
                                (self.rectangle.size[0]//2+self.grille.marge[0]-self.sprite_J1.get_width()//2,
                                 self.rectangle.size[1]//2+self.grille.marge[1]-self.sprite_J1.get_height()//2))
            else:
                self.screen.blit(self.sprite_J2,
                                (self.rectangle.size[0]//2+self.grille.marge[0]-self.sprite_J1.get_width()//2,
                                 self.rectangle.size[1]//2+self.grille.marge[1]-self.sprite_J1.get_height()//2))
        pygame.display.update()
        pygame.time.wait(200)
        if self.contdown == 0:
            self.screen.blit(self.text,(0,0))
            pygame.display.update()
            pygame.time.wait(1500)
    def run(self) -> int:
        while self.running:
            self.event()
            self.display()
        return self.choix