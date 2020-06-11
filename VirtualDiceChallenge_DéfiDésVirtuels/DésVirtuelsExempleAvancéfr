"""Il s'agit d'un exemple plus complexe de dé virtuel qui utilise des matrices de 1s (pixels blancs) et de -1s (pixels noirs) pour 
représenter le résultat du lancer de dés. Numpy est utilisé pour créer des matrices, matplotlib est utilisé pour le tracé, et random 
est utilisé pour générer des nombres au hasard. Pouvez-vous penser à d'autres modifications de dés virtuels ? Que diriez-vous d'imprimer 
une image réelle d'un dé ? Pouvez-vous créer votre propre jeu de Yahtzee ? Que diriez-vous d'un script qui vous demande combien de fois 
vous voulez lancer les dés et qui enregistre vos lancers dans une chaîne ? Votre imagination est la limite ici !"""

# Importer les librairies nécessaires
import numpy as np
import matplotlib.pyplot as plt
import random


# Création de matrices pour chaque nombre où 1=pixel blanc et -1=pixel noir
un = np.ones((7,7), dtype=int, order='C')
un[3,[3]] = [-1]

deux = np.ones((7,7), dtype=int, order='C')
deux[2,[2]] = [-1]
deux[4,[4]] = [-1]

trois = np.ones((7,7), dtype=int, order='C')
trois[1,[1]] = [-1]
trois[3,[3]] = [-1]
trois[5,[5]] = [-1]

quatre = np.ones((7,7), dtype=int, order='C')
quatre[1,[1]] = [-1]
quatre[5,[5]] = [-1]
quatre[1,[5]] = [-1]
quatre[5,[1]] = [-1]

cinq = np.ones((7,7), dtype=int, order='C')
cinq[1,[1]] = [-1]
cinq[1,[5]] = [-1]
cinq[3,[3]] = [-1]
cinq[5,[1]] = [-1]
cinq[5,[5]] = [-1]

six = np.ones((7,7), dtype=int, order='C')
six[1,[1]] = [-1]
six[1,[5]] = [-1]
six[3,[1]] = [-1]
six[3,[5]] = [-1]
six[5,[1]] = [-1]
six[5,[5]] = [-1]

# Voici une fonction qui utilise matplotlib pour imprimer une image pixelisée en noir et blanc
def arrayPlot(data):
   
    fig, ax = plt.subplots()
    ax.imshow(data, cmap='gray', interpolation='none')

    # Placer les tiques majeures au centre et les tiques mineures sur les bords
    locs = np.arange(len(data))
    for axis in [ax.xaxis, ax.yaxis]:
        axis.set_ticks(locs + 0.5, minor=True)
        axis.set(ticks=locs, ticklabels=[])

    # Allumer la grille pour les tiques mineures
    ax.grid(False, which='minor', linestyle='-')
    plt.show()


# Affecter les matrices aux variables
Rouler1 = un
Rouler2 = deux
Rouler3 = trois
Rouler4 = quatre
Rouler5 = cinq
Rouler6 = six

# Créer une liste de variables possibles
Roules_Possibles = [Rouler1, Rouler2, Rouler3, Rouler4, Rouler5, Rouler6]


# Choisir au hasard une des variables
x = random.choice(Roules_Possibles)
Empty_List = []
Empty_List.append(x)
arrayPlot(x)
