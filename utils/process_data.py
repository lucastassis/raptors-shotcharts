import pandas as pd
import numpy as np

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

if __name__ == '__main__':
    df = pd.read_csv('../data/2020-21/kylelowry.csv') # read csv
    df_league = pd.read_csv('../data/2020-21/league_averages.csv')
    # print(player_fg_zone(df))
    # print(league_fg_zone(df_league))
    print(player_loc_zone(df, 'Above the Break 3'))



