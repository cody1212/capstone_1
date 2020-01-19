# import numpy as np
# x = [10, 25, 12, 35, 14, 18, 16, 15, 22, 10, 9, 11, 49, 20, 15, 9, 18, 19, 20, 20]
# lst = []
# for i in x:
#     y = (i-18.35)**2
#     lst.append(y)
# y = np.array(lst).mean()
# print(y)
import pandas as pd
import numpy as np
pd.set_option("display.max_rows",1300)
odds = pd.read_csv('Sheet1-Table 1.csv')
nhl = pd.read_csv('nhl_sorted_by_dates.csv')
team_info = pd.read_csv('team_info.csv')
print(team_info)
pd.set_option("display.max_columns",12000)
pd.set_option('display.max_rows',12000)
pd.set_option('display.width', 320)
# lst = []
odds = odds[::2]
# print(odds)
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
pd.set_option("display.max_rows",1300)
pd.set_option("display.max_columns",12000)
pd.set_option('display.max_rows',200000)
pd.set_option('display.width', 320)
team_info = pd.read_csv('team_info.csv')
nhl = pd.read_csv('nhl_sorted_by_dates.csv')
odds = pd.read_csv('odds_all_years.csv')
odds = odds[::2]
nhl2 = nhl.copy()
string = '2018-09-30'
d = {1:2,3:4}
# print(d[1])
# class Season():
#     def __init__(self, df, date='0', end_date='0'):
#         self.df = df
#         self.date = date
#         team_info = pd.read_csv('team_info.csv')
#         team_ids = team_info.team_id.tolist()
#         self.team_names = {}
#         for i in team_ids:
#             team_name = team_info[(team_info['team_id']==i)].abbreviation.max()
#             self.team_names.update({i:team_name})
#         df2 = df.copy()
#         self.s = df2
#         self.df_last_row = df2[-1:] # get last row of data frame
#         self.end_reg_season={'2011': 13, '2012': 11, '2013': 30, '2014': 16, '2015': 15, '2016': 13, '2017': 12, '2018': 11, '2019': 10}
#         arr = str(self.df_last_row.date_time).split('-') # get date of last row of df and split to get year
#         _ = arr[0].split(" ") # turn series object into something useable
#         year = _[-1]
#         self.final_year = int(year)
#     def last_reg_date(self,reg=0):    #finish to include playoffs
#         # split out just the year from date given to class
#         splt = self.date.split('-')
#         year = int(splt[0])
#         month = splt[1]
#         if month >='01' and month <='04':
#             return str(year)+'-04-'+str(self.end_reg_season.get(str(year))-1)
#         if year >= self.final_year:                                 # if year is the end of the data frame return the last date available
#             return self.df_last_row.date_time                           #does not work!!!!!!!!!!!!!!
#         else:                                                       # else the year is older than the last year in the df return the end of the season date
#             new_year=str(year+1)
#             next = new_year+'-04-'+str(self.end_reg_season.get(str(new_year))-1)
#             return next
#     def get_team_ids(self):
#         df = self.df
#         season = df[(df['date_time'] > self.date) & (df['date_time'] < self.last_reg_date())]
#         ids = season.home_team_id.unique()
#         return ids
# class Games():
#     def __init__(self,df,start_date,end_date=0):
#
# class Team(Season):
#     def __init__(self, df, start_date, end_date=0, name='0', team_id=0):
#         self.df = df
#         self.name = name
#         self.start_date = start_date
#         self.end_date = end_date
#         self.team_id = team_id
#         self.team = self.team_games()
#         Season.__init__(self.df, self.start_date, self.end_date)
#     def team_games(self):
#         team_id = self.team_id
#         stop = self.end_date
#         df = self.df
#         if stop=='0':
#             season = df[(df['date_time'] > self.date) & (df['date_time'] < self.last_reg_date())]
#             season = season[(season['home_team_id']==team_id) | (season['away_team_id']==team_id)]
#             super().s = season
#             return season
#         else:
#             season = df[(df['date_time'] > self.date) & (df['date_time'] < stop)]
#             season = season[(season['home_team_id'] == team_id) | (season['away_team_id'] == team_id)]
#             super().s = season
#             return season
#     def win_lose(self, away_team, home_team, away_goals, home_goals, team_id):
#         if team_id != away_team and team_id != home_team:
#             return "error"
#         if (away_team == team_id and away_goals > home_goals) or (home_team == team_id and home_goals > away_goals):
#             return 'w'
#         else:
#             return 'l'
#     def create_win_column(self):
#         team_id = self.team_id
#         df = self.team
#         df['win_loss'] = df.apply(lambda col: self.win_lose(int(col[4]), int(col[5]), int(col[6]), int(col[7]), int(team_id)), axis=1)
#         return df
#     def team_streak(self,df_form=0):
#         lst = self.s.win_loss.tolist()
#         ws = [0]
#         for i in lst:
#             if i == 'w':
#                 if ws[-1] > 0:
#                     ws.append(ws[-1] + 1)
#                 else:
#                     ws.append(1)
#             elif i == 'l' and ws[-1] > 0:
#                 ws.append(-1)
#             else:
#                 ws.append(ws[-1] - 1)
#         ws.remove(ws[0])
#         if df_form==0:
#             return ws
#         else:
#             self.s['streak'] = ws
#             return self.s
# class Season():
#     def __init__(self,df,date='0'):
#         self.nhl = df
#         self.date = date
#         df2 = nhl.copy()
#         self.s = df2
#         self.df_last = df2[-1:] # get last row of data frame
#         self.end_reg_season={'2011': 13, '2012': 11, '2013': 30, '2014': 16, '2015': 15, '2016': 13, '2017': 12, '2018': 11, '2019': 10}
#         arr = str(self.df_last.date_time).split('-') # get date of last row of df and split to get year
#         _ = arr[0].split(" ") # turn series object into something useable
#         year = _[-1]
#         self.final_year = int(year)
#     def just_df(self):
#         return self.nhl
#     def last_reg_date(self,reg=0):    #finish to include playoffs
#         # split out just the year from date given to class
#         splt = self.date.split('-')
#         year = int(splt[0])
#         month = splt[1]
#         if month >='01' and month <='04':
#             return str(year)+'-04-'+str(self.end_reg_season.get(str(year))-1)
#         if year >= self.final_year:                                 # if year is the end of the data frame return the last date available
#             return self.df_last.date_time                           #does not work!!!!!!!!!!!!!!
#         else:                                                       # else the year is older than the last year in the df return the end of the season date
#             new_year=str(year+1)
#             next = new_year+'-04-'+str(self.end_reg_season.get(str(new_year))-1)
#             return next
#     def get_team_ids(self):
#         df = self.nhl
#         season = df[(df['date_time'] > self.date) & (df['date_time'] < self.last_reg_date())]
#         ids = season.home_team_id.unique()
#         return ids
#     def season_team(self,team_id,stop='0'):
#         df = self.nhl
#         if stop=='0':
#             season = df[(df['date_time'] > self.date) & (df['date_time'] < self.last_reg_date())]
#             season = season[(season['home_team_id']==team_id) | (season['away_team_id']==team_id)]
#             self.s = season
#             return season
#         else:
#             season = df[(df['date_time'] > self.date) & (df['date_time'] < stop)]
#             season = season[(season['home_team_id'] == team_id) | (season['away_team_id'] == team_id)]
#             self.s = season
#             return season
#     def win_lose(self, away_team, home_team, away_goals, home_goals, team_id):
#         if team_id != away_team and team_id != home_team:
#             return "error"
#         if (away_team == team_id and away_goals > home_goals) or (home_team == team_id and home_goals > away_goals):
#             return 'w'
#         else:
#             return 'l'
#     def create_win_column(self,team_id):
#         df = self.s
#         df['win_loss'] = df.apply(lambda col: self.win_lose(int(col[4]), int(col[5]), int(col[6]), int(col[7]), int(team_id)), axis=1)
#         return df
#     def team_streak(self):
#         lst = self.s.win_loss.tolist()
#         ws = [0]
#         for i in lst:
#             if i == 'w':
#                 if ws[-1] > 0:
#                     ws.append(ws[-1] + 1)
#                 else:
#                     ws.append(1)
#             elif i == 'l' and ws[-1] > 0:
#                 ws.append(-1)
#             else:
#                 ws.append(ws[-1] - 1)
#         ws.remove(ws[0])
#         # self.s['streak'] = ws
#         # return self.s
#         return ws
#     # def divisions(self,conference=0):
# # class Rank(Season):
# #
# del nhl['date_time_GMT']
# del nhl['home_rink_side_start']
# del nhl['venue_link']
# del nhl['venue_time_zone_id']
# yr = '2010'
# start = '-09-30'
# tms = {}
# # nhl2 = nhl.copy()
# # print(nhl.head())
# season = Season(nhl,(yr +'-09-30'))
# for j in season.get_team_ids():
#     for i in range(9):
#         end = season.end_reg_season.get(str(int(yr)+1))
#         # for j in season.get_team_ids():
#         dt = str(int(yr)+1)+'-04-'+str(end)
#         season.season_team(j, stop=dt)
#         season.create_win_column(j)
#         name = team_info[(team_info['team_id']==j)].abbreviation.max()
#         tms.update({name +'-'+ yr :season.team_streak()})
#         yr = str(int(yr)+1)
# del nhl['date_time_GMT']
# del nhl['home_rink_side_start']
# del nhl['venue_link']
# del nhl['venue_time_zone_id']
# for i in team_info['team_id']:
#     print(i)
years = {1:2,3:4}
# print(years[0])
nval= [2,3,4]
name = 'TOR'
x = np.arange(0,4)
y = x[3]

