class Operation:
  def __init__(self, nombre1=12, nombre2=3):
    self.nombre1 = nombre1
    self.nombre2 = nombre2
  
  # ajout de str avec bonne identation et le /n pour revenir a la ligne
  def __str__(self):
        return f"Le nombre 1 est {self.nombre1}\nLe nombre 2 est {self.nombre2}"
  
  def addition(self):
     
     resultat = self.nombre1 + self.nombre2
     print("La somme des deux nombres est de :", resultat )

#instanciation pour manipuler l'objet
op = Operation()

#print l'opperation
print(op)

#appel de la definition addition
op.addition()