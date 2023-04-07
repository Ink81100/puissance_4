from jeton import Jeton

class Grille():

    def __init__(self,largeur = 7,hauteur = 6,victoire = 4):
        """
        Initialise une grille de jeu.

        Args:
            largeur (int): Largeur de la grille.
            hauteur (int): Hauteur de la grille.
            victoire (int): nombre de jetons necessaire pour gagner

        Attributes:
            tab (list): Grille de jeu représentée sous la forme d'une liste de listes.
            Chaque élément de la sous-liste est un objet de la classe Jeton où son type peut avoir trois valeurs :
            0 : case vide,pard défault
            1 : jeton du joueur 1
            2 : jeton du joueur 2
            largeur (int): Largeur du tableau
            hauteur (int): Hauteur du tableau 
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

        #Création de la grille
        self.tab = [[Jeton() for _ in range(largeur)] for _ in range(hauteur)]
        
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
    
g1 = Grille(
)
print(g1)

print(g1)
print(g1.gagne())
