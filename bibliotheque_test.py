import bibliotheque as bib


def test_ajout_livre():
    bibliotheque = bib.Bibliotheque()
    livre = bib.Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    bibliotheque.ajouter_livre(livre)
    livre = bib.Livre("1984", "George Orwell")
    bibliotheque.ajouter_livre(livre)
    assert len(bibliotheque.livres) == 2
    assert bibliotheque.livres[0].titre == "Le Petit Prince"
    assert bibliotheque.livres[0].auteur == "Antoine de Saint-Exupéry"
    assert bibliotheque.livres[1].titre == "1984"
    assert bibliotheque.livres[1].auteur == "George Orwell"


def test_suppression_livre():
    bibliotheque = bib.Bibliotheque()
    livre1 = bib.Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    livre2 = bib.Livre("1984", "George Orwell")
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)
    bibliotheque.supprimer_livre(livre1)
    assert len(bibliotheque.livres) == 1
    assert bibliotheque.livres[0].titre == "1984"
    assert bibliotheque.livres[0].auteur == "George Orwell"


def test_recherche_par_auteur():
    bibliotheque = bib.Bibliotheque()
    livre1 = bib.Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    livre2 = bib.Livre("1984", "George Orwell")
    livre3 = bib.Livre("Animal Farm", "George Orwell")
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)
    bibliotheque.ajouter_livre(livre3)
    result = bibliotheque.rechercher_par_auteur("George Orwell")
    assert len(result) == 2
    assert result[0].titre == "1984"
    assert result[1].titre == "Animal Farm"
    assert result[0].auteur == "George Orwell"
    assert result[1].auteur == "George Orwell"


def test_statistiques_bibliotheque():
    bibliotheque = bib.Bibliotheque()
    livre1 = bib.Livre("Le Petit Prince", "Antoine de Saint-Exupéry")
    livre2 = bib.Livre("1984", "George Orwell")
    livre3 = bib.Livre("Animal Farm", "George Orwell")
    bibliotheque.ajouter_livre(livre1)
    bibliotheque.ajouter_livre(livre2)
    bibliotheque.ajouter_livre(livre3)
    stats = bibliotheque.generation_stat()
    assert stats["total_livres"] == 3
    assert stats["auteurs_uniques"] == {"Antoine de Saint-Exupéry", "George Orwell"}