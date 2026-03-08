class Voiture:

    def __init__(self, matricule, marque, couleur):
        self.matricule = matricule
        self.marque = marque
        self.couleur = couleur

    def afficherInformations(self):
            print("Matricule :", self.matricule)
            print("Marque :", self.marque)
            print("Couleur :", self.couleur)


class Parc:

    def __init__(self, id, adresse, capacite):
        self.id = id
        self.adresse = adresse
        self.capacite = capacite
        self.listeVoitures = []

    def entrervoiture(self, voiture):
        if voiture in self.listevoitures:
            print(" La voiture est déja dans le parc ")

        elif self.capacite <= 0:
            print(" La capacite maximale du parc est atteinte ")
        else:
            self.listevoitures.append(voiture)
            self.capacite = self.capacite - 1
            print(" Voiture bien ajouté au parc ")

    def sortirvoiture(self, voiture):
        if voiture not in self.listevoitures:
            print(" Voiture n'est pas présente dans le parc ")

    else:
        self.listevoitures.remove(voiture)
        self.capacite = self.capacite + 1

        print(" La voiture est sortie du parc ")
        print(" La nouvelle capacité est : ", self.capacite)

    def NbrPlacesLibres(self):
        return self.capacite

p1=Parc(1,"Toronto", 3)
v1=Voiture("AO10", "Mercedes", "Noir")
v2=Voiture("AO11", "JEEP","Noir")
v3=Voiture("AO12","TOYOTA","Noir")
v4=Voiture("AO13","AUDI","Bleu")
p1.entrervoiture(v1)
v1.afficherinformations()

p1.entrervoiture(v2)
v2.afficherinformations()

p1.entrervoiture(v3)
v3.afficherinformations()

p1.entrervoiture(v4)
p1.sortirvoiture(v1)
p1.sortirvoiture(v2)
p1.sortirvoiture(v4)
p1.NbrPlacesLibres()