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
    
Librairie : transformation.py.
Procédure(s) :
    - Transformer les données de Aliments.csv.
    - Transformer les résultats de resolution.py.
"""

from .data import Donnees, data_aliments
import project.resolution as pr
import pandas as pd
import numpy as np
import importlib

np.set_printoptions(precision=1, suppress=True)


def _transformation(donnees: Donnees):  # -> list[np.ndarray[float]]
    """Description :

    Transformer les données pour les optimiser.

    donnees: Donnees.
        Les données de la personne désirant optimiser son régime alimentaire :
            Prénom,
            Contraintes (protéines, lipides, glucides, kcal, fer, calcium, fibres).

    Exemple :

    >>> _transformation(donnees)
    [array([[  26.9,   20.9,    9.4,    3.1,    3.6,   29.8,   19.8,   18.5,
                0.8,    5.2,   24.1,   22.6,   22.6,   29.8,   29. ,   15.3,
               19.4,   29. ,   26. ,   24.6,   23.9,    2.4,    0.8,    0.9,
                1.8,    0.7,    3.3,    1.1,    1.6,    3. ,    3.3,    5.3,
                2.3,    2.3,    3.8,    5.8,    2.4,    5.3,    5.5,    9. ,
               12.7],
           [  27.8,   35. ,    9.4,    3.2,    4.1,   32.3,   24.3,   21.1,
              81.1,    1.6,   20.7,    9. ,   19.8,    9. ,    9.9,   19.9,
              28.4,   10.8,   13.5,   11.4,   17.8,    0.4,    0.2,    0.2,
               0.5,    0.3,    0.2,    0.4,    0.3,    0.3,    1.4,    0.5,
               0.8,    1.2,   17.1,    0.9,    0.2,    0.4,    5.2,    0.4,
               1.1],
           [   5.4,    2.8,    3.3,    4.8,    4.5,    0.4,    0.5,    0.9,
               0.1,    7. ,    0. ,    0. ,    0.2,    0. ,    0. ,    0.7,
               0. ,    0. ,    0. ,    0. ,    0. ,    7.2,    8.2,    9.6,
               4.1,   14.3,    7. ,    2.7,    9. ,    3.8,   18.7,   26.5,
              23.5,   16.1,   37.5,   30.9,   28.6,   15.5,   21.6,   20.1,
              72.8],
           [ 380. ,  328. ,  136. ,   61. ,   69. ,  413. ,  300. ,  268. ,
             717. ,   63. ,  289. ,  178. ,  283. ,  200. ,  206. ,  247. ,
             339. ,  222. ,  232. ,  208. ,  262. ,   35. ,   35. ,   41. ,
              23. ,   56. ,   42. ,   15. ,   38. ,   23. ,   86. ,  124. ,
             112. ,   83. ,  319. ,  158. ,  130. ,   85. ,  155. ,  116. ,
             360. ],
           [   0.2,    0. ,    0.2,    0.3,    0.1,    0.2,    0.3,    1.9,
               0. ,    0.1,    2.4,    1.3,    2. ,   27.6,    1.7,    0.8,
               1.4,    1.1,    1.3,    2.9,    1.6,    0.7,    0.3,    0.3,
               0.3,    0.4,    2. ,    0.4,    0.5,    3.6,    0.5,    1.1,
               0.5,    0.5,    1.4,    1.3,    0.2,    1.3,    2. ,    3.3,
               1.2],
           [ 791. ,   66.3,  112. ,  113. ,  134. , 1011. ,  388. ,  140. ,
              24. ,  183. ,   11. ,    8. ,   35.9,    1.7,   15. ,   11. ,
              13. ,   15. ,   12. ,  382. ,   15. ,   40. ,   30. ,   33. ,
              16. ,    9. ,   42. ,   18. ,   18. ,  136. ,    2. ,   15. ,
              10. ,   21. ,   13. ,    7. ,    3. ,   25. ,   61. ,   19. ,
              17. ],
           [   0. ,    0. ,    0. ,    0. ,    0. ,    0. ,    0. ,    0. ,
               0. ,    0. ,    0. ,    0. ,    0. ,    0. ,    0. ,    0. ,
               0. ,    0. ,    0. ,    0. ,    0. ,    2.4,    2.7,    2.4,
               2.3,    2.9,    2.8,    1. ,    1.9,    2.4,    2. ,    3.2,
               1.9,    1.2,    3.5,    1.8,    0.5,    5.4,    5.5,    4.2,
               3.9]]),
            array([
                1.3, 0.8, 0.4, 0.3, 0.7, 1.2, 1.1,
                3. , 1.2, 1. , 1.1, 4.6, 1.1, 2. ,
                3.7, 3.2, 1.3, 0.5, 1.1, 3. , 0.7,
                0.3, 0.5, 0.4, 0.4, 0.3, 0.5, 0.4,
                0.6, 0.6, 0.4, 0.2, 0.3, 0.2, 0.3,
                0.2, 0.3, 0.4, 0.1, 0.2, 0.2]),
            array([75, 90, 225, 2000, 9, 800, 45])]
    """

    aliments_array = np.array(data_aliments).T
    transformation = []

    coefficients_array = aliments_array[:-1]  # on enlève le prix.
    transformation.append(coefficients_array)

    prix_array = aliments_array[-1]  # on prend le prix.
    transformation.append(prix_array)

    contraintes_array = np.array(donnees.contraintes)  # les contraintes.
    transformation.append(contraintes_array)
    return transformation


def _contraintes_bornes(donnees: Donnees) -> tuple[tuple]:
    """Description :

    Transformer les contraintes en bornes allant de 1 fois la contrainte à 1.1 fois la contrainte.

    donnees: Donnees.
        Les données de la personne désirant optimiser son régime alimentaire :
            Prénom,
            Contraintes (protéines, lipides, glucides, kcal, fer, calcium, fibres).

    Exemple :

    >>> donnees = pd.Donnees(
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
    >>> _contraintes_bornes(donnees)
    [(75, 82.5), (90, 99.00000000000001), (225, 247.50000000000003), (2000, 2200.0), (9, 9.9), (800, 880.0000000000001), (45, 49.50000000000001)]
    """

    bornes = []
    for contrainte in donnees.contraintes:
        bornes.append((contrainte * 1, contrainte * 1.1))
    return bornes


importlib.reload(pr)


def _extraction_resolution(resultats: pr.Resultats) -> pd.core.frame.DataFrame:
    """ "Description :

    Extraire les résultats.

    resultats: Resultats.
        Les résultats de la personne désirant optimiser son régime alimentaire :
            Prénom,
            Couts,
            Valeurs (41 aliments),
            Succès.

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
    >>> resultats = _resolution(donnees)
    >>> extraction = _resolution_transformation(resultats)
    >>> extraction
                            Protéines  Lipides  Glucides    Kcal  Fer  Calcium  Fibres  Prix

    Lait – crème fraîche         15.3     25.7       2.1   240.4  0.0     48.6     0.0   0.6
    Lait – Gruyère               15.6     16.9       0.2   216.3  0.1    529.6     0.0   0.6
    Lait – Beurre                 0.4     38.9       0.0   344.2  0.0     11.5     0.0   0.6
    Légume – Courg                3.6      1.8      77.4   302.3  1.9     48.6    15.7   1.7
    Base – Haricots rouges        9.6      1.3      57.9   316.9  4.7     93.2    20.1   1.6
    Base – Haricots blancs        4.2      3.9      16.6   118.8  1.5     46.8     4.2   0.1
    Base – Semoule               16.2      1.3      93.3   461.0  1.6     21.8     5.0   0.2"""

    (a,) = resultats.valeurs.nonzero()  # Indices des aliments optimaux.
    aliments_opt = data_aliments.iloc[a, :]  # Tableau des aliments optimaux.

    paniers_opt = pd.DataFrame(
        {
            "Paniers de 100 g": resultats.valeurs[
                resultats.valeurs.nonzero()
            ]  # Colonne de la valeur des aliments optimaux.
        }
    ).set_index(
        data_aliments.iloc[a, :].index
    )  # Indices des aliments correspondants aux valeurs des aliments optimaux.

    paniers_opt.index.name = ""  # Remplacé par Paniers de 100 g.

    variables_opt = pd.DataFrame(
        (
            np.array(aliments_opt).T * resultats.valeurs[resultats.valeurs.nonzero()]
        ).T  # Colonnes des variables.
    ).set_index(paniers_opt.index)

    resultat = [paniers_opt, variables_opt]

    return resultat


def _resolution_transformation(resultats: pr.Resultats) -> pd.core.frame.DataFrame:
    """Description :

    Transformer les résultats pour les représenter.

    resultats: Resultats.
        Les résultats de la personne désirant optimiser son régime alimentaire :
            Prénom,
            Couts,
            Valeurs (41 aliments),
            Succès.

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
    >>> resultats = _resolution(donnees)
    >>> tableau = _resolution_transformation(resultats)
    >>> tableau
                            Paniers de 100 g  Protéines  Lipides  Glucides    Kcal  Fer  Calcium  Fibres  Prix

    Lait – crème fraîche                 0.7       15.3     25.7       2.1   240.4  0.0     48.6     0.0   0.6
    Lait – Gruyère                       0.5       15.6     16.9       0.2   216.3  0.1    529.6     0.0   0.6
    Lait – Beurre                        0.5        0.4     38.9       0.0   344.2  0.0     11.5     0.0   0.6
    Légume – Courge                      5.4        3.6      1.8      77.4   302.3  1.9     48.6    15.7   1.7
    Base – Haricots rouges               3.7       19.6      1.3      57.9   316.9  4.7     93.2    20.1   1.6
    Base – Haricots blancs               0.8        4.2      3.9      16.6   118.8  1.5     46.8     4.2   0.1
    Base – Semoule                       1.3       16.2      1.3      93.3   461.0  1.6     21.8     5.0   0.2
    Total                               12.9       75.0     90.0     247.5  2000.0  9.9    800.0    45.0   5.4
    """

    extraction = _extraction_resolution(resultats)

    regime = pd.concat([extraction[0], extraction[1]], axis=1)  # Tableau.
    regime.loc["Total"] = regime.sum(numeric_only=True, axis=0)  # Total.

    noms_col = [extraction[0].columns[0]] + list(data_aliments.columns)  # Variables.
    regime.columns = noms_col

    resultat = regime.round(decimals=1)

    return resultat


def _transformation_final(tableau: pd.core.frame.DataFrame) -> str:
    """Description :

    Transformer les résultats pour informer la personne désirant optimiser son régime alimentaire.

    tableau: pd.core.frame.DataFrame.
        Le tableau des résultats de la personne désirant optimiser son régime alimentaire.

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
    >>> resultats = _resolution(donnees)
    >>> tableau = _resolution_transformation(resultats)
    >>> _transformation_final(tableau)
    Vous devez manger 70 grammes de crème fraîche ce qui vous coûtera 0.6 euros.
    Vous devez manger 50 grammes de Gruyère ce qui vous coûtera 0.6 euros.
    Vous devez manger 50 grammes de Beurre ce qui vous coûtera 0.6 euros.
    Vous devez manger 540 grammes de Courge ce qui vous coûtera 1.7 euros.
    Vous devez manger 370 grammes de Haricots rouges ce qui vous coûtera 1.6 euros.
    Vous devez manger 80 grammes de Haricots blancs ce qui vous coûtera 0.1 euros.
    Vous devez manger 130 grammes de Semoule ce qui vous coûtera 0.2 euros.
    Le repas vous coûtera 5.4 euros.
    """

    final = tableau.copy()
    final = final.drop(labels="Total", inplace=False)

    produits = []
    for i in final.index:
        produit = i.split(" – ")
        produits.append(produit[1])

    final.index = produits

    phrases = final.apply(
        lambda row: "Vous devez manger "
        + str(int(row["Paniers de 100 g"] * 100))
        + " grammes de "
        + str(row.name)
        + " ce qui vous coûtera "
        + str(row["Prix"])
        + " euros",
        axis=1,
    )
    for i in phrases:
        print(f"{i}.")
    print(
        f"""Le repas vous coûtera {tableau.loc[
        "Total",
        "Prix"
    ]} euros."""
    )


# def _contraintes_logiques() -> bool:
#    pass

## Prospection :

# Regarder si les contraintes sont logiques.
# Renseigner quelles sont les contraintes qui sont logiques.
# Transformer `_data_resolution` en tableau. (en cours) √
# Scinder `_data_resolution_transformation` en classe ou en plusieurs fonctions. (en cours) √
# Transformer `_data_resolution_transforamtion` en phrase.
# À regarder...
