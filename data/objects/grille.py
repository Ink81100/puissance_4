from data.objects.jeton import Jeton
import pygame 
from pygame.locals import *


class Grille():

    def __init__(self,screen,largeur = 7,hauteur = 6,victoire = 4,):
        """
        Initialise une grille de jeu.

        Args:
            largeur (int): Largeur de la grille.
            hauteur (int): Hauteur de la grille.
            victoire (int): nombre de jetons necessaire pour gagner
            screen: écran de pygame

        Attributes:
            tab (list): Grille de jeu représentée sous la forme d'une liste de listes.
            Chaque élément de la sous-liste est un objet de la classe Jeton où son type peut avoir trois valeurs :
            0 : case vide,pard défault
            1 : jeton du joueur 1
            2 : jeton du joueur 2
            largeur (int): Largeur du tableau
            hauteur (int): Hauteur du tableau 
            victoire (int): Nombre de jeton pour une victoire
            screen (pygame.screen): Ecran du jeu 
            marge (int): marge de la grille sur l'écran
            facteur_redim(float): facteur dee redimension appliquer à la grille
                                dans le cas où elle dépasserais de la fenêtre
            carreau (pygame.surface): sprite d'un carreau d la grille
        """
        ###Vérification des paramètres
        #Vérification du type
        assert type(largeur) == int,'largeur doît être un entier' 
        assert type(hauteur) == int,'hauteur doît être un entier'
        assert type(victoire) == int, 'Victoire doit être un entier'
        
        #Vérification de la valeur
        assert largeur >= 4,'largeur < 4' 
        assert hauteur >= 4,'hauteur < 4'
        assert victoire >= 4,'hauteur < 4'

        #Stockage des arguments en attribut
        self.largeur = largeur
        self.hauteur = hauteur 
        self.victoire = victoire
        self.screen = screen

        #Sprite de la grille
        Grille.sprite = pygame.image.load('data/image/jetons/CaseGrille.png')
        
        #facteur de rétrécissement
       
        
        self.l_f = int(min(0.7 * self.screen.get_width()//self.largeur,
                                0.7 * self.screen.get_height()//self.hauteur))

        self.marge = (int((self.screen.get_width() - (self.l_f * self.largeur))//2),
                      int((self.screen.get_height() - (self.l_f * self.hauteur))//2))

        self.carreau = pygame.transform.scale(Grille.sprite,
                                              (self.l_f,self.l_f))

        #Création de la grille de jeton
        self.tab = [[Jeton(screen,0,self.l_f) for _ in range(self.largeur)]
                    for _ in range(self.hauteur)]
        
    def size(self) -> tuple:
        """Renvois la taille """
        return (self.carreau.get_width(),
                self.carreau.get_height())

    def hauteur_tab(self) -> int:
        """renvois la hauteur de la grille"""
        return self.hauteur
    
    def largeur_tab(self) -> int:
        """renvois la largeur de la grille"""
        return self.largeur
    
    def pleine(self,colonne) -> bool:
        """vérifie si la colone est pleine oui où non"""
        for ligne in range(self.hauteur_tab()):
            if self.tab[ligne][colonne].type() == 0:
                return False
            return True

    def grille_pleine(self) -> bool:
        """
        vérifie si la grille est pleine

        Return:
            bool: 
                True: la grille est pleine
                False: la grille n'est pas pleine
        """
        for i in range(self.largeur):
            if self.pleine(i):
                return True
        return False


    def ajout_jeton(self,y,jeton = 0):
        """
        Ajoute un jeton dans la grille de jeu.

        Args:
            y (int): Coordonnée de la colonne où ajouter le jeton.
            jeton (int): Type du jeton à ajouter (0 : vide, 1 : joueur 1, 2 : joueur 2). Par défaut, le jeton ajouté est vide.

        Var:
            depose (bool): permet de vérifiée si le jeton à été déposé

        Conditions d'ajout d'un jeton:
            - Un jeton ne peut être ajouté que s'il n'y a pas déjà un jeton à l'endroit voulu.
            - Il lui faut un jeton en dessous de lui ou qu'il soit en première ligne.
            - La coordonnée entrée doit exister dans la grille.
            - La colonne donnée ne doit pas être pleine.
        """
        ###Vérification des paramètres
        #Vérification du type 
        assert type(y) == int,"la coordonnées de la colonne n'est pas un entier"
        
        #Vérification de l'existence des coordonnées données
        if y > self.hauteur_tab() or y < 0:
            print('coordonnées de colonne entré inexistante')

        #Vérification si la colone sélectionnée n'est pas pleine 
        if self.pleine(y):
            print('colone %s pleine' % y)           
        else:
            #Création de la variable depose
            depose = False
            ###Ajout du jeton
            for i in range(-1,-len(self.tab)-1,-1):
                if self.tab[i][y].type() == 0 and depose == False:
                    self.tab[i][y].type_update(jeton)
                    print("jeton de type %s placer en(%s,%s)" % (jeton,(-i)-1,y))
                    depose = True

    def gagne(self) -> tuple:
        """
        Vérifie si il y une victoire

        Returns:
            tuple: len = 2 
                [0] (bool):
                    True:Il y une victoire
                    False:Il n'y pas de victoire

                [1] (int):
                    1:J1 gagnant
                    2:J2 gagnant
        """
        ###Vérification des différent cas de victoires
        #Ligne
        for i in self.tab:
            for j in range(self.largeur_tab() - self.victoire+1):
                if (i[0 + j].type() ==  i[1+ j].type() and i[1+ j].type() == i[2 + j].type() and i[1+ j].type() == i[2 + j].type() and i[2 + j].type() == i[3 + j].type() and i[0 + j].type() != 0):
                    return (True,i[0 + j].type())
        #Colone
        for i in range(self.largeur_tab()):
            for j in range(self.hauteur_tab()-self.victoire+1):
                if (self.tab[0+j][i].type() == self.tab[1+j][i].type() and self.tab[1+j][i].type() == self.tab[2+j][i].type() and self.tab[2+j][i].type() == self.tab[3+j][i].type() and self.tab[0+j][i].type() != 0):
                    return (True,self.tab[0+j][i].type())
        #Diagonale ->^
        for i in range(-1,-self.hauteur_tab(),-1):
            for j in range(self.largeur_tab()):
                if self.hauteur_tab() - 1 + i >= 4:
                    if self.largeur_tab() - j >= 4:
                        if (self.tab[i][j].type() == self.tab[i-1][j+1].type() and self.tab[i-1][j+1].type() == self.tab[i-2][j+2].type() and self.tab[i-2][j+2].type() == self.tab[i-3][j+3] and self.tab[i][j].type() != 0):
                            return (True,self.tab[i][j].type())
        #Diagonale ->|
        for i in range(self.hauteur_tab()):
            for j in range(self.largeur_tab()):
                if self.hauteur_tab() - i >= 4:
                    if self.largeur_tab() - j >= 4:
                        if (self.tab[i][j].type() == self.tab[i+1][j+1].type() and self.tab[i+1][j+1].type() == self.tab[i+2][j+2].type() and self.tab[i+2][j+2].type() == self.tab[i+3][j+3].type() and self.tab[i][j].type() != 0):
                            return (True,self.tab[i][j].type())

    def display(self):
        """Affiche la grille et les jeton à l'intérieur"""

        #Affichage de la grille            
        for x in range(self.marge[0],self.largeur_tab()*self.size()[0] + self.marge[0],self.size()[0]):
            for y in range(self.marge[1],self.hauteur_tab()*self.size()[1] + self.marge[1],self.size()[1]):
                self.screen.blit(self.carreau, (x, y))
        
        #Affichage des jetons
        for i in range(self.hauteur_tab()):
            for j in range(self.largeur_tab()):
                self.tab[i][j].display(self.marge[0] + j * self.size()[0],
                             self.marge[1] + i * self.size()[1])

    def __str__(self):
        """
        Renvoie une représentation de la grille sous forme de chaîne de caractères.

        Returns:
            str: la grille sous forme de tableau affichable dans la console.
        Variables:
            tab_str (str): La chaîne de caractères stockant la grille sous forme de tableau.
        """
        tab_str = ''
        temp_l = []
        for i in self.tab:
            for j in range(self.largeur_tab()):
                temp_l.append(i[j].type())
            tab_str += (str(temp_l)+'\n')#On concationne  pour les afficher comme un tableau dans la console
            temp_l = []
        return str(tab_str)
