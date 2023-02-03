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
    
Librairie : resolution.py.

La résolution est réussit si et seulement si l'optimisation est réussit.

Procédure(s) :
    - Résoudre le problème du sujet avec les données du sujet et les données de Aliments.csv.
    - Conclure la résolution du problème.
"""

from .data import Donnees
import project.transformation as pt
from serde import serde
import numpy as np
import scipy.optimize as so

np.set_printoptions(precision=1, suppress=True)


@serde
class Resultats:
    """Description :

    Structurer et représenter les résultats du sujet.

    prenom: caractères.
        Le prénom de la personne désirant optimiser son régime alimentaire.
    couts: flottant numpy 64.
        Le coût total de tous les aliments du résultat de l'optimisation du régime alimentaire.
    valeurs: matrice numpy.
        Le nombre de paniers de 100 grammes de chaque aliment du résultat de l'optimisation alimentaire.
    succes: logique.
        Le succès du résultat de l'optimisation du régime alimentaire.

    Nous regardons que le sujet est logique :

    Le prénom est un `str` :
        - Le prénom n'est pas trop long.

    Les couts sont un `np.float64` :
        - Les coûts ne sont pas nuls et sont srictements supérieurs à 0.

    Les valeurs sont un `np.array` :
        - Les valeurs ne sont pas toutes nuls.
        - Les valeurs sont strictement supérieurs à 0.

    Le succès est un `bool` :
        - Nous devons parvenir à optimiser le régime alimentaire.

    Exemple :

    >>> donnees = Donnees(
    ...     prenom = "Marie",
    ...     contraintes = [
    ...         75,
    ...         90,
    ...         225,
    ...         2000,
    ...         9,
    ...         800,
    ...         45
    ...     ]
    ... )
    >>> _resolution(donnees)

        Nous sommes parvenus à optimiser le régime alimentaire de Marie.

    >>> resultats = _resolution(donnees)
    >>> resultats.prenom
    'Marie'
    >>> resultats.couts
    5.4
    >>> resultats.valeurs
    array([0. , 0.7, 0. , 0. , 0. , 0.5, 0. , 0. , 0.5, 0. , 0. , 0. , 0. ,
           0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 5.4,
           0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 0. , 3.7, 0.8,
           0. , 1.3])
    >>> resultats.succes
    True
    """

    prenom: str
    couts: np.float64
    valeurs: np.ndarray
    succes: bool

    def __post_init__(self):
        if len(self.prenom) <= 0 or len(self.prenom) > 62:
            raise ValueError(
                "Le prénom n'est pas renseigné ou le prénom est trop long."
            )
        if self.couts <= 0:
            raise ValueError("Les coûts ne peuvent pas être nuls.")
        if sum(self.valeurs) == 0:
            raise ValueError(
                "Le nombre de paniers de chaque aliment ne peut pas être nul."
            )
        for aliment in self.valeurs:
            if aliment < 0:
                raise ValueError(
                    "Le nombre de paniers de chaque aliment ne peut pas être nul."
                )
        # if not self.success:
        #    raise ValueError("Nous ne sommes pas parvenus à optimiser parfaitement le régime alimentaire.")

    def __repr__(self) -> str:
        if self.succes:
            interne = "sommes parvenus"
        else:
            interne = "ne sommes pas parvenus"
        return f"""
        Nous {interne} à optimiser parfaitement le régime alimentaire de {self.prenom}.
        """


def _resolution(donnees: Donnees):
    """Description :

    Optimiser le régime alimentaire.

    donnees: Donnees.
        Les données de la personne désirant optimiser son régime alimentaire :
            Prénom,
            Contraintes (protéines, lipides, glucides, kcal, fer, calcium, fibres).

    Exemple :

    >>> donnees = Donnees(
    ...     prenom = "Marie",
    ...     contraintes = [
    ...         75,
    ...         90,
    ...         225,
    ...         2000,
    ...         9,
    ...         800,
    ...         45
    ...     ]
    ... )
    >>> _resolution(donnees)

        Nous sommes parvenus à optimiser parfaitement le régime alimentaire de Marie.

    """

    transformees = pt._transformation(donnees=donnees)
    resultat = so.linprog(
        transformees[1],  # prix.
        A_ub=np.concatenate(
            (-transformees[0], transformees[0]), axis=0
        ),  # coefficients.
        b_ub=np.concatenate(
            (-transformees[2], transformees[2] * 1.1), axis=0
        ),  # contraintes.
        method="simplex",
    )
    # if not resultat.success:
    #    raise ValueError("Nous ne sommes pas parvenus à optimiser parfaitement le régime alimentaire.")
    resultats = Resultats(
        prenom=donnees.prenom,
        couts=np.round(resultat.fun, decimals=1),
        valeurs=resultat.x,
        succes=resultat.success,
    )
    return resultats
