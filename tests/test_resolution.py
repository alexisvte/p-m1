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
    
Test : resolution.py.
Procédure :
    - Tester automatiquement la librairie resolution.py.
"""

from project.data import Donnees
import project.resolution as pr
import pytest
import numpy as np


def test_resolution():
    donnees = Donnees(
        prenom="Marie",
        contraintes=[75, 90, 225, 2000, 9, 800, 45],
    )
    essai = pr._resolution(donnees=donnees)
    attendu = """
        Nous sommes parvenus à optimiser parfaitement le régime alimentaire de Marie.
        """
    assert str(essai) == attendu


def test_resultats():
    essai = pr.Resultats(
        prenom="Marie",
        couts=np.float64(5.4),
        valeurs=np.array(
            [
                0.0,
                0.7,
                0.0,
                0.0,
                0.0,
                0.5,
                0.0,
                0.0,
                0.5,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                5.4,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                3.7,
                0.8,
                0.0,
                1.3,
            ]
        ),
        succes=True,
    )
    donnees = Donnees(
        prenom="Marie",
        contraintes=[75, 90, 225, 2000, 9, 800, 45],
    )
    essaibis = pr._resolution(donnees)
    isinstance(essai, pr.Resultats)


def test_resultats_post():
    with pytest.raises(ValueError):
        pr.Resultats(
            prenom="",
            couts=np.float64(5.4),
            valeurs=np.array(
                [
                    0.0,
                    0.7,
                    0.0,
                    0.0,
                    0.0,
                    0.5,
                    0.0,
                    0.0,
                    0.5,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    5.4,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    3.7,
                    0.8,
                    0.0,
                    1.3,
                ]
            ),
            succes=True,
        )
    with pytest.raises(ValueError):
        pr.Resultats(
            prenom="Marie",
            couts=np.float64(0),
            valeurs=np.array(
                [
                    0.0,
                    0.7,
                    0.0,
                    0.0,
                    0.0,
                    0.5,
                    0.0,
                    0.0,
                    0.5,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    5.4,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    3.7,
                    0.8,
                    0.0,
                    1.3,
                ]
            ),
            succes=True,
        )
    with pytest.raises(ValueError):
        pr.Resultats(
            prenom="Marie",
            couts=np.float64(5.4),
            valeurs=np.array(
                [
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                ]
            ),
            succes=True,
        )
    with pytest.raises(ValueError):
        pr.Resultats(
            prenom="Marie",
            couts=np.float64(5.4),
            valeurs=np.array(
                [
                    0.0,
                    0.7,
                    0.0,
                    0.0,
                    0.0,
                    0.5,
                    0.0,
                    0.0,
                    0.5,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    5.4,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    3.7,
                    0.8,
                    0.0,
                    -1.3,
                ]
            ),
            succes=True,
        )


def test_resultats_repr():
    essai = pr.Resultats(
        prenom="Marie",
        couts=np.float64(5.4),
        valeurs=np.array(
            [
                0.0,
                0.7,
                0.0,
                0.0,
                0.0,
                0.5,
                0.0,
                0.0,
                0.5,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                5.4,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                3.7,
                0.8,
                0.0,
                1.3,
            ]
        ),
        succes=True,
    )
    attendu = """
        Nous sommes parvenus à optimiser parfaitement le régime alimentaire de Marie.
        """
    assert str(essai) == attendu
