import pandas as pd
import os

# Liste des fichiers CSV à traiter
files = [
    'ligue1_data.csv',
    'laliga_data.csv',
    'serieA_data.csv',
    'bundesliga_data.csv',
    'premier_league_data.csv'
]

# Chemins d'accès des dossiers
input_dir = 'Extract/data/'
output_dir = 'data_clean/'

# Créer le dossier de sortie s'il n'existe pas
os.makedirs(output_dir, exist_ok=True)

# Fonction pour charger, prétraiter et sauvegarder les données
def preprocess_and_save(file):
    
    df = pd.read_csv(os.path.join(input_dir, file))
    
    df.fillna(0, inplace=True)
    
    output_file = os.path.join(output_dir, file.replace('.csv', '_cleaned.csv'))
    
    df.to_csv(output_file, index=False)
    
    print(f'File {file} processed and saved as {output_file}')

# Boucle sur chaque fichier
for file in files:
    preprocess_and_save(file)
