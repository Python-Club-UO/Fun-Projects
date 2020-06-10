# Utiliser la fonction input() pour recueillir quelques mots de l'utilisateur
# Le string de la fonction leur indiquera ce qu'ils doivent entrer dans la console
# Enregistrer ces mots dans différentes variables
nom = input("Entrez votre nom ")
adjectif = input("Un adjectif ")
animal = input("Quel est votre animal préféré? ")
nom2 = input("Nom de votre meilleur ami ")
verbe = input("Un verb au 3e pluriel passé composé ")
endroit = input("Un endroit ")

# Vous devez maintenant écrire votre histoire et utiliser le format .format() et les parenthèses pour insérer les mots dans votre histoire
# N'oubliez pas d'être créatif ! Ceci n'est qu'un exemple
# Testez votre histoire à plusieurs reprises. Vous devrez peut-être préciser les contributions que vous attendez de votre utilisateur pour que tout ait un sens.
print("Voilà l'histoire de {0} et de leur animal de compagnie {1}.  Un jour, {0} et leur {2} marchaient et ils se sont croisés {3} dans la rue. {3} se promenait et la police s'est approchée pour tenter de les arrêter.  {0} et {3} {4} loin des policiers et a finit par se cacher à {5}.".format(nom,adjectif,animal,nom2,verbe,endroit))

# Ce défi est un peu plus difficile en français en raison de l'accord au masculin et au féminin et de la conjugaison des verbes qui est plus compliquée. Cependant, avec des instructions très précises pour la saisie, c'est possible ! 
# À vous de jouer ! Pratiquez différents formats et types de saisie. Quelle est l'histoire la plus folle que vous pouvez créer ?
