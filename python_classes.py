class Personne:
    """Classe definissant une personne caracterisee par
        - nom
        - prenom
        - age
        - lieu de residence"""
    def __init__(self, nom, prenom): # constructeur
        """Constructeur de notre classe. Deux valeurs en parametre ainsi
            que deux attributs avec valeurs par defauts"""
        
        self.nom = nom
        self.prenom = prenom
        self.age = 33
        self.lieu_residence = "Paris"


jean = Personne("Jean", "De LaVille")

print("prenom:", jean.prenom)
print("nom:", jean.nom)
print("age:", jean.nom)
print("lieu de residence", jean.lieu_residence)
