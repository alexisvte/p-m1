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
"""

import project.data
import project.transformation
import project.resolution
import typer


def debut_externe(prenom: str):

    typer.echo(
        f"""
    Bonjour {prenom} !
    """
    )

    typer.echo(
        f"""
    Pour répondre aux questions suivantes, veuillez ne rentrer que des valeurs entières.

    Exemple :

    Quels sont vos besoins en protéines (en g) ?: 75
    """
    )
    variables = [
        "protéines (en g)",
        "lipides (en g)",
        "glucides (en g)",
        "calories (en kcal)",
        "fer (en mg)",
        "calcium (en mg)",
        "fibres (en g)",
    ]
    contrainte = []
    for variable in variables:
        besoin = int(typer.prompt(f"Quels sont vos besoins en {variable} ?"))
        contrainte.append(besoin)
    donnees = project.data.Donnees(
        prenom=prenom,
        contraintes=[
            contrainte[0],
            contrainte[1],
            contrainte[2],
            contrainte[3],
            contrainte[4],
            contrainte[5],
            contrainte[6],
        ],
    )

    typer.echo(donnees)

    return donnees


def debut_interne():

    yesno = typer.confirm(
        "Voulez-vous voir les aliments composants notre base de données ?"
    )

    while yesno:
        typer.echo(
            f"""
        Pour répondre aux questions suivantes, veuillez ne rentrer que des valeurs entières ou des valeurs possibles.

        Vous pouvez voir les besoins suivants (séparés d'un espace) :
        Tout, Protéines, Glucides, Lipides, Kcal, Fer, Calcium, Fibres.
    
        Vous pouvez voir les types d'aliments suivants (séparés d'un espace) :
        Tout, Lait, Viande, Poisson, Légume, Base.

        Exemple :

        Combien d'aliments voulez-vous voir ?: 10
        Quelles sont les besoins que voulez-vous voir ?: Kcal Prix
        Quel type d'aliments voulez-vous voir ?: Viande
        """
        )

        ligne = typer.prompt(f"Combien d'aliments voulez-vous voir ?")
        if ligne == "Tout":
            ligne = 41
        else:
            ligne = int(ligne)
        colonnes = typer.prompt(f"Quelles sont les besoins que voulez-vous voir ?")
        if colonnes == "Tout":
            colonnes = []  # défaut.
        else:
            colonnes = colonnes.split()

        type_aliments = typer.prompt(f"Quel type d'aliments voulez-vous voir ?")

        if type_aliments == "Tout":
            type_aliments = ""  # défaut.

        typer.echo(
            project.data._data_aliments_show(
                ligne=ligne, colonnes=colonnes, type=type_aliments
            )
        )

        yesno = typer.confirm(
            "Voulez-vous voir d'autres aliments composants notre base de données ?"
        )


def fin_interne(donnees: project.data.Donnees):
    resultats = project.resolution._resolution(donnees)
    tableau = project.transformation._resolution_transformation(resultats)
    final = project.transformation._transformation_final(tableau)

    typer.echo(resultats)
    typer.echo(final)

    yesno = typer.confirm("Voulez-vous voir plus de détails ?")

    if yesno:
        typer.echo(tableau)


def programme(prenom: str):

    prenom = typer.prompt("Quel est votre nom ?")

    donnees = debut_externe(prenom)  # Base de données externe (besoins).
    debut_interne()  # Base de données interne (aliments).
    fin_interne(donnees)  # Résultats.


if __name__ == "__main__":
    typer.run(programme)
