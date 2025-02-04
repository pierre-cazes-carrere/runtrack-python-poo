class Produit:
    def __init__(self, nom, prixHT, TVA):
        # Initialisation des attributs
        self.nom = nom            
        self.prixHT = prixHT      
        self.TVA = TVA            

    def calculerPrixTTC(self):
# Calcule le prix TTC 
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
# Donne les détails du produits en format string
        info = (
            f"Nom: {self.nom}, "
            f"Prix HT: {self.prixHT:.2f}, "
            f"TVA: {self.TVA}%, "
            f"Prix TTC: {self.calculerPrixTTC():.2f}"
        )
        return info

    def modifierNom(self, nouveau_nom):
# Modifie le nom du produit
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prix):
# Modifie le prix HT du produit
        self.prixHT = nouveau_prix

    def getNom(self):
# Retourne le nom du produit
        return self.nom

    def getPrixHT(self):
# Retourne le prix HT du produit
        return self.prixHT

    def getTVA(self):
# Retourne le taux de TVA du produit
        return self.TVA


# Attribution de plusieurs produits avec leur caractéristiques
produit1 = Produit("Produit A", 100, 20)
produit2 = Produit("Produit B", 50, 10)
produit3 = Produit("Produit C", 200, 5)

# Affichage des informations de chaque produit
print("Informations initiales :")
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Modification du nom et du prix de chaque produit
produit1.modifierNom("Produit A - Nouvelle édition")
produit1.modifierPrixHT(120)

produit2.modifierNom("Produit B - Version améliorée")
produit2.modifierPrixHT(55)

produit3.modifierNom("Produit C - Édition spéciale")
produit3.modifierPrixHT(210)

# Affichage des informations après modification
print("\nAprès modifications :")
print(produit1.afficher())
print(produit2.afficher())
print(produit3.afficher())

# Affichage du nouveau prix TTC pour chaque produit
print("\nNouveaux prix TTC :")
print(f"{produit1.getNom()} : {produit1.calculerPrixTTC():.2f}")
print(f"{produit2.getNom()} : {produit2.calculerPrixTTC():.2f}")
print(f"{produit3.getNom()} : {produit3.calculerPrixTTC():.2f}")
