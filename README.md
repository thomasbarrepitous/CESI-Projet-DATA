# Projet DATA - CESI - 3ème Année


## Setup :
Pour ce projet vous allez avoir besoin de modifier tous les chemins de fichiers existant dans respectivement main.py et generation.py. Pour respecter l'architecture des dossiers, gardez la fin de la chaine de caractères (il vous faudra modifier le chemin avant /DATASET/...).

Vous aurez évidemment besoin de Python 3 et d'un IDE.

## Execution :
L'execution principale se déroule au sein du fichier main.py où il y est appelé trois classes :

- VRPGenerator
- Genetic_Algorithm
- Genetic_Algorithm_with_constraint

La première est celle qui, lors de son initialisation va générer un graphe ainsi que des fichiers d'instances qui vont être utilisés par la suite.

La deuxième est un algorithme génétique qui va résoudre le problème du TSP à partir du graphe généré plus tôt.

Le troisième est aussi un algorithme génétique qui va résoudre le problème du VRP à partir du graphe généré plus tôt.

##Utilisation des fichiers :
Pour utiliser un graphe, matrice ou tableau de capacité déjà existant il vous faut tout d'abord commenter la ligne appelant la classe VRPGenerator dans le main.py.
Puis de mettre les même paramètres qu'un fichier existant ou alors de remplacer les chemins à un fichier de votre choix. 
