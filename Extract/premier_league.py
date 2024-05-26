import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_premier_league_data():
    url = 'https://www.premierleague.com/tables'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    teams = []
    points = []

    # Trouver le conteneur des lignes du tableau
    table_body = soup.find('tbody', class_='tableBodyContainer')
    if not table_body:
        return

    # Sélectionner toutes les lignes du tableau
    rows = table_body.find_all('tr')

    for row in rows:
        # Trouver le nom de l'équipe
        team_name_tag = row.find('span', class_='long')
        if team_name_tag:
            team_name = team_name_tag.get_text(strip=True)
            teams.append(team_name)
        else:
            teams.append('N/A')

        # Trouver les points de l'équipe
        points_tag = row.find('td', class_='points')
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

    df_premier_league = pd.DataFrame(data)
    df_premier_league.to_csv('Extract/data/premier_league_data.csv', index=False)
    print("Premier League data saved to premier_league_data.csv")

get_premier_league_data()
