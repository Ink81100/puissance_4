import pygame

class Jeton():

    def __init__(self,sorte = 0) -> None:
        """
        Iniltialise un jeton

        Args:
            sorte (int): entier qui définit le type du jeton
                3 valeurs possibles:
                    0: vide, par défault
                    1: joueur 1
                    2: joueur 2
        
        Attributes:
            sorte (int): type du jeton
        """
        ###Vérification des paramètres
        assert type(sorte) == int,'sorte du jeton de type incorrect(%s)' % sorte

        ###
        self.sorte = sorte
        #self.sprite = pygame.transform.scale(pygame.image.load('data/image/jetons/token_empty.png',(64,64)))

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

