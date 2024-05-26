import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_laliga_data():
    url = 'https://www.laliga.com/en-GB/laliga-easports/standing'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    teams = []
    points = []

    # Trouver tous les éléments de la liste correspondant à chaque équipe
    for row in soup.find_all('div', class_='styled__StandingTabBody-sc-e89col-0'):
        # Trouver le nom de l'équipe
        team_name_tag = row.find('p', class_='styled__TextStyled-sc-1mby3k1-0 hOVgXP')
        if team_name_tag:
            team_name = team_name_tag.get_text(strip=True)
            teams.append(team_name)
        else:
            teams.append('N/A')

        # Trouver les points de l'équipe
        points_tag = row.find('p', class_='styled__TextStyled-sc-1mby3k1-0 iBRpyN')
        if points_tag:
            team_points = points_tag.get_text(strip=True)
            points.append(team_points)
        else:
            points.append('N/A')

    data = {
        'team': teams,
        'points': points
    }

    df_laliga = pd.DataFrame(data)
    df_laliga.to_csv('Extract/data/laliga_data.csv', index=False)
    print("LaLiga data saved to laliga_data.csv")

get_laliga_data()
