import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_ligue1_data():
    url = 'https://www.ligue1.com/ranking'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    teams = []
    points = []

    # Trouver tous les éléments de la liste correspondant à chaque équipe
    for row in soup.find_all('li', class_='GeneralStats-row'):
        team_name = row.find('span', class_='GeneralStats-clubName').get_text(strip=True)
        team_points = row.find('div', class_='GeneralStats-item GeneralStats-item--points').get_text(strip=True)
        teams.append(team_name)
        points.append(team_points)

    data = {
        'team': teams,
        'points': points
    }

    df_ligue1 = pd.DataFrame(data)
    df_ligue1.to_csv('Extract/data/ligue1_data.csv', index=False)
    print("Ligue 1 data saved to ligue1_data.csv")

get_ligue1_data()
