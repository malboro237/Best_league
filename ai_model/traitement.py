import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Charger les données
ligue1_df = pd.read_csv('data_clean/ligue1_data_cleaned.csv')
laliga_df = pd.read_csv('data_clean/laliga_data_cleaned.csv')
bundesliga_df = pd.read_csv('data_clean/bundesliga_data_cleaned.csv')
seriea_df = pd.read_csv('data_clean/seriea_data_cleaned.csv')
premierleague_df = pd.read_csv('data_clean/premier_league_data_cleaned.csv')

# Ajout de rangs et de points précédents
for df in [ligue1_df, laliga_df, bundesliga_df, seriea_df, premierleague_df]:
    df['previous_points'] = df['points'].shift(1, fill_value=0)
    df['rank'] = df['points'].rank(ascending=False)

# Combiner les données
combined_df = pd.concat([ligue1_df, laliga_df, bundesliga_df, seriea_df, premierleague_df])
combined_df.fillna(0, inplace=True)

# Caractéristiques et étiquettes
features = combined_df[['previous_points', 'rank']]
labels = combined_df['points']

# Normalisation des données
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(features_scaled, labels, test_size=0.2, random_state=42)

