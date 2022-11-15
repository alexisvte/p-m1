"""Description :

Base de données : Aliments.csv.
Sujet Numéro 2 : Régime Alimentaire - Marie estime ses besoins journaliers de la manière suivante :
    - 75g de Protéines,
    - 90g de Lipides,
    - 225g de Glucides,
    - 2000 Kcal,
    - 9mg de Fer,
    - 800mg de Calcium,
    - 45g de Fibres.
Comment doit-elle satisfaire ses besoins si elle veut minimiser son budget ?
Comment doit-elle procéder si elle ne veut pas dépasser de plus de 10 % les apports journaliers ?
    
Test : data.py.
Procédure :
    - Tester automatiquement la librairie data.py.
"""

from project.data import Donnees, _data_aliments_show
import pytest


def test_donnees():
    essai = Donnees(
        prenom="Marie",
        contraintes=[75, 90, 225, 2000, 9, 800, 45],
    )
    isinstance(essai, Donnees)


def test_donnees_post():
    with pytest.raises(ValueError):
        Donnees(
            prenom="",
            contraintes=[75, 90, 225, 2000, 9, 800, 45],
        )
    with pytest.raises(ValueError):
        Donnees(
            prenom="Marieeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee",
            contraintes=[75, 90, 225, 2000, 9, 800, 45],
        )
    with pytest.raises(ValueError):
        Donnees(
            prenom="Marie",
            contraintes=[75, 90, 225, 2000, 9, 800],
        )
    with pytest.raises(ValueError):
        Donnees(
            prenom="Marie",
            contraintes=[75, 90, 225, 2000, 9, 800, 0],
        )


def test_donnees_repr():
    essai = Donnees(
        prenom="Marie",
        contraintes=[75, 90, 225, 2000, 9, 800, 45],
    )
    attendu = """
        Donnees de Marie :

        Protéines : 75 g,
        Lipides : 90 g,
        Glucides : 225 g,
        Kcal : 2000 Kcal,
        Fer : 9 mg,
        Calcium : 800 mg,
        Fibres : 45 g.
        """
    assert str(essai) == attendu


def test_aliments_show():
    essai = _data_aliments_show(ligne=20, colonnes=["Kcal", "Prix"], type="Viande")
    attendu = """                           Kcal  Prix
Produit (100g)                       
Viande – Boeuf haché        289  1.10
Viande – Jambon             178  4.64
Viande – Merguez            283  1.06
Viande – Gigot d'Agneau     200  1.99
Viande – Côtes d'Agneau     206  3.70
Viande – Saucisson          247  3.21
Viande – Saucisse           339  1.32
Viande – Blanc de Poulet    222  0.53
Viande – Cuisse de Poulet   232  1.13"""
    assert str(essai) == attendu
