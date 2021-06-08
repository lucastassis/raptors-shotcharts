'''
Functions to fetch the player's data using the nba_api
'''
from nba_api.stats.endpoints import shotchartdetail
from nba_api.stats.static import teams
from nba_api.stats.static import players
import pandas as pd

'''
Class that stores the player shotchart data
'''
class PlayerShotchart(object):
    def __init__(self, team_city_name='toronto', player_name='Kyle Lowry', season='2019-20'):
        self.team_info = self._get_team_info(team_city_name)
        self.player_info = self._get_player_info(player_name)
        self.season = season
        self._create_shotchart()
        
    # get team info by city
    def _get_team_info(self, city_name='toronto'):
        return teams.find_teams_by_city(city_name)[0]

    # get player info by name
    def _get_player_info(self, player_name='Kyle Lowry'):
        return players.find_players_by_full_name(player_name)[0]
    
    # create shotchart dataframe
    def _create_shotchart(self):
        response = shotchartdetail.ShotChartDetail(team_id=self.team_info['id'], 
                                                   player_id=self.player_info['id'],
                                                   season_type_all_star='Regular Season',
                                                   context_measure_simple='FGA',
                                                   season_nullable=self.season)        
        attributes = ['SHOT_ZONE_BASIC', 'SHOT_ZONE_AREA', 'SHOT_DISTANCE', 'LOC_X', 'LOC_Y', 'SHOT_MADE_FLAG']
        self.shotchart_df = response.get_data_frames()[0][attributes]
    
    # function that returns the shotchart dataframe
    def get_shotchart(self):
        return self.shotchart_df
    
    # function that saves the dataframe into a csv file
    def to_csv(self):
        self.shotchart_df.to_csv(f'../data/{self.season}/{self.player_info["full_name"].lower().replace(" ", "")}.csv')

if __name__ == "__main__":
    # fetch player data
    # klow = PlayerShotchart(team_city_name='toronto', player_name='Kyle Lowry', season='2020-21')
    # klow.to_csv()

    # fetch roster data (except for Malachi Flynn, Jalen Harris and Freddir Gillespie in the 2020-21 roster. nba_api did not find the players :( )
    roster2019_20 = ['Chris Boucher', 'Oshae Brissett', 'Terence Davis', 'Marc Gasol', 'Dewan Hernandez', 'Rondae Hollis-Jefferson', 'Serge Ibaka', 'Stanley Johnson', 'Kyle Lowry', 'Patrick McCaw', 'Malcolm Miller', 'Shamorie Ponds','Norman Powell', 'Pascal Siakam', 'Matt Thomas', 'Fred VanVleet', 'Paul Watson', 'OG Anunoby']
    roster2020_21 = ['Fred VanVleet', 'Pascal Siakam', 'Kyle Lowry', 'OG Anunoby', 'Gary Trent Jr.', 'Khem Birch', 'Norman Powell', 'Chris Boucher', "DeAndre' Bembry", 'Henry Ellenson', 'Aron Baynes', 'Stanley Johnson', 'Terence Davis', 'Yuta Watanabe', 'Rodney Hood', 'Paul Watson', 'Alex Len', 'Matt Thomas', 'Patrick McCaw']

    rosters = [roster2019_20, roster2020_21]
    seasons = ['2019-20', '2020-21']

    for roster, season in zip(rosters, seasons):
        for player in roster:
            print(player)
            shotchart = PlayerShotchart(team_city_name='toronto', player_name=player, season=season)
            shotchart.to_csv()

    
