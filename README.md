# CI/CD Final Project — Counter Service

## Nom du projet
**CI/CD Final Project - Counter Service**

## Description
Ce dépôt contient le projet final du cours CI/CD. Il met en œuvre un pipeline
CI/CD complet pour une application Flask (« Counter Service ») en combinant :

- **GitHub Actions** pour l'intégration continue (lint + tests unitaires)
- **Tekton** pour la gestion des tâches de build/test sur OpenShift
- **OpenShift Pipelines** pour le déploiement continu de l'application

## Structure du dépôt

```
.
├── README.md
├── .github/
│   └── workflows/
│       └── workflow.yml      # Pipeline CI : lint (flake8) + tests unitaires (nose)
├── .tekton/
│   └── tasks.yml              # Tâches Tekton : cleanup + nose-test
├── service/
│   ├── __init__.py
│   ├── routes.py              # Routes Flask de l'application
│   └── models.py              # Modèle de données
├── tests/
│   ├── __init__.py
│   └── test_routes.py         # Tests unitaires (nose/nosetests)
├── Dockerfile
└── requirements.txt
```

## Pipeline CI (GitHub Actions)

Le workflow `.github/workflows/workflow.yml` se déclenche à chaque `push` et
`pull_request` sur la branche `main`, et exécute deux étapes principales :

1. **Lint** : analyse statique du code avec `flake8`
2. **Tests unitaires** : exécution de la suite de tests avec `nosetests`

## Pipeline CD (Tekton / OpenShift)

Le fichier `.tekton/tasks.yml` définit les tâches Tekton utilisées par le
pipeline OpenShift :

1. **cleanup** : nettoie l'espace de travail avant chaque exécution
2. **nose-test** : exécute les tests unitaires dans le cluster avant le déploiement

Le pipeline OpenShift (`oc-pipelines-oc-final`) enchaîne : clone du dépôt →
nettoyage → lint → tests → build de l'image → déploiement sur OpenShift.

## Auteur
Aly — HE2B-ESI, Bachelier en informatique, orientation réseaux et télécommunications
