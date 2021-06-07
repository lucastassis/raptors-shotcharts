'''
Script for plotting the 2019-20 and 2020-21 visualizations for the four core players
'''
from utils.plot_data import plot_scatter_zone
import pandas as pd

core_players = ['Kyle Lowry', 'Fred Vanvleet', 'OG Anunoby', 'Pascal Siakam']
seasons = ['2020-21']

for season in seasons:
    league_data = pd.read_csv(f'./data/{season}/league_averages.csv') # read league averages for that year
    for player in core_players:
        player_name = player.lower().replace(' ','') # get player name in lowercase and without space
        file_name = player_name + '.csv'
        player_data = pd.read_csv(f'./data/{season}/{file_name}')
        plot_scatter_zone(player_data=player_data, league_data=league_data, player_name=player, player_img=f'./utils/players_pics/{player_name}.png', season=season, out_path=f'./plots/{season}/{player_name}.png', show_plot=False)