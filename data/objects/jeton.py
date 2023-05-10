import pygame
import math

class Jeton():

    def __init__(self,screen,sorte = 0,carreau_l = 72,marge = 40,
                 sprite_1 = pygame.image.load('data/image/jetons/jeton_Jaune.png'),
                 sprite_2 = pygame.image.load('data/image/jetons/jeton_Rouge.png')) -> None:
        """
        Iniltialise un jeton

        Args:
            sorte (int): entier qui définit le type du jeton
                3 valeurs possibles:
                    0: vide, par défault
                    1: joueur 1
                    2: joueur 2
            f (float): nombre flotant du facteur de redimension du jeton
        Attributes:
            sorte (int): type du jeton
            f (float): nombre flotant du facteur de redimension du jeton
            screen (): écran
        """
        ###Vérification des paramètres
        assert type(sorte) == int,'sorte du jeton de type incorrect(%s)' % sorte

        ###Attributs
        self.sorte = sorte
        self.screen = screen
        self.carreau_l = carreau_l
        self.marge = marge
        self.sprite = pygame.image.load('data/image/jetons/BlancRond.png')
        self.sprite_f = pygame.transform.scale(self.sprite,(((self.carreau_l * self.sprite.get_width())//72),
                                               ((self.carreau_l *self.sprite.get_height())//72)))
        #Sprites des jetons
        self.sprite_1 = sprite_1
        self.sprite_2 = sprite_2

    def type(self) -> int:
        """Renvois le type du jeton"""
        return self.sorte
    
    def type_update(self,n_type):
        """
        Met à jours le type du jeton 

        Args:
            n_type (int): nouvelle valeurs du jeton
        """
        ###Vérification des Arguments
        #Vérification du type
        assert type(n_type) == int,'nouveau type du jeton incorrect'
        #Vérification des valeurs
        assert n_type == 0 or n_type == 1 or n_type == 2,'Valeur du nouveau type du jeton incorrect'
        self.sorte = n_type
        if self.sorte == 1:
            self.sprite = self.sprite_1
        elif self.sorte == 2:
            self.sprite = self.sprite_2
        else:
            self.sprite = pygame.image.load('data/image/jetons/BlancRond.png')

        self.sprite_f = pygame.transform.scale(self.sprite,(math.ceil((self.carreau_l *self.sprite.get_width())/72),
                                               math.ceil((self.carreau_l *self.sprite.get_height())/72)))

    def size(self) -> tuple:
        """Renvois la taille du jeton"""
        return (self.sprite_f.get_width(),self.sprite_f.get_height())

    def display(self,x,y):
        """Affiche le jeton"""
        if self.sorte != 0:
            self.screen.blit(self.sprite_f,(x + ((self.carreau_l - self.size()[0])/2),
                                            y + ((self.carreau_l - self.size()[0])/2)))