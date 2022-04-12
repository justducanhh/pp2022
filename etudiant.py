liste_des_étudiant = []

class étudiant :
    def __init__(self, nom ,age,ddn, id):
        self.nom   = nom
        self.ddn    = ddn
        self.age    = age
        self.id     = id 

    def print_details(self):
        print("Nom de étudiant " + self.nom)
        print("ddn: " + self.ddn)
        print("id: " + self.id)
        print("age: " + self.age)


def Entrez_le_numéro_de_létudiants():
    numbres_des_étudiants = int(input("Entrez le numéro du étudiant: "))
    return numbres_des_étudiants
 
    
def entrez_les_informations_des_létudiant():
    numbres_des_étudiants = Entrez_le_numéro_de_létudiants()
    for i in range(0,numbres_des_étudiants):
        nom = input("Entrez le nom de l'étudiant: ")
        age = input("Entrer l'âge de l'étudiant: ")
        ddn = input("Entrez le date de naissance: ")
        id = input("Entrez le nom de l'étudiant: ")
        étudiant_info = étudiant(nom,age,ddn,id)
        liste_des_étudiant.append(étudiant_info)
        print("\n")
    
def liste_des_étudiants():
    for i in range(0,len(liste_des_étudiant)):
        print("Numéro ",i+1)
        print("Nom de l'étudiant : " + liste_des_étudiant[i].nom)
        print("Date de naissance de l'étudiant : " + liste_des_étudiant[i].ddn)
        print("Id de l'étudiant : " + liste_des_étudiant[i].id)
        print("\n")
        
entrez_les_informations_des_létudiant()