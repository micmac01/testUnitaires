class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur


class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, livre):
        self.livres.remove(livre)

    def lister_livres(self):
        return self.livres
    
    def rechercher_par_auteur(self, auteur):
        return [livre for livre in self.livres if livre.auteur == auteur]
    
    def generation_stat(self):
        return {
            "total_livres": len(self.livres),
            "auteurs_uniques": set(livre.auteur for livre in self.livres)
        }
