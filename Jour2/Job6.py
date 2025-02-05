class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats = {}  # Dictionnaire contenant les plats commandés
        self.__statut = "En cours"  # Statut initial de la commande

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix):
        if prix > 0:
            self.__plats[nom_plat] = prix
            print(f"Plat {nom_plat} ajouté à la commande.")
        else:
            print("Erreur : Le prix du plat doit être supérieur à zéro.")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        self.__statut = "Annulée"
        self.__plats.clear()
        print("Commande annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        return sum(self.__plats.values())

    # Méthode pour afficher les informations de la commande
    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Commande N°{self.__numero_commande}\nStatut : {self.__statut}\nPlats commandés :")
        for plat, prix in self.__plats.items():
            print(f"- {plat} : {prix} €")
        print(f"Total à payer : {total} € (hors TVA)")

    # Méthode pour calculer la TVA
    def calculer_tva(self, taux_tva=0.2):
        total = self.__calculer_total()
        tva = total * taux_tva
        print(f"TVA ({taux_tva*100}%) : {tva} €")
        return tva

# Instanciation et test de la classe
commande1 = Commande(101)
commande1.ajouter_plat("Pizza", 12)
commande1.ajouter_plat("Pâtes", 10)
commande1.afficher_commande()
commande1.calculer_tva()
commande1.annuler_commande()
commande1.afficher_commande()
