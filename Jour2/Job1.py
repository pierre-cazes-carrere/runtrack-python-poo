class Rectangle:
    def __init__(self, longueur, largeur):
        # Attributs privés
        self.__longueur = longueur
        self.__largeur = largeur

    # Accesseurs (getters)
    def get_longueur(self):
        return self.__longueur

    def get_largeur(self):
        return self.__largeur

    # Mutateurs (setters)
    def set_longueur(self, nouvelle_longueur):
        self.__longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur):
        self.__largeur = nouvelle_largeur

    # Méthode pour afficher les dimensions du rectangle
    def afficher(self):
        print(f"Rectangle: longueur = {self.__longueur} et largeur = {self.__largeur}")


# Création d'un rectangle avec longueur 10 et largeur 5
rect = Rectangle(10, 5)
print("Dimensions initiales :")
rect.afficher()

# Modification des attributs
rect.set_longueur(15)
rect.set_largeur(8)
print("\nDimensions après modification :")
rect.afficher()