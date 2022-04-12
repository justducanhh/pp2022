liste_des_course = []

class course : 
    def __init__ (self , nom , id ,notes, credits):
        self.nom = nom
        self.id  = id
        self.notes = notes
        self.credits = credits
    def print_details(self):
        print("Course name:" + self.nom)
        print("Course id :" + self.id)
        print("Course notes:" + self.notes)
        print("Course credits:" + self.credits)
def Entrez_le_numéro_du_cours():
    le_numéro_du_cours = int(input("Entrez le numéro du cours: "))
    return le_numéro_du_cours

def entrez_les_informations_des_courses():
    le_numéro_du_cours = Entrez_le_numéro_du_cours()
    for i in range(0,le_numéro_du_cours):
        nom = input("Entrez le nom du cours: ")
        id  = input("Entrez l'identifiant du cours : ")
        notes = input("Entrez la note du cours: ")
        crédits = input("Entrez le crédits du cours: ")
        informations_du_cours= course(nom,id, notes, crédits)
        liste_des_course.append(informations_du_cours)
        print("\n") 
    
def liste_des_courses():
    for i in range(0,len(liste_des_course)):
        print("Numeró  ",i+1)
        print("Le mom du course : " + liste_des_course[i].nom)
        print("Le id du course: " + liste_des_course[i].id)
        print("Le notes du course : " + liste_des_course[i].notes)
        print("Le crédits du course : " + liste_des_course[i].crédits)
        print("\n")


def gpa_calculator():
    sum_notes = 0
    sum_crédits = 0
    for i in range(0,len(liste_des_course)):
        sum_notes = sum_notes + int(liste_des_course[i].notes)
        sum_crédits = sum_crédits + int(liste_des_course[i].crédits)
    gpa = sum_notes/sum_crédits
    return gpa

def print_gpa():
    gpa = gpa_calculator()
    print("GPA: " + str(gpa))





entrez_les_informations_des_courses()
liste_des_courses()
print_gpa()


