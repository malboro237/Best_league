import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_seriea_data():
    url = 'https://www.legaseriea.it/en/serie-a/classifica'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    teams = []
    points = []

    # Trouver la table de classement
    table = soup.find('table', class_='table table-responsive hm-table hm-table-none')
    if not table:
        return

    # Sélectionner les lignes du tableau à partir de tbody
    rows = table.find('tbody').find_all('tr')

    for row in rows:
        # Trouver le nom de l'équipe
        team_name_tag = row.find('div', class_='team-name')
        if team_name_tag:
            team_name = team_name_tag.get_text(strip=True)
            teams.append(team_name)
        else:
            teams.append('N/A')

        # Trouver les points de l'équipe
        points_tag = row.find('td', class_='bold primary-200 text-center')
        if points_tag:
            team_points = points_tag.get_text(strip=True)
            points.append(team_points)
        else:
            points.append('N/A')

    # Créer un DataFrame avec les données collectées
    data = {
        'team': teams,
        'points': points
    }

    df_seriea = pd.DataFrame(data)
    df_seriea.to_csv('Extrac/data/seriea_data.csv', index=False)
    print("Serie A data saved to seriea_data.csv")

get_seriea_data()
