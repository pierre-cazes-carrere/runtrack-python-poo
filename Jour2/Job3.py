class Livre:
    def __init__(self, titre, auteur, nb_pages):
        # Attributs privés
        self.__titre = titre
        self.__auteur = auteur
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être positif. Valeur par défaut utilisée : 1")
            self.__nb_pages = 1
        # Attribut privé 'disponible' initialisé par défaut à True
        self.__disponible = True

    # Accesseurs (getters)
    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_nb_pages(self):
        return self.__nb_pages

    # Mutateurs (setters)
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nb_pages(self, nb_pages):
        if nb_pages > 0:
            self.__nb_pages = nb_pages
        else:
            print("Erreur : le nombre de pages doit être positif. La valeur n'a pas été modifiée.")

    # Méthode pour afficher les attributs du livre
    def afficher(self):
        print(f"Livre : titre = {self.__titre}, auteur = {self.__auteur}, nbPages = {self.__nb_pages}, disponible = {self.__disponible}")

    # Méthode de vérification de disponibilité
    def verification(self):
        """Retourne True si le livre est disponible, False sinon."""
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        """
        Emprunte le livre en le rendant indisponible.
        Vérifie d'abord (via verification()) que le livre est disponible.
        """
        if self.verification():
            self.__disponible = False
            print("Livre emprunté avec succès.")
        else:
            print("Le livre est déjà emprunté et donc indisponible.")

    # Méthode pour rendre le livre emprunté
    def rendre(self):
        """
        Rend le livre en le rendant disponible.
        Vérifie d'abord (via verification()) que le livre a été emprunté.
        """
        if not self.verification():
            self.__disponible = True
            print("Livre rendu avec succès.")
        else:
            print("Ce livre n'a pas été emprunté.")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un livre avec les valeurs initiales
    livre = Livre("1984", "George Orwell", 328)
    print("État initial du livre :")
    livre.afficher()
    print("Vérification de disponibilité :", livre.verification())

    # Emprunter le livre
    print("\nTentative d'emprunt :")
    livre.emprunter()
    livre.afficher()
    print("Vérification de disponibilité :", livre.verification())

    # Tentative d'emprunt d'un livre déjà emprunté
    print("\nNouvelle tentative d'emprunt :")
    livre.emprunter()

    # Rendre le livre
    print("\nTentative de retour :")
    livre.rendre()
    livre.afficher()
    print("Vérification de disponibilité :", livre.verification())

    # Tentative de rendre un livre qui n'est pas emprunté
    print("\nNouvelle tentative de retour :")
    livre.rendre()
