class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = 0
        self.__level = self.__student_eval()
    
    def add_credits(self, credits):
        if credits > 0:
            self.__credits += credits
            self.__level = self.__student_eval()  # Mettre à jour le niveau après l'ajout des crédits
        else:
            print("Erreur : Le nombre de crédits ajouté doit être supérieur à zéro.")
    
    def get_credits(self):
        return self.__credits
    
    def __student_eval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"
    
    def student_info(self):
        print(f"Nom : {self.__nom}\nPrénom : {self.__prenom}\nID Étudiant : {self.__numero_etudiant}\nNiveau : {self.__level}")

# Instanciation de l'étudiant John Doe
john_doe = Student("Doe", "John", 145)

# Ajout de crédits à trois reprises
john_doe.add_credits(10)
john_doe.add_credits(20)
john_doe.add_credits(30)

# Affichage des informations de l'étudiant
john_doe.student_info()
