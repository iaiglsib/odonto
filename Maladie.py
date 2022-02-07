class Maladie:
    def __init__(self, description, caracteristique ):
        self.id = id
        self.description = description
        self.caracteristique = {} 




class Pulpite_réversible(Maladie):
    def __init__(self, description, caracteristique):
        self.id = 1
        self.description = "Inflammation pulpaire qui devrait disparaître une fois sa cause prise en charge"
        self.caracteristique = {"Douleur provoquée remarquable, sensibilité pulpaire, Trait de fêlure dentaire"}
        





class Pulpite_aigue(Maladie):
    def __init__(self, description, caracteristique):
        self.id = 2
        self.description = "Inflammation de la pulpe dentaire contenue dans le canal dentaire"
        self.caracteristique = {"Douleur provoquée, Douleur spontanée ou rémanente remarquable, sensibilité pulpaire, Trait de fêlure dentaire "}
        



class Pulpite_aigue_et_parodontite_apicale_aigue_initiale(Maladie):
    def __init__(self, description, caracteristique):
        self.id = 3
        self.description = "Inflammation de la pulpe dentaire contenue dans le canal dentaire et Inflammation aiguë du péri-apex due à une irritation qui peut être d'origine chimique, physique ou infectueuse"
        self.caracteristique = {"Douleur provoquée, Douleur spontanée ou rémanente remarquable, sensibilité pulpaire, Douleur percussion remarquable, Tait de fêlure dentaire, Image radioclaire pert-apicale"}
        



class Pulpite_chronique(Maladie) :
    def __init__(self, description, caracteristique ):
        self.id = 4
        self.description = "Inflammation de la pulpe dentaire résultant de l'évolution des caries non traitées, de traumatismes ou de restaurations iatrogènes"
        self.caracteristique = {"Douleur provoquée, sensibilité pulpaire, Trait de fêlure dentaire, Image radiodense pert-apicale"}
        


class Necrose_pulpaire(Maladie):
    def __init__(self, descrption, caracteristique):
        self.id = 5
        self.description = "Stade ultérieur de la pulpite irréversible; la pulpe ne répond pas au chaud ou au froid, mais elle répond souvent à la percussion, et un traitement canalaire ou une extraction sont nécessaires."
        self.caracteristique = {"Douleur provoquée, Douleur percussion, Douleur palpation apicale, Oedème des tissus mous, Ostium fisculaire, Trait de fêlure dentaire, Image radioclaire pert-apicale, Image radiodense pert-apicale"}
        


class Parodontite_apicale_aigue(Maladie):
    def __init__(self, descrption, caracteristique):
        self.id = 6
        self.description = "Inflammation aiguë du péri-apex due à une irritation qui peut être d'origine chimique, physique ou infectueuse"
        self.caracteristique = {"Douleur provoquée remarquable, Douleur spontanée ou rémanente remarquable, Douleur percussion remarquable, Trait de fêlure dentaire, Image radioclaire pert-apicale"}
        



class Parodontite_apicale_chronique(Maladie):
    def __init__(self, descrption, caracteristique):
        self.id = 7
        self.description = "Lésoins inflammatoires du parodonte profond péri-radiculaire, principalement de la région périapicale, consécutive à l infection bactérienne de l endodonte"
        self.caracteristique = {"Trait de fêlure dentaire, Image radioclaire pert-apicale remarquable, Image radiodense pert-apicale "}
        


class Abces_apical_aigu(Maladie):
    def __init__(self, descrption, caracteristique):
        self.id = 8
        self.description = "C'est une symptomatologie aiguë accompagnée de douleurs constantes avec ou sans gonflement des tissus périradiculaires ou faciaux"
        self.caracteristique = {"Douleur provoquée, Douleur spontanée ou rémanente remarquable, Douleur percussion remarquable, Douleur palpation apicale, Oedème des tissus mous, Trait de fêlure dentaire, Image radioclaire pert-apicale"}


class Abces_apical_secondaire(Maladie):
    def __init__(self, descrption, caracteristique):
        self.id = 9
        self.description = "abcès qui survient au bout de la racine de la dent. On parle d origine endodontique. Ce type de pathologie peut prendre différentes formes"
        self.caracteristique = {"Douleur provoquée, Douleur spontanée ou rémanente remarquable, Douleur percussion remarquable, Douleur palpation apicale, Oedème des tissus mous, Trait de fêlure dentaire, Image radioclaire pert-apicale remarquable"}
        


class Parodontite_apicale_chronique_fistulisee(Maladie):
    def __init__(self, descrption, caracteristique):
        self.id = 10
        self.description = "Parodontite apicale chronique avec fistule"
        self.caracteristique = {"Douleur spontanée ou rémanente, Douleur percussion, Douleur palpation apicale, Oedème des tissus mous, Ostium fisculaire remarquable, Trait de fêlure dentaire, Image radioclaire pert-apicale"}
        


class Cellulite (Maladie):
    def __init__(self, descrption, caracteristique):
        self.id = 11
        self.description = "Diffusion d une infection dentaire vers les tissus cellulo-adipeux, principalement, les tissus mous-cutanés"
        self.caracteristique = {"Douleur provoquée, Douleur spontanée ou rémanente, Douleur percussion, Douleur palpation apicale remarquable, Oedème des tissus mous remarquable, Ostium fisculaire, Trait de fêlure dentaire, Image radioclaire pert-apicale"} 


















