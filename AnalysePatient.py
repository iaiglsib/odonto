from datetime import datetime

from Patient import Patient

class AnalysePatient(Patient):
    dico = dict()
    maladies = list()

    def __init__(self, id, nom, age, sexe, test_sensibilite1, test_sensibilite2, test_sensibilite3, test_de_percution_axiale, test_de_palpation_apicale, date_consul: datetime.now()):
        Patient.__init__(self, id, nom, age, sexe)
        self.test_sensibilite1 = test_sensibilite1
        self.test_sensibilite2 = test_sensibilite2
        self.test_sensibilite3 = test_sensibilite3
        self.test_de_percution_axiale = test_de_percution_axiale
        self.test_de_palpation_apicale = test_de_palpation_apicale 
        self.dat_consul = date_consul
        self.maladies = []
        self.dico = self.resultat()

    def Analyse(self):
        if (self.test_sensibilite1 == "Positif") and (self.test_sensibilite2 == "Douloureux") and (self.test_sensibilite3 == "Non_Remanent") and (self.test_de_percution_axiale == "Negatif") and (self.test_de_palpation_apicale == "Negatif"):
            self.maladies.append("Pulpite_réversible")
            return "Pulpite_réversible"
        elif (self.test_sensibilite1 == "Positif") and (self.test_sensibilite2 == "Douloureux") and (self.test_sensibilite3 == "Remanent") and (self.test_de_percution_axiale == "Negatif") and (self.test_de_palpation_apicale == "Negatif"):
            self.maladies.append("Pulpite_aigue")
            return "Pulpite_aigue"
        elif (self.test_sensibilite1 == "Positif") and (self.test_sensibilite2 == "Douloureux") and (self.test_sensibilite3 == "Remanent") and (self.test_de_percution_axiale == "Positif") and (self.test_de_palpation_apicale == "Negatif"):
            self.maladies.append("Pulpite_aigue_et_parodontite_apicale_aigue_initiale")
            return "Pulpite_aigue_et_parodontite_apicale_aigue_initiale"
        elif (self.test_sensibilite1 == "Positif" or self.test_sensibilite1 == "Negatif" ) and (self.test_sensibilite2 == "Douloureux") and (self.test_sensibilite3 == "Non_Remanent") and (self.test_de_percution_axiale == "Negatif") and (self.test_de_palpation_apicale == "Negatif"):
            self.maladies.append("Pulpite_chronique")
            return "Pulpite_chronique"
        elif (self.test_sensibilite1 == "Negatif") and (self.test_sensibilite2 == "Douloureux" or self.test_sensibilite2 == "Non_Douloureux") and (self.test_sensibilite3 == "Non_Remanent") and (self.test_de_percution_axiale == "Negatif" or self.test_de_percution_axiale == "Positif") and (self.test_de_palpation_apicale == "Negatif" or self.test_de_palpation_apicale == "Positif" ):
            self.maladies.append("Necrose_pulpaire")
            return "Necrose_pulpaire"
        elif (self.test_sensibilite1 == "Negatif" ) and (self.test_sensibilite2 == "Douloureux") and (self.test_sensibilite3 == "Remanent") and (self.test_de_percution_axiale == "Positif") and (self.test_de_palpation_apicale == "Negatif"):
            self.maladies.append("Parodontite_apicale_aigue")
            return "Parodontite_apicale_aigue"
        elif (self.test_sensibilite1 == "Negatif" ) and (self.test_sensibilite2 == "Non_Douloureux") and (self.test_sensibilite3 == "Non_Remanent") and (self.test_de_percution_axiale == "Negatif") and (self.test_de_palpation_apicale == "Negatif"):
            self.maladies.append("Parodontite_apicale_chronique")
            return "Parodontite_apicale_chronique"
        elif (self.test_sensibilite1 == "Negatif" ) and (self.test_sensibilite2 == "Douloureux") and (self.test_sensibilite3 == "Remanent") and (self.test_de_percution_axiale == "Positif") and (self.test_de_palpation_apicale == "Positif"):
            self.maladies.append("Abces_apical_aigu")
            return "Abces_apical_aigu"
        elif (self.test_sensibilite1 == "Negatif" ) and (self.test_sensibilite2 == "Douloureux" or self.test_sensibilite2 == "Non_Douloureux") and (self.test_sensibilite3 == "Remanent") and (self.test_de_percution_axiale == "Positif") and (self.test_de_palpation_apicale == "Positif"):
            self.maladies.append("Abces_apical_secondaire")
            return "Abces_apical_secondaire"
        elif (self.test_sensibilite1 == "Negatif" ) and (self.test_sensibilite2 == "Non_Douloureux") and (self.test_sensibilite3 == "Remanent" or self.test_sensibilite3 == "Non_Remanent") and (self.test_de_percution_axiale == "Positif" or self.test_de_percution_axiale == "Negatif") and (self.test_de_palpation_apicale == "Positif" or self.test_de_palpation_apicale == "Negatif"):
            self.maladies.append("Parodontite_apicale_chronique_fistulisee")
            return "Parodontite_apicale_chronique_fistulisee"
        else:
            self.maladies.append("Expertise medicale requise")
            return "Analyses approfondies requises"


    def resultat(self):

        dic_res = dict()
        dic_res["Date consultation"] = str(self.dat_consul)
        dic_res["Test de sensibilite1"] = self.test_sensibilite1
        dic_res["Test de sensibilite2"] = self.test_sensibilite2
        dic_res["Test de sensibilite3"] = self.test_sensibilite3
        dic_res["Test de percution axiale"] = self.test_de_percution_axiale
        dic_res["Test de palpation apicale"] = self.test_de_palpation_apicale
        dic_res["Troubles"] = self.maladies

        return dic_res

