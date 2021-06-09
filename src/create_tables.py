'''
Script for creating the 2019-20 and 2020-21 data tables for the four core players and team
'''
import process_data
import pandas as pd
import numpy as np

core_players = ['Kyle Lowry', 'Fred VanVleet', 'OG Anunoby', 'Pascal Siakam', 'roster_data']
seasons = ['2019-20', '2020-21']

for season in seasons:
    league_data = pd.read_csv(f'./data/{season}/league_averages.csv')
    league_fg_zone = process_data.league_fg_zone(league_data)
    out_table_df = pd.DataFrame(index=league_fg_zone.index)
    league_fg_zone = league_fg_zone['FG%'].to_numpy()
    idx = 0 # column idx

    for player in core_players:
        # prepare fg per zone
        player_name = player.lower().replace(' ','') # get player name in lowercase and without space
        player_data = pd.read_csv(f'./data/{season}/{player_name}.csv')
        player_fg_zone = process_data.player_fg_zone(player_data)

        # insert data on table
        out_table_df.insert(idx, player, player_fg_zone)

        # add idx
        idx += 1
    # insert league data on table
    out_table_df.insert(idx, 'League Averages', league_fg_zone)
    print(out_table_df.to_markdown())



