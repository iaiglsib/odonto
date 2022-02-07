from AnalysePatient import AnalysePatient


from datetime import datetime


def consultation():
    print("Informations du Patient")

    id = input("Id du patient : ")
    nom = input("Nom : ")
    age = -1
    sex = 'D'
    while (int(age) < 0):
        age = int(input("Age : "))
        if (int(age) > 0):

            while sex != 'M' or sex != 'F':
                sex = input("Sexe (M pour Homme et F pour Femme) : ")
                if (sex == 'M') or (sex == 'F'):
                    print("Donnees du patient enregistrees. \n")
                    break
            break


    print("Analyses ")
    test_sensibilite1 = "Rien"

    while test_sensibilite1 != "Positif" or test_sensibilite1 != "Negatif" :
        test_sensibilite1 = input("Test de sensibilite1 (Positif ou Negatif) : ")                    #test_de_percution_axiale, test_de_palpation_abucale
        if (test_sensibilite1 == "Positif" or test_sensibilite1 == "Negatif"):
            test_sensibilite2, test_sensibilite3 = "", ""
            while test_sensibilite2 != "Douloureux " or test_sensibilite2 != "Non_Douloureux":
                test_sensibilite2 = input("Test de sensibilite2 (Douloureux ou Non_Douloureux) : ")
                if (test_sensibilite2 == "Douloureux" or test_sensibilite2 == "Non_Douloureux"):
                    while test_sensibilite3 != "Remanent " or test_sensibilite3 != "Non_Remanent":
                        test_sensibilite3 = input("Test de sensibilite3 (Remanent ou Non_Remanent) : ")
                        if (test_sensibilite3 == "Remanent" or test_sensibilite3 == "Non_Remanent" ) :
                            test_de_percution_axiale = ""
                            while test_de_percution_axiale != "Positif " or test_de_percution_axiale != "Negatif":
                                test_de_percution_axiale = input("Test de percution axiale (Positif ou Negatif) : ")
                                if (test_de_percution_axiale == "Positif" or test_de_percution_axiale == "Negatif") :
                                    test_de_palpation_apicale = ""
                                    while test_de_palpation_apicale != "Positif " or test_de_palpation_apicale != "Negatif":
                                        test_de_palpation_apicale = input("Test de palpation apicale (Positif ou Negatif) : ")
                                        if (test_de_palpation_apicale == "Positif" or test_de_palpation_apicale == "Negatif"):
                                            print("Resultats analyses enregistrees")
                                            patient = AnalysePatient(id=id,
                                                                     nom=nom,
                                                                     age=age,
                                                                     sexe=sex,
                                                                     date_consul= datetime.now(),
                                                                     test_sensibilite1=test_sensibilite1,
                                                                     test_sensibilite2=test_sensibilite2,
                                                                     test_sensibilite3=test_sensibilite3,
                                                                     test_de_percution_axiale=test_de_percution_axiale,
                                                                     test_de_palpation_apicale=test_de_palpation_apicale)
                                                                
                                            return patient
            break        
