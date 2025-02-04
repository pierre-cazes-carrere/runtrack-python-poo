class Animal:
    def __init__(self):

# 1 Attribut les valeurs de base donc 0.
        self.age = 0
        self.prenom = ""

# 2 Ajoute +1 si "Viellir" est appelé.
    def vieillir(self):

        self.age += 1

    def nommer(self, nom):
        # 4 Méthode qui attribue le nom passé en paramètre à l'animal
        self.prenom = nom
        print("Nom de l'animal:", self.prenom)

#Instance de la classe Animal.
mon_animal = Animal()

# 1 Appel de la valeur de base 
print("Âge initial:", mon_animal.age)

# 2 Une fois Animal appeler, change pour Vieillir.
mon_animal.vieillir()

# 3 Appel de la nouvelle valeure.
print("Âge après vieillir:", mon_animal.age)

# 4 Nommer l'animal.
mon_animal.nommer("Rex")