# p-m1

```diff
+ WORK IS DONE.

! COMMENT IN PROGRESS...

Code needs to be commented.

- IMPROVEMENT...

Create a shiny application in place of this command line application.
```


_Optimization_ in python.

## Goal

<div style="text-align: justify">

> Develop an application to solve a food program depending on several constraints and minimizing the cost:

- Calories (in Kcal),
- Proteins (in g),
- Carbohydrates (in g),
- Lipids (in g),
- Iron (in mg),
- Calcium (in mg),
- Fibers (in g).

## Documentation

We have a `project` application that we call by typing:

```shell
python3 -m project main
```

The purpose of the application is to offer the user a meal that respects his nutritional needs while minimizing the cost of the meal. The user will have to answer several questions to allow the application to offer him a list of foods to eat and their cost.

The user can, if he wishes, look at the database containing all the foods and their nutritional information. At the end, he can, look at the final database  (optimization result) containing all the foods that optimize his diet and their nutritional information.

The application steps are:

- To request personal data from the user:
     - The name,
     - Nutritional needs,
- Restore the optimal foods, in the form of a sentence and a table, ie:
     - Foods that provide the necessary nutritional needs while minimizing the cost.

### Example:

```shell
poetry run python -m project main
```

```shell
What is your name?: Mary

     Hello Marie !
    
Do you want to see the foods that make up our database? [y/N]: N

     To answer the following questions, please enter only integer values.

     Example :

     What are your protein needs (in g)?: 75
    
What are your protein needs (in g)?: 75
What are your fat needs (in g)?: 90
What are your carbohydrate needs (in g)?: 225
What are your calorie needs (in kcal)?: 2000
What are your iron needs (in mg)?: 9
What are your calcium needs (in mg)?: 800
What are your fiber needs (in g)?: 45

         Marie's data:

         Protein: 75g,
         Lipids: 90 g,
         Carbohydrates: 225 g,
         Kcal: 2000 Kcal,
         Iron: 9mg,
         Calcium: 800mg,
         Fibers: 45g.
        
You must eat 70 grams of crème fraîche which will cost you 0.6 euros.
You must eat 50 grams of Gruyère which will cost you 0.6 euros.
You must eat 50 grams of Beurre which will cost you 0.6 euros.
You must eat 540 grams of Courge which will cost you 1.7 euros.
You must eat 370 grams of Haricots rouges which will cost you 1.6 euros.
You must eat 80 grams of Haricots blancs which will cost you 0.1 euros.
You must eat 130 grams of Semoule which will cost you 0.2 euros.
The meal will cost you 5.4 euros.

         We perfectly succeeded to optimize Marie's diet.
        

Do you want to see more details? [y/N]:N
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

In development:

12/04/2021:

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

</div>
