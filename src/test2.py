import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_rows", 1300)
pd.set_option("display.max_columns", 12000)
pd.set_option('display.max_rows', 200000)
pd.set_option('display.width', 320)
team_info = pd.read_csv('team_info.csv')
nhl = pd.read_csv('nhl_sorted_by_dates.csv')
odds = pd.read_csv('odds_all_years.csv')
odds = odds[::2]
nhl2 = nhl.copy()
string = '2018-09-30'


class Season():
    def __init__(self, df, date='0'):
        self.nhl = df
        self.date = date
        df2 = nhl.copy()
        self.s = df2
        self.df_last = df2[-1:]  # get last row of data frame
        self.end_reg_season = {'2011': 13, '2012': 11, '2013': 30, '2014': 16, '2015': 15, '2016': 13, '2017': 12,
                               '2018': 11, '2019': 10}
        self.ids = self.get_team_ids()
        arr = str(self.df_last.date_time).split('-')  # get date of last row of df and split to get year
        _ = arr[0].split(" ")  # turn series object into something useable
        year = _[-1]
        self.final_year = int(year)

    def last_reg_date(self, reg=0):  # finish to include playoffs
        # split out just the year from date given to class
        splt = self.date.split('-')
        year = int(splt[0])
        month = splt[1]
        if month >= '01' and month <= '04':
            return str(year) + '-04-' + str(self.end_reg_season.get(str(year)) - 1)
        else:  # else the year is older than the last year in the df return the end of the season date
            new_year = str(year + 1)
            next = new_year + '-04-' + str(self.end_reg_season.get(str(new_year)) - 1)
            return next

    def get_team_ids(self):
        df = self.nhl
        season = df[(df['date_time'] > self.date) & (df['date_time'] < self.last_reg_date())]
        ids = season.home_team_id.unique()
        return ids


# ***************************************************************************************************************
class Teams():
    def __init__(self, df, date='0', yr='2010', start='-09-30', stop_yr=2019):
        self.df = df
        self.s = df.copy()
        self.date = yr + start
        self.yr = yr
        self.start = start
        self.stop_yr = stop_yr
        self.season = Season(self.df, self.date)
        self.streaks_dictionary = self.data_form()
        self.teams_dfs_dictionary = self.data_form(df_or_dict=1)
        team_id_dict = {}
        ids = team_info.team_id.tolist()
        names = team_info.abbreviation.tolist()
        for i in range(len(ids)):
            team_id_dict.update({ids[i]: names[i]})
        names_id_dict = {}
        for i in range(len(names)):
            names_id_dict.update({names[i]: ids[i]})

    def data_form(self, default=1, df_or_dict=0):
        tms = {}
        yr = self.yr
        df = self.df
        yr1 = int(self.yr)
        if default != 0:
            for i in range(self.stop_yr - yr1):
                season = Season(self.df, (self.yr + self.start))
                end = self.season.end_reg_season.get(str(int(yr) + 1))
                dt = str(int(yr) + 1) + '-04-' + str(end)
                for j in season.get_team_ids():
                    self.season_team(j, stop=dt)
                    self.create_win_column(j)
                    name = team_info[(team_info['team_id'] == j)].abbreviation.max()
                    if df_or_dict == 0:
                        tms.update({name + '-' + yr: self.team_streak()})
                    else:
                        tms.update({name + '-' + yr: self.team_streak(df_form=1)})
                yr = str(int(yr) + 1)
        return tms

    def season_team(self, team_id, stop='0'):
        df = self.df
        if stop == '0':
            seas = df[(df['date_time'] > str(self.date)) & (df['date_time'] < self.season.last_reg_date())]
            seas = seas[(seas['home_team_id'] == team_id) | (seas['away_team_id'] == team_id)]
            self.s = seas
            return seas
        else:
            seas = df[(df['date_time'] > str(self.date)) & (df['date_time'] < str(stop))]
            seas = seas[(seas['home_team_id'] == team_id) | (seas['away_team_id'] == team_id)]
            self.season.s = seas
            return seas

    def win_lose(self, away_team, home_team, away_goals, home_goals, team_id):
        if team_id != away_team and team_id != home_team:
            return "error"
        if (away_team == team_id and away_goals > home_goals) or (home_team == team_id and home_goals > away_goals):
            return 'w'
        else:
            return 'l'

    def create_win_column(self, team_id):
        df = self.s
        df['win_loss'] = df.apply(
            lambda col: self.win_lose(int(col[4]), int(col[5]), int(col[6]), int(col[7]), int(team_id)), axis=1)
        return df

    def team_streak(self, df_form=0):
        lst = self.s.win_loss.tolist()
        ws = [0]
        for i in lst:
            if i == 'w':
                if ws[-1] > 0:
                    ws.append(ws[-1] + 1)
                else:
                    ws.append(1)
            elif i == 'l' and ws[-1] > 0:
                ws.append(-1)
            else:
                ws.append(ws[-1] - 1)
        ws.remove(ws[0])
        if df_form == 0:
            return ws
        else:
            self.s['streak'] = ws
            return self.s


del nhl['date_time_GMT']
del nhl['home_rink_side_start']
del nhl['venue_link']
del nhl['venue_time_zone_id']

yr = '2010'
start = '-09-30'
teams87 = Teams(nhl)

