# Best_league
Ce projet développe un modèle d'IA pour prédire les points des équipes de football dans les grandes ligues européennes (Ligue 1, LaLiga, Bundesliga, Serie A, Premier League). Il inclut la collecte, le nettoyage, le développement et l'évaluation du modèle.

## Installation et Configuration

### Prérequis

- Python 3.12
- pip (Python package installer)

### Installation des Dépendances

Exécutez la commande suivante pour installer les dépendances nécessaires :

```bash
pip install -r requirements.txt

## Structure du Répertoire

- `Extract/` : Contient les fichiers CSV collectés pour chaque ligue et le scripts qui permet de faire le webscrapping.
- `data_clean/` : Contient les scripts Python pour la préparation, le netoyage des données.
- `ai_model/` : Contient l'entraînement du modèle, l'évaluation et les résultats de l'évaluation.
- `requirements.txt` : Contient les dépendances nécessaires pour l'installation.
- `visualisation/` : Contient le script de l'analyse et de la visualisation.


## Structure du Projet

### Fichiers Principaux

- `bundesliga_all.py, laliga_es.py, ligue1_fr.py, premier_league.py, serieA_it.py` : Script pour collecter les données de chaque ligue.
- `transform_and_load.py` : Script pour préparer et nettoyer les données.
- `traitement.py` : Script pour entraîner le modèle d'IA.
- `evaluat.py` : Script pour évaluer les performances du modèle.
- `visual.py` : Script pour analyser et visualiser les résultats.


###  Résultats et Évaluation

#### Objectif :
Présenter les résultats de l'entraînement et de l'évaluation du modèle.

## Résultats et Évaluation

### Performances du Modèle

- **Régression Linéaire** :
  - RMSE : 7.254711285176827
  - R² : 0.87283319785834

- **Forêt Aléatoire** :
  - RMSE : 3.0009811132503876
  - R² : 0.9782399440593601

### Visualisations

Les histogrammes et les box plots pour la distribution des points des équipes dans chaque ligue sont disponibles dans le répertoire `visualisation/`.


## Améliorations Futures

### Suggestions

1. **Enrichissement des Données** : Inclure plus de caractéristiques, telles que les statistiques des joueurs, les blessures, etc.
2. **Modèles Avancés** : Expérimenter avec des modèles plus complexes, comme les réseaux neuronaux profonds.
3. **Validation Croisée** : Utiliser la validation croisée pour obtenir des estimations plus robustes des performances du modèle.
4. **Déploiement** : Déployer le modèle sous forme d'API web pour permettre des prédictions en temps réel.

## Références

- [Scikit-Learn Documentation](https://scikit-learn.org/stable/documentation.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://docs.python-requests.org/en/latest/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)

##CONCLUSION

La Premier League anglaise se distingue comme la meilleure ligue à inclure dans le nouveau package de streaming. Elle offre un mélange optimal de compétitivité, performances européennes, popularité mondiale, qualité des joueurs et croissance continue. Intégrer la Premier League dans le package assurera un contenu attrayant et de haute qualité, capable de séduire un large public et de maximiser les abonnements au service de streaming.