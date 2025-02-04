class Personnage:
    def __init__(self, x, y):
        # Le constructeur initialise la position (x, y)
        self.x = x
        self.y = y


    def droite(self):
# 1 Déplace le personnage vers la droite (augmente y)
        self.y += 1

    def bas(self):
# 2 Déplace le personnage vers le bas (diminue x)
        self.x -= 1

    def gauche(self):
# 3 Déplace le personnage vers la gauche (diminue y)
        self.y -= 1

    def haut(self):
# 4 Déplace le personnage vers le haut (augmente x)
        self.x += 1

    def position(self):
# Retourne la position actuelle sous forme de tuple (x, y)
        return (self.x, self.y)

# Instanciation de la position de 0.0
perso = Personnage(0, 0)
print("Position initiale :", perso.position())


#Récupere les données du tuple et l'affiche dans la console.
# 1 Déplacement vers la droite
perso.droite()
print("Après déplacement à droite :", perso.position())

# 2 Déplacement vers le bas
perso.bas()
print("Après déplacement en bas :", perso.position())

# 3 Déplacement vers la gauche
perso.gauche()
print("Après déplacement à gauche :", perso.position())

# 4 Déplacement vers le haut
perso.haut()
print("Après déplacement en haut :", perso.position())