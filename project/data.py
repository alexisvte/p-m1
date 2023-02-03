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
    
Librairie : data.py.
Procédure(s) :
    - Créer une classe pour structurer les données du sujet.
    - Créer une classe pour représenter les données du sujet.
    - Importer la base de données Aliments.csv.
    - Présenter la base de données Aliments.csv.
"""

from serde import serde
import pandas as pd


@serde
class Donnees:
    """Description :

    Structurer et représenter les données du sujet.

    prenom: caractères.
        Le prénom de la personne désirant optimiser son régime alimentaire.
    contraintes: liste d'entiers.
        Les contraintes et les besoins de la personne désirant optimiser son régime alimentaire.

    Nous regardons que le sujet est logique :

    Le prénom est un `str` :
        - Le prénom n'est pas trop long.

    Les contraintes sont des `int` dans une `list` :
        - Les contraintes sont strictement supérieurs à 0.
        - Les contraintes sont au nombre de 7.

    La sérialisation est faite automatiquement vers json, yaml et toml via pyserde.

    Exemple :

    >>> essai = Donnees(
    ...     prenom = "Marie",
    ...     contraintes = [
    ...             75,
    ...             90,
    ...             225,
    ...             2000,
    ...             9,
    ...             800,
    ...             45
    ...     ]
    ... )
    >>> essai

        Donnees de Marie :

        Protéines : 75 g,
        Lipides : 90 g,
        Glucides : 225 g,
        Kcal : 2000 Kcal,
        Fer : 9 g,
        Calcium : 800 mg,
        Fibres : 45 g.

    >>> from serde.json import to_json, from_json
    >>> code = to_json(essai)
    >>> code
    '{"prenom": "Marie", "contraintes": [75, 9, 225, 2000, 9, 800, 45]}'
    >>> decode = from_json(
    ...     Donnees,
    ...     code
    ... )
    >>> decode

        Donnees de Marie :

        Protéines : 75 g,
        Lipides : 90 g,
        Glucides : 225 g,
        Kcal : 2000 Kcal,
        Fer : 9 mg,
        Calcium : 800 mg,
        Fibres : 45 g.

    """

    prenom: str
    contraintes: list[int]

    def __post_init__(self):
        if len(self.prenom) <= 0 or len(self.prenom) > 62:
            raise ValueError(
                "Le prénom n'est pas renseigné ou le prénom est trop long."
            )
        if len(self.contraintes) != 7:
            raise ValueError(
                """
            Les contraintes ne sont pas renseignées. Elles sont au nombre de 7 :\n
            • les protéines (en g),
            • les lipides (en g),
            • les glucides (en g),
            • Les calories (en Kcal),
            • le fer (en mg),
            • le calcium (en mg)
            • les fibres (en g).
            """
            )
        for besoin in self.contraintes:
            if besoin <= 0:
                raise ValueError("Les contraintes sont stictement supérieurs à 0.")

    def __repr__(self) -> str:
        return f"""
        Donnees de {self.prenom} :\n
        Protéines : {self.contraintes[0]} g,
        Lipides : {self.contraintes[1]} g,
        Glucides : {self.contraintes[2]} g,
        Kcal : {self.contraintes[3]} Kcal,
        Fer : {self.contraintes[4]} mg,
        Calcium : {self.contraintes[5]} mg,
        Fibres : {self.contraintes[6]} g.
        """


data_aliments = pd.read_csv("Aliments.csv", sep=";", index_col=0)

data_aliments = data_aliments.rename(
    columns={
        "Protéines (en g)": "Protéines",
        "Lipides (en g)": "Lipides",
        "Glucides (en g)": "Glucides",
        "Energie (kcal)": "Kcal",
        "Fer (mg)": "Fer",
        "Calcium (mg)": "Calcium",
        "Fibres (en g)": "Fibres",
        "Prix €/100g": "Prix",
    }
)


def _data_aliments_show(
    ligne: int = 10, colonnes: list[str] = [], type: str = ""
) -> pd.core.frame.DataFrame:
    """Description :

    Représenter les données de la base de données `data_aliments` avec des options.

    ligne: entier (defaut = 10).
        Le nombre de ligne à représenter si et seulement si colonnes = défaut et / ou type = défaut.
    colonnes: liste de de caractères (défaut = []).
        Les besoins à représenter :
            Protéines,
            Lipides,
            Glucides,
            Kcal,
            Fer,
            Calcium,
            Fibres,
            Prix.
    type: caractères (défaut = "").
        Le type d'aliment à représenter :
            Lait,
            Viande,
            Poisson,
            Légume,
            Base.

    Exemple :

    >>> _data_aliments_show(
    ...     ligne = 20,
    ...     colonnes = [
    ...             "Kcal",
    ...             "Prix"
    ...     ],
    ...     type = "Viande"
    ... )
                               Kcal  Prix
    Produit (100g)
    Viande – Boeuf haché        289  1.10
    Viande – Jambon             178  4.64
    Viande – Merguez            283  1.06
    Viande – Gigot d'Agneau     200  1.99
    Viande – Côtes d'Agneau     206  3.70
    Viande – Saucisson          247  3.21
    Viande – Saucisse           339  1.32
    Viande – Blanc de Poulet    222  0.53
    Viande – Cuisse de Poulet   232  1.13
    """

    aliments = data_aliments.copy()

    if ligne > len(aliments):
        ligne = len(aliments)

    if colonnes == []:
        if type == "":
            tableau = aliments.head(ligne)
        else:
            ligne = None
            for aliment in aliments.index:
                if not aliment.startswith(type):
                    aliments.drop(labels=aliment, inplace=True)
                else:
                    None
            tableau = aliments
    else:
        ligne = None
        if type == "":
            tableau = aliments.loc[:, colonnes]
        else:
            for aliment in aliments.index:
                if not aliment.startswith(type):
                    aliments.drop(labels=aliment, inplace=True)
                else:
                    None
            tableau = aliments.loc[:, colonnes]
    return tableau
