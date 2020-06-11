# Cette librairie vous permet de choisir un numéro au hasard
import random

# Voici l'exemple le plus simple possible
# Créer une liste avec six numéros possibles
dice = [1,2,3,4,5,6]

# Utilisez la fonction random.choice() pour choisir dans la liste et imprimer
lancer = random.choice(dice)
print(lancer)


# Voici un autre exemple possible
# Générer une liste en utilisant les fonctions list() et range()
# Rappelez-vous, l'argument stop dans range() n'est pas inclus, donc je mets un range de 1-7
dice2 = list(range(1,7))

# J'ai encore utilisé random.choice() pour sélectionner un nombre aléatoire
# Cette fois, j'ai imprimé un message. J'avais besoin de convertir la variable roll2 en string en utilisant str()
lancer2 = random.choice(dice2)
print("Vous avez roulé un  " + str(lancer2))


# Jetez un coup d'oeil à l'exemple avancé pour quelques solutions plus complexes
# N'oubliez pas de tester votre code pour vous assurer que les chiffres sont générés de manière aléatoire à chaque fois 
