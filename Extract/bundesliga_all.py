import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_bundesliga_data():
    url = 'https://www.bundesliga.com/en/bundesliga/table'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    teams = []
    points = []

    # Sélectionner les lignes du tableau contenant les informations des équipes
    rows = soup.find_all('tr', class_='ng-star-inserted')
    for row in rows:
        # Trouver le nom de l'équipe
        team_name_tag = row.find('td', class_='team')
        if team_name_tag:
            team_name = team_name_tag.find('span', class_='d-none d-sm-inline-block')
            if team_name:
                teams.append(team_name.get_text(strip=True))
            else:
                teams.append('N/A')
        
        # Trouver les points de l'équipe
        points_tag = row.find('td', class_='pts')
        if points_tag:
            team_points = points_tag.find('span')
            if team_points:
                points.append(team_points.get_text(strip=True))
            else:
                points.append('N/A')
        else:
            points.append('N/A')

    # Créer un DataFrame avec les données collectées
    data = {
        'team': teams,
        'points': points
    }

    df_bundesliga = pd.DataFrame(data)
    df_bundesliga.to_csv('Extract/data/bundesliga_data.csv', index=False)
    print("Bundesliga data saved to bundesliga_data.csv")

get_bundesliga_data()
