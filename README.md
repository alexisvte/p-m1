# p-m1

_Optimization_ in python.

## But

<div style="text-align: justify">

Développer une application permettant de résoudre un programme alimentaire dépendant de plusieurs contraintes et minimisant le coût :

- Les calories (en Kcal),
- Les protéines (en g),
- Les glucides (en g),
- Les lipides (en g),
- Le fer (en mg),
- Le calcium (en mg),
- Les fibres (en g).

## Documentation

On a une application `project` qu'on appelle avec :

```shell
python3 -m project main
```

Le but de l'application est de proposer à l'utilisateur un repas respectant ses besoins nutritionnels tout en minimisant le coût de ce dernier. L'utilisateur devra répondre à plusieurs questions pour permettre à l'application de lui proposer une liste d'aliments à consommer et le coût de ces derniers.

L'utilisateur pourra, s'il le souhaite, regarder la base de données contenant tous les aliments et leurs informations nutritionnelles. L'utilisateur pourra, s'il le souhaite, regarder la base de données contenant tous les aliments optimisant son régime alimentaire et leurs informations nutritionnelles.

Les étapes de l'application sont :

- De demander les données personnelles à l'utilisateur :
    - Le nom,
    - Les besoins nutritionnels,
- Restituer les aliments optimaux, sous la forme d'une phrase et d'un tableau, c'est à dire :
    - Les aliments permettants d'apporter les besoins nutritionnels nécessaires tout en minimisant le coût.

### Exemple :

```shell
poetry run python -m project main
```

```shell
Quel est votre nom ?: Marie        

    Bonjour Marie !
    
Voulez-vous voir les aliments composants notre base de données ? [y/N]: N

    Pour répondre aux questions suivantes, veuillez ne rentrer que des valeurs entières.

    Exemple :

    Quels sont vos besoins en protéines (en g) ?: 75
    
Quels sont vos besoins en protéines (en g) ?: 75
Quels sont vos besoins en lipides (en g) ?: 90
Quels sont vos besoins en glucides (en g) ?: 225
Quels sont vos besoins en calories (en kcal) ?: 2000
Quels sont vos besoins en fer (en mg) ?: 9
Quels sont vos besoins en calcium (en mg) ?: 800
Quels sont vos besoins en fibres (en g) ?: 45

        Donnees de Marie :

        Protéines : 75 g,
        Lipides : 90 g,
        Glucides : 225 g,
        Kcal : 2000 Kcal,
        Fer : 9 mg,
        Calcium : 800 mg,
        Fibres : 45 g.
        
Vous devez manger 70 grammes de crème fraîche ce qui vous coûtera 0.6 euros.
Vous devez manger 50 grammes de Gruyère ce qui vous coûtera 0.6 euros.
Vous devez manger 50 grammes de Beurre ce qui vous coûtera 0.6 euros.
Vous devez manger 540 grammes de Courge ce qui vous coûtera 1.7 euros.
Vous devez manger 370 grammes de Haricots rouges ce qui vous coûtera 1.6 euros.
Vous devez manger 80 grammes de Haricots blancs ce qui vous coûtera 0.1 euros.
Vous devez manger 130 grammes de Semoule ce qui vous coûtera 0.2 euros.
Le repas vous coûtera 5.4 euros.

        Nous sommes parvenus à optimiser parfaitement le régime alimentaire de Marie.
        

Voulez-vous voir plus de détails ? [y/N]: y
                        Paniers de 100 g  Protéines  Lipides  Glucides    Kcal  Fer  Calcium  Fibres  Prix
                                                                                                          
Lait – crème fraîche                 0.7       15.3     25.7       2.1   240.4  0.0     48.6     0.0   0.6
Lait – Gruyère                       0.5       15.6     16.9       0.2   216.3  0.1    529.6     0.0   0.6
Lait – Beurre                        0.5        0.4     38.9       0.0   344.2  0.0     11.5     0.0   0.6
Légume – Courge                      5.4        3.6      1.8      77.4   302.3  1.9     48.6    15.7   1.7
Base – Haricots rouges               3.7       19.6      1.3      57.9   316.9  4.7     93.2    20.1   1.6
Base – Haricots blancs               0.8        4.2      3.9      16.6   118.8  1.5     46.8     4.2   0.1
Base – Semoule                       1.3       16.2      1.3      93.3   461.0  1.6     21.8     5.0   0.2
Total                               12.9       75.0     90.0     247.5  2000.0  9.9    800.0    45.0   5.4
```

En cours de développement :

12/04/2022 :

```shell
Name                           Stmts   Miss  Cover
--------------------------------------------------
project/__init__.py                3      0   100%
project/data.py                   40     10    75%
project/resolution.py             32      1    97%
project/transformation.py         46      0   100%
tests/__init__.py                  0      0   100%
tests/test_data.py                22      0   100%
tests/test_project.py              4      0   100%
tests/test_resolution.py          27      0   100%
tests/test_transformation.py      32      1    97%
--------------------------------------------------
TOTAL                            206     12    94%
```

25/03/2022 :

```shell
Name                           Stmts   Miss  Cover
--------------------------------------------------
project/__init__.py                3      0   100%
project/data.py                   40     10    75%
project/resolution.py             32      1    97%
project/transformation.py         45     21    53%
tests/__init__.py                  0      0   100%
tests/test_data.py                22      0   100%
tests/test_project.py              4      0   100%
tests/test_resolution.py          27      0   100%
tests/test_transformation.py      34     11    68%
--------------------------------------------------
TOTAL                            207     43    79%
```

</div>
