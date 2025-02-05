class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    # Assesseurs (getters)
    def get_marque(self):
        return self.__marque
    
    def get_modele(self):
        return self.__modele
    
    def get_annee(self):
        return self.__annee
    
    def get_kilometrage(self):
        return self.__kilometrage
    
    def get_en_marche(self):
        return self.__en_marche
    
    def get_reservoir(self):
        return self.__reservoir

    # Mutateurs (setters)
    def set_marque(self, marque):
        self.__marque = marque
    
    def set_modele(self, modele):
        self.__modele = modele
    
    def set_annee(self, annee):
        self.__annee = annee
    
    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage
    
    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche
    
    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    # Méthode privée pour vérifier le niveau de carburant
    def __verifier_plein(self):
        return self.__reservoir
    
    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Réservoir trop bas, impossible de démarrer.")
    
    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print("La voiture est arrêtée.")

# Instanciation et test de la classe
voiture1 = Voiture("Toyota", "Corolla", 2020, 30000)
voiture1.demarrer()
voiture1.arreter()