print(y)



# d = {1:3,2:4}
# d.update({1:(3+d.get(1))})
# d.update({1:0})
# d.update
# print(d)
# lst = [1,2,3]
# lst2 = [5,6,7]
# lst3= []
# ..lil more time I could probably pull the points for each team for each game to see if during on a winning or losing streak a team is affected by the opponents rank instead of just looking at the rank of opponents that end a teams streak
# for i in range(len(lst)):
#     lst3.append((lst[i],lst2[i]))
# print(lst3)
# for i in teams:
#     get a dict of opponents points
# for i in teams2:
#     if streak
# class Blah():
#     def __init__(self,x):
#         self.x = x
#         self.make_x()
#     def make_x(self):
#         self.x *= self.x
# thing = Blah(10)
# print(thing.x)
# print(165+ 81+48+ 24+ 8+ 10+ 5+ 1+ 0+ 2)
# nhl2= nhl[(nhl['date_time']>'2018-09-03')&(nhl['date_time']<'2019-04-09')]
# nhl2 = nhl2[(nhl2['away_team_id']==30) | (nhl2['home_team_id']==30)]
# print(len(nhl2))
# lst = [1,2,3]
# print(len(lst))
# for i in range(len(lst)):
#     print(i)
# d = {'h':1, 'j':2, 'r':3}
# for i in d:
#     print(i)
# name = team_info[(team_info['team_id']==j)].abbreviation.max()

# print(nhl2[(nhl2['date_time'] > '2010-03-01') & (nhl2['date_time'] < '2011-06-01')])
# end_reg_season = {11:13,12:11,13:30,14:16,15:15,16:13,17:12,18:11,19:10}
# d = dict()
# for i in end_reg_season.keys():
#     d.update({'20'+str(i):end_reg_season[i]})
# end_reg_season = d
# print(end_reg_season)

# end = int(arr[0])+1
# arr_date = df_last.date_time[0].split('-')
# end = int(arr_date[0])
# print(end)

# WHY DOES THIS NOT WORK???
# del nhl['date_time_GMT']
# del nhl['home_rink_side_start']
# del nhl['venue_link']
# del nhl['venue_time_zone_id']
# yr = '2010'
# tms = {}
# for i in range(9):
#     season = Season(nhl,(yr +'-09-30'))
#     print(season.end_reg_season.get(str(int(yr)+1)))
#     for j in season.get_team_ids():
#         season.season_team(j)
#         season.create_win_column(j)
#         name = team_info[(team_info['team_id']==j)].abbreviation.max()
#         tms.update({name +'-'+ yr :season.team_streak()})
#     yr = str(int(yr)+1)
# for i in tms:
#     print(len(tms.get(i)))