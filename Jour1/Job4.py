class Personnes:
  def __init__(self, nom, prenom):
    self.nom = nom
    self.prenom = prenom
  
  # méthode pour attribuer un nouveau nom et prenom
  def sePresenter(self):
     
    return f" {self.prenom} {self.nom}."
  #La classe Personnes a deux attributs
Personne1 = Personnes("Doe", "John")
Personne2 = Personnes("Dupont", "Jean")

#Les attributs sont appeler ici

print(Personne1.sePresenter())
print(Personne2.sePresenter())
