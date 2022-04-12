liste_des_étudiant = []
liste_des_course = []

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

class course : 
    def __init__ (self , nom , id ,notes):
        self.nom = nom
        self.id  = id
        self.notes = notes
    def print_details(self):
        print("Course name:" + self.nom)
        print("Course id :" + self.id)
        print("Course mark:" + self.notes)

        
def Entrez_le_numéro_de_létudiants():
    numbres_des_étudiants = int(input("Entrez le numéro du étudiant: "))
    return numbres_des_étudiants
 
    
def entrez_les_informations_des_létudiant():
    numbres_des_étudiants = Entrez_le_numéro_de_létudiants()
    for i in range(0,numbres_des_étudiants):
        nom = input("Entrez le nom de l'étudiant: ")
        age = input("Entrez l'âge de l'étudiant: ")
        ddn = input("Entrez le date de naissance: ")
        id = input("Entrez le nom de l'étudiant: ")
        student_info = étudiant(nom,age,ddn,id)
        liste_des_étudiant.append(student_info)
        print("\n")
    
def liste_des_étudiants():
    for i in range(0,len(liste_des_étudiant)):
        print("Numéro ",i+1)
        print("Nom de l'étudiant : " + liste_des_étudiant[i].nom)
        print("Date de naissance de l'étudiant : " + liste_des_étudiant[i].ddn)
        print("Id de l'étudiant : " + liste_des_étudiant[i].id)
        print("\n")
    
def Entrez_le_numéro_du_cours():
    le_numéro_du_cours = int(input("Entrez le numéro du cours: "))
    return le_numéro_du_cours

def entrez_les_informations_des_courses():
    le_numéro_du_cours = Entrez_le_numéro_du_cours()
    for i in range(0,le_numéro_du_cours):
        nom = input("Entrez le nom du cours: ")
        id  = input("Entrez l'identifiant du cours : ")
        notes = input("Entrez la note du cours: ")
        informations_du_cours= course(nom,id, notes)
        liste_des_course.append(informations_du_cours)
        print("\n") 
    
def liste_des_courses():
    for i in range(0,len(liste_des_course)):
        print("Numeró  ",i+1)
        print("Le mom du course : " + liste_des_course[i].nom)
        print("Le id du course: " + liste_des_course[i].id)
        print("Le notes du course : " + liste_des_course[i].notes)
        print("\n")
 


entrez_les_informations_des_létudiant()
entrez_les_informations_des_courses()
liste_des_étudiants()
liste_des_courses()
