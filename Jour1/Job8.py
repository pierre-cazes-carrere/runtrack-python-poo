import math

class Cercle:
    def __init__(self, rayon):
# Attribution du rayon au cercle pour sa création.
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
# Permet de modifier le rayon du cercle.
        self.rayon = nouveau_rayon

    def afficherInfos(self):
# Affiche toutes les informations des deux cercles.
        print(f"Cercle de rayon : {self.rayon}")

# Calcule avec 2 x pi x rayon.
    def circonference(self):
# Calcule et retourne la circonférence du cercle..
        return 2 * math.pi * self.rayon

    def diametre(self):
# Calcule et retourne le diamètre du cercle.
        return 2 * self.rayon

    def aire(self):
# Calcule et retourne l'aire du cercle.
        return math.pi * (self.rayon ** 2)


# Création de deux cercles avec les rayons 4 et 7
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour le premier cercle
print("Cercle 1 :")
cercle1.afficherInfos()
print("Circonférence :", cercle1.circonference())
print("Diamètre      :", cercle1.diametre())
print("Aire          :", cercle1.aire())

print("\nCercle 2 :")
# Affichage des informations pour le deuxième cercle
cercle2.afficherInfos()
print("Circonférence :", cercle2.circonference())
print("Diamètre      :", cercle2.diametre())
print("Aire          :", cercle2.aire())


# ! EXERCICE COMPRIS MAIS PAS FAIT TOUT SEUL, JE L'AI VU SUR INTERNET POUR LE METTRE EN PLACE ! 