import json


from serialisation import serialiseur_patient
from Consultation import consultation

liste_patient = []

p1 = consultation()
p1.Analyse()

liste_patient.append(p1)


with open('fichier_patients.json', 'a', encoding='utf-8') as f:
    json.dump(liste_patient, f, indent=4, default=serialiseur_patient)


