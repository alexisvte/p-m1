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
    
Test : transformation.py.
Procédure :
    - Tester automatiquement la librairie transformation.py.
"""

from project.data import Donnees
import project.transformation as pt
import project.resolution as pr
import pytest
import numpy as np
import importlib

np.set_printoptions(precision=1, suppress=True)


def test_transformation():
    essai = Donnees(
        prenom="Marie",
        contraintes=[75, 90, 225, 2000, 9, 800, 45],
    )
    attendu = [
        np.array(
            [
                [
                    26.9,
                    20.9,
                    9.4,
                    3.1,
                    3.6,
                    29.8,
                    19.8,
                    18.5,
                    0.8,
                    5.2,
                    24.1,
                    22.6,
                    22.6,
                    29.8,
                    29.0,
                    15.3,
                    19.4,
                    29.0,
                    26.0,
                    24.6,
                    23.9,
                    2.4,
                    0.8,
                    0.9,
                    1.8,
                    0.7,
                    3.3,
                    1.1,
                    1.6,
                    3.0,
                    3.3,
                    5.3,
                    2.3,
                    2.3,
                    3.8,
                    5.8,
                    2.4,
                    5.3,
                    5.5,
                    9.0,
                    12.7,
                ],  # Protéines.
                [
                    27.8,
                    35.0,
                    9.4,
                    3.2,
                    4.1,
                    32.3,
                    24.3,
                    21.1,
                    81.1,
                    1.6,
                    20.7,
                    9.0,
                    19.8,
                    9.0,
                    9.9,
                    19.9,
                    28.4,
                    10.8,
                    13.5,
                    11.4,
                    17.8,
                    0.4,
                    0.2,
                    0.2,
                    0.5,
                    0.3,
                    0.2,
                    0.4,
                    0.3,
                    0.3,
                    1.4,
                    0.5,
                    0.8,
                    1.2,
                    17.1,
                    0.9,
                    0.2,
                    0.4,
                    5.2,
                    0.4,
                    1.1,
                ],  # Lipides.
                [
                    5.4,
                    2.8,
                    3.3,
                    4.8,
                    4.5,
                    0.4,
                    0.5,
                    0.9,
                    0.1,
                    7.0,
                    0.0,
                    0.0,
                    0.2,
                    0.0,
                    0.0,
                    0.7,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    0.0,
                    7.2,
                    8.2,
                    9.6,
                    4.1,
                    14.3,
                    7.0,
                    2.7,
                    9.0,
                    3.8,
                    18.7,
                    26.5,
                    23.5,
                    16.1,
                    37.5,
                    30.9,
                    28.6,
                    15.5,
                    21.6,
                    20.1,
                    72.8,
                ],  # Glucides.
                [
                    380.0,
                    328.0,
                    136.0,
                    61.0,
                    69.0,
                    413.0,
                    300.0,
                    268.0,
                    717.0,
                    63.0,
                    289.0,
                    178.0,
                    283.0,
                    200.0,
                    206.0,
                    247.0,
                    339.0,
                    222.0,
                    232.0,
                    208.0,
                    262.0,
                    35.0,
                    35.0,
                    41.0,
                    23.0,
                    56.0,
                    42.0,
                    15.0,
                    38.0,
                    23.0,
                    86.0,
                    124.0,
                    112.0,
                    83.0,
                    319.0,
                    158.0,
                    130.0,
                    85.0,
                    155.0,
                    116.0,
                    360.0,
                ],  # Kcal.
                [
                    0.2,
                    0.0,
                    0.2,
                    0.3,
                    0.1,
                    0.2,
                    0.3,
                    1.9,
                    0.0,
                    0.1,
                    2.4,
                    1.3,
                    2.0,
                    27.6,
                    1.7,
                    0.8,
                    1.4,
                    1.1,
                    1.3,
                    2.9,
                    1.6,
                    0.7,
                    0.3,
                    0.3,
                    0.3,
                    0.4,
                    2.0,
                    0.4,
                    0.5,
                    3.6,
                    0.5,
                    1.1,
                    0.5,
                    0.5,
                    1.4,
                    1.3,
                    0.2,
                    1.3,
                    2.0,
                    3.3,
                    1.2,
                ],  # Fer.
                [
                    791.0,
                    66.3,
                    112.0,
                    113.0,
                    134.0,
                    1011.0,
                    388.0,
                    140.0,
                    24.0,
                    183.0,
                    11.0,
                    8.0,
                    35.9,
                    1.7,
                    15.0,
                    11.0,
                    13.0,
                    15.0,
                    12.0,
                    382.0,
                    15.0,
                    40.0,
                    30.0,
                    33.0,
                    16.0,
                    9.0,
                    42.0,
                    18.0,
                    18.0,
                    136.0,
                    2.0,
                    15.0,
                    10.0,
                    21.0,
                    13.0,
                    7.0,
                    3.0,
                    25.0,
                    61.0,
                    19.0,
                    17.0,
                ],  # Calcium.
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
                    2.4,
                    2.7,
                    2.4,
                    2.3,
                    2.9,
                    2.8,
                    1.0,
                    1.9,
                    2.4,
                    2.0,
                    3.2,
                    1.9,
                    1.2,
                    3.5,
                    1.8,
                    0.5,
                    5.4,
                    5.5,
                    4.2,
                    3.9,
                ],  # Fibres.
            ]
        ),  # coefficients.
        np.array(
            [
                1.3,
                0.8,
                0.4,
                0.3,
                0.7,
                1.2,
                1.1,
                3.0,
                1.2,
                1.0,
                1.1,
                4.6,
                1.1,
                2.0,
                3.7,
                3.2,
                1.3,
                0.5,
                1.1,
                3.0,
                0.7,
                0.3,
                0.5,
                0.4,
                0.4,
                0.3,
                0.5,
                0.4,
                0.6,
                0.6,
                0.4,
                0.2,
                0.3,
                0.2,
                0.3,
                0.2,
                0.3,
                0.4,
                0.1,
                0.2,
                0.2,
            ]
        ),  # prix
        np.array([75, 90, 225, 2000, 9, 800, 45]),  # contraintes.
    ]
    for array1, array2 in zip(pt._transformation(essai), attendu):
        if (array1 == array2).all:
            return True
        else:
            return False


def test_contraintes_bornes():
    donnees = Donnees(
        prenom="Marie",
        contraintes=[75, 90, 225, 2000, 9, 800, 45],
    )
    essai = pt._contraintes_bornes(donnees=donnees)
    attendu = "[(75, 82.5), (90, 99.00000000000001), (225, 247.50000000000003), (2000, 2200.0), (9, 9.9), (800, 880.0000000000001), (45, 49.50000000000001)]"
    assert str(essai) == attendu


importlib.reload(pr)


def test_extraction_resolution():
    donnees = Donnees(prenom="Marie", contraintes=[75, 90, 225, 2000, 9, 800, 45])
    resultats = pr._resolution(donnees)
    essai = pt._extraction_resolution(resultats)
    assert type(essai[0]) == type(essai[1])


# @pytest.mark.skip(reason = "Nous cherchons un moyen de tester `_resolution_transformation` (interne).")
def test_resolution_transformation():
    donnees = Donnees(prenom="Marie", contraintes=[75, 90, 225, 2000, 9, 800, 45])
    resultats = pr._resolution(donnees)
    essai = pt._resolution_transformation(resultats)
    attendu = 12.9
    assert essai.loc["Total", "Paniers de 100 g"] == attendu


# @pytest.mark.skip(reason = "Nous cherchons un moyen de tester `_resolution_transformation` (interne).")
def test_transformation_final():
    donnees = Donnees(prenom="Marie", contraintes=[75, 90, 225, 2000, 9, 800, 45])
    resultats = pr._resolution(donnees)
    tableau = pt._resolution_transformation(resultats)
    attendu = None
    assert pt._transformation_final(tableau) == attendu
