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
# print(team_info)
pd.set_option("display.max_columns",12000)
pd.set_option('display.max_rows',12000)
pd.set_option('display.width', 320)
# lst = []
odds = odds[::2]
print(odds)
# nhl2 = nhl.copy()
# print(nhl.head())
del nhl['date_time_GMT']
del nhl['home_rink_side_start']
del nhl['venue_link']
del nhl['venue_time_zone_id']
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