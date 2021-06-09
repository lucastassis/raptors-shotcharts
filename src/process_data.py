'''
Functions used to process the player's input data to facilitate the plots in plot_data.py
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_fgp(df) -> float:
    return round(100 *  len(player_fgm(df)) / len(df), 2)

def player_fgm(df) ->pd.DataFrame:
    idx_made = list(np.where(df["SHOT_MADE_FLAG"] == 1)[0])
    return df.iloc[idx_made]

def player_loc_zone(df, zone) -> pd.DataFrame:
    idx_zone = list(np.where(df["SHOT_ZONE_BASIC"] == zone)[0])
    return df.iloc[idx_zone]

def player_fg_zone(df) -> pd.DataFrame:
    shots_per_zone = df['SHOT_ZONE_BASIC'].value_counts() # number of shots per zone
    shot_zone_basic = shots_per_zone.index.to_numpy() # list of shot zones
    df_grouped = df.groupby('SHOT_ZONE_BASIC').sum() # group df values py shot_zone
    
    df_fg = pd.DataFrame(columns=['FG%'])
    for shot_zone in shot_zone_basic:
        fga = shots_per_zone[shot_zone]
        fgm = df_grouped.loc[shot_zone]['SHOT_MADE_FLAG']
        df_fg.loc[shot_zone] = round(100 * fgm/fga, 2)    
    return df_fg

def league_fg_zone(df) -> pd.DataFrame:
    shots_per_zone = df['SHOT_ZONE_BASIC'].value_counts() # number of shots per zone
    shot_zone_basic = shots_per_zone.index.to_numpy() # list of shot zones
    df_grouped = df.groupby('SHOT_ZONE_BASIC').sum()

    df_fg = pd.DataFrame(columns=['FG%'])
    for shot_zone in shot_zone_basic:
        fg = df_grouped.loc[shot_zone]
        df_fg.loc[shot_zone] = round(100 * (fg['FGM'] / fg['FGA']), 2)
    return df_fg

def fg_per_feet(df) -> pd.DataFrame:
    shots_per_distance = df[['SHOT_DISTANCE', 'SHOT_MADE_FLAG']]
    shots_per_distance = shots_per_distance.groupby('SHOT_DISTANCE').agg(['mean', 'count']).reset_index()
    return shots_per_distance

def freq_per_feet(df) -> pd.DataFrame:
    freq_per_distance = df[['SHOT_DISTANCE']]
    total_shots = len(df[['SHOT_DISTANCE']])
    freq_per_distance = freq_per_distance.value_counts().reset_index()
    freq_per_distance.rename(columns={0 : 'COUNT'}, inplace=True)
    freq_per_distance['COUNT'] = 100 * freq_per_distance['COUNT'] / total_shots
    return freq_per_distance.sort_values('SHOT_DISTANCE')

if __name__ == '__main__':
    df = pd.read_csv('./data/2020-21/kylelowry.csv') # read csv
    df_league = pd.read_csv('./data/2020-21/league_averages.csv')
    # print(player_fg_zone(df))
    # print(league_fg_zone(df_league))
    # print(player_loc_zone(df, 'Above the Break 3'))
    # fg_per_feet(df)
    print(freq_per_feet(df))



