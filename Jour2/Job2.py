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
        print(f"Livre : titre = {self.__titre}, auteur = {self.__auteur}, nbPages = {self.__nb_pages}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un livre avec les valeurs initiales
    livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
    print("Livre initial :")
    livre.afficher()

    # Modification des attributs
    livre.set_titre("1984")
    livre.set_auteur("George Orwell")
    livre.set_nb_pages(328)
    print("\nLivre modifié :")
    livre.afficher()

    # Tentative de modification avec un nombre de pages négatif
    livre.set_nb_pages(-50)
    print("\nAprès tentative de modification avec nbPages négatif :")
    livre.afficher()
