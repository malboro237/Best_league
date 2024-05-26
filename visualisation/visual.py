import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lire les fichiers CSV
ligue1_df = pd.read_csv('data_clean/ligue1_data_cleaned.csv')
laliga_df = pd.read_csv('data_clean/laliga_data_cleaned.csv')
bundesliga_df = pd.read_csv('data_clean/bundesliga_data_cleaned.csv')
seriea_df = pd.read_csv('data_clean/seriea_data_cleaned.csv')
premierleague_df = pd.read_csv('data_clean/premier_league_data_cleaned.csv')

# Ajouter une colonne pour identifier la ligue dans chaque dataframe
ligue1_df['league'] = 'Ligue 1'
laliga_df['league'] = 'LaLiga'
bundesliga_df['league'] = 'Bundesliga'
seriea_df['league'] = 'Serie A'
premierleague_df['league'] = 'Premier League'

# Combiner les données
combined_df = pd.concat([ligue1_df, laliga_df, bundesliga_df, seriea_df, premierleague_df])

# Histogramme des points des équipes dans chaque ligue
plt.figure(figsize=(12, 8))
sns.histplot(data=combined_df, x='points', hue='league', multiple='stack', palette='tab10', bins=15)
plt.title('Distribution des Points par Ligue')
plt.xlabel('Points')
plt.ylabel('Nombre d\'équipes')
plt.legend(title='Ligue')
plt.savefig('visualisation/distribution_points_par_ligue.png')
plt.show()

# Box plot pour comparer les distributions de points entre les ligues
plt.figure(figsize=(12, 8))
sns.boxplot(data=combined_df, x='league', y='points', palette='tab10')
plt.title('Comparaison des Distributions des Points entre les Ligues')
plt.xlabel('Ligue')
plt.ylabel('Points')
plt.savefig('visualisation/comparaison_distributions_points.png')
plt.show()

# Bar plot des points moyens par ligue
plt.figure(figsize=(12, 8))
mean_points = combined_df.groupby('league')['points'].mean().reset_index()
sns.barplot(data=mean_points, x='league', y='points', palette='tab10')
plt.title('Points Moyens par Ligue')
plt.xlabel('Ligue')
plt.ylabel('Points Moyens')
plt.savefig('visualisation/points_moyens_par_ligue.png')
plt.show()

# Heatmap de la corrélation des points entre les ligues
plt.figure(figsize=(12, 8))
corr = combined_df.pivot_table(index='league', columns='team', values='points').corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Corrélation des Points entre les Ligues')
plt.savefig('visualisation/correlation_points.png')
plt.show()
