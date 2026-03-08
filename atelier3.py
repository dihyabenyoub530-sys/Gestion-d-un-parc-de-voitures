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
