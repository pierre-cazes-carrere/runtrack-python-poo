class Point:
    def __init__(self, x, y):
# Attribution des valeurs aux attributs de l'objet
        self.x = x
        self.y = y

# 1 Appeler la méthode voulu pour afficher les points avec leurs coordonnées
    def afficherLesPoints(self):
        print(f"Les coordonnées du point sont : x = {self.x}, y = {self.y}")

# 2 Coordonnées Individuelles
    def afficherX(self):
        print(f"La coordonnée x est : {self.x}")

    def afficherY(self):
        print(f"La coordonnée y est : {self.y}")

# 3 Changement des coordonnées a appeler a ligne 33-34

    def changerX(self, nouvelle_valeur):
        self.x = nouvelle_valeur

    def changerY(self, nouvelle_valeur):
        self.y = nouvelle_valeur

# 1 première valeure de départ x - y
point = Point(5, 10)
point.afficherLesPoints()  

# 2 Affiche cordonnées Individuelles
point.afficherX()       
point.afficherY()          

# 3 Seconde valeure de changement x - y
point.changerX(15)
point.changerY(20)
point.afficherLesPoints()  