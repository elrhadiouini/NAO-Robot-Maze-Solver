# NAO Robot Maze Solver

## Vue d'ensemble
Ce projet présente une solution de résolution de labyrinthes utilisant le robot humanoïde NAO. Le système basé sur Python permet au NAO de naviguer de manière autonome à travers des labyrinthes, en identifiant et en évitant les obstacles grâce à ses capteurs intégrés.

## Fonctionnalités
- **Navigation Autonome** : Le robot NAO peut naviguer de manière indépendante à travers les labyrinthes.
- **Détection d'Obstacles** : Utilise le sonar pour détecter et éviter les obstacles.
- **Planification Dynamique de Trajectoire** : Calcule le chemin optimal en temps réel.

## Prérequis
- Python 2.7 ou ultérieur
- SDK NAOqi

## Installation
Assurez-vous d'avoir installé le SDK NAOqi et Python correctement. Clonez ce dépôt sur votre machine locale.

```bash
git clone git@github.com:elrhadiouini/NAO-Robot-Maze-Solver.git
cd NAO-Robot-Maze-Solver
```

## Utilisation
Pour exécuter le solveur de labyrinthe, exécutez la commande suivante, en remplaçant ip et port par l'adresse IP et le numéro de port de votre robot :
python main.py --ip [Adresse_IP_Robot] --port [Port_Robot]

## Fonctionnement
- **Initialisation** :  Établit une connexion avec le robot NAO et initialise ses paramètres de posture et de mouvement.
- **Navigation dans le Labyrinthe** : Utilise la classe Maze_finder pour traiter les données des capteurs et prendre des décisions pour la planification du trajet.
- **Évitement d'Obstacles** :  Utilise des capteurs sonar pour détecter les obstacles et ajuste dynamiquement le chemin.
## Contribution
Les contributions à ce projet sont les bienvenues. Veuillez forker le dépôt et soumettre une demande de tirage (pull request) avec vos modifications.
## Contact
Pour toute question, n'hésitez pas à contacter elrhadiouini.zakaria@gmail.com.
