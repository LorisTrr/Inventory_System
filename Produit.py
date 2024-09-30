# produit.py
class Produit:
    def __init__(self, nom, quantite, prix, seuil_alerte):
        self.nom = nom
        self.quantite = quantite
        self.prix = prix
        self.seuil_alerte = seuil_alerte

    def __str__(self):
        return f"{self.nom} - Quantité : {self.quantite}, Prix : {self.prix}, Seuil d'alerte : {self.seuil_alerte}"
