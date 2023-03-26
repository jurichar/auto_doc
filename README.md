# Mon Projet

Ce projet est un exemple de générateur de documentation utilisant Python, Sphinx et GitHub. Il a pour but de vous aider à apprendre les outils DevOps et les bonnes pratiques de développement.

## Prérequis

- Python 3.x
- pip

## Installation

1. Clonez ce dépôt :
`git clone https://github.com/jurichar/auto_doc.git`
`cd auto_doc`

2. Installez les dépendances du projet :
`pip install -r requirements.txt`

## Arborescence

`auto_doc/`\
`│`\
`├── .gitignore # Fichier Git pour ignorer les fichiers/dossiers spécifiques`\
`├── README.md # Fichier README avec des informations sur le projet et son utilisation`\
`├── requirements.txt # Liste des dépendances Python nécessaires pour le projet`\
`│`\
`├── docs/ # Dossier contenant la documentation Sphinx`\
`│ ├── conf.py # Fichier de configuration Sphinx`\
`│ ├── index.rst # Fichier d'accueil de la documentation Sphinx`\
`│ └── _static/ # Dossier pour les fichiers statiques de la documentation (CSS, images, etc.)`\
`│`\
`├── module/ # Dossier contenant le code source Python de\ votre projet`\
`│ ├── init.py # Fichier d'initialisation du module Python`\
`│ └── functions.py # Fichier de fonctionnalité a tester`\
`│`\
`└── tests/ # Dossier contenant les tests unitaires`\
`├── init.py # Fichier d'initialisation des tests`\
`└── test_functions.py # Fichier de tests pour les fonctionnalité`\

## Utilisation

1. Exécutez votre module Python :
`python3 -m module`

2. Générez la documentation avec Sphinx :
`cd docs`
`make html`

La documentation générée se trouvera dans le dossier `docs/_build/html`.

## Tests

Pour exécuter les tests unitaires, utilisez la commande suivante :
`python3 -m unittest discover tests`

## Contribuer

Les contributions sont les bienvenues ! Veuillez suivre ces étapes pour contribuer au projet :

1. Forkez ce dépôt et clonez votre fork.
2. Créez une nouvelle branche pour votre fonctionnalité ou correction de bug.
3. Ajoutez votre code et les tests associés.
4. Assurez-vous que les tests passent et que votre code est conforme aux conventions du projet.
5. Soumettez une pull request vers le dépôt principal.

## Signaler des problèmes

Si vous rencontrez des problèmes ou des bugs, veuillez les signaler en créant une issue sur la page GitHub du projet.
