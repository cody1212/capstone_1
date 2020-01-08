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
class Season():
    def __init__(self, df, date='0'):
        self.nhl = df
        self.date = date
        df2 = nhl.copy()
        self.s = df2
        self.df_last = df2[-1:] # get last row of data frame
        self.end_reg_season={'2011': 13, '2012': 11, '2013': 30, '2014': 16, '2015': 15, '2016': 13, '2017': 12, '2018': 11, '2019': 10}
        arr = str(self.df_last.date_time).split('-') # get date of last row of df and split to get year
        _ = arr[0].split(" ") # turn series object into something useable
        year = _[-1]
        self.final_year = int(year)
    def last_reg_date(self,reg=0):    #finish to include playoffs
        # split out just the year from date given to class
        splt = self.date.split('-')
        year = int(splt[0])
        month = splt[1]
        if month >='01' and month <='04':
            return str(year)+'-04-'+str(self.end_reg_season.get(str(year))-1)
        if year >= self.final_year:                                 # if year is the end of the data frame return the last date available
            return self.df_last.date_time                           #does not work!!!!!!!!!!!!!!
        else:                                                       # else the year is older than the last year in the df return the end of the season date
            new_year=str(year+1)
            next = new_year+'-04-'+str(self.end_reg_season.get(str(new_year))-1)
            return next
    def get_team_ids(self):
        df = self.nhl
        season = df[(df['date_time'] > self.date) & (df['date_time'] < self.last_reg_date())]
        ids = season.home_team_id.unique()
        return ids
    def season_team(self,team_id,stop='0'):
        df = self.nhl
        if stop=='0':
            season = df[(df['date_time'] > self.date) & (df['date_time'] < self.last_reg_date())]
            season = season[(season['home_team_id']==team_id) | (season['away_team_id']==team_id)]
            self.s = season
            return season
        else:
            season = df[(df['date_time'] > self.date) & (df['date_time'] < stop)]
            season = season[(season['home_team_id'] == team_id) | (season['away_team_id'] == team_id)]
            self.s = season
            return season
    def win_lose(self, away_team, home_team, away_goals, home_goals, team_id):
        if team_id != away_team and team_id != home_team:
            return "error"
        if (away_team == team_id and away_goals > home_goals) or (home_team == team_id and home_goals > away_goals):
            return 'w'
        else:
            return 'l'
    def create_win_column(self,team_id):
        df = self.s
        df['win_loss'] = df.apply(lambda col: self.win_lose(int(col[4]), int(col[5]), int(col[6]), int(col[7]), int(team_id)), axis=1)
        return df
    def team_streak(self,df_form=0):
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
        if df_form==0:
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

# create teams dictionary --either of season or streak ...
def data_form(df,yr,start,default=1,df_or_dict=0):
    tms = {}
    nhl = df
    if default != 0:
        for i in range(9):
            season = Season(nhl,(yr + start))
            end = season.end_reg_season.get(str(int(yr)+1))
            for j in season.get_team_ids():
                dt = str(int(yr)+1)+'-04-'+str(end)
                season.season_team(j, stop=dt)
                season.create_win_column(j)
                name = team_info[(team_info['team_id']==j)].abbreviation.max()
                if df_or_dict == 0:
                    tms.update({name +'-'+ yr :season.team_streak()})
                else:
                    tms.update({name +'-'+ yr :season.team_streak(df_form=1)})
            yr = str(int(yr)+1)
    else:
        season = Season(nhl, (yr + start))
        for j in season.get_team_ids():
            for i in range(9):
                end = season.end_reg_season.get(str(int(yr) + 1))
                dt = str(int(yr) + 1) + '-04-' + str(end)
                season.season_team(j, stop=dt)
                season.create_win_column(j)
                name = team_info[(team_info['team_id'] == j)].abbreviation.max()
                if df_or_dict == 0:
                    tms.update({name + '-' + yr: season.team_streak()})
                else:
                    tms.update({name + '-' + yr: season.team_streak(df_form=1)})
                yr = str(int(yr) + 1)
    return tms

def win_streak_per_team_per_season(dct,st,w=1):
    overall = []
    total_winstreaks_per_team_per_season = {}
    if w ==1:
#  ******* winning streaks ********
        for i in dct:
            lst = []
            strk = dct.get(i)
            for j in range(len(strk)):
                if j != len(strk)-1:
                    if strk[j] >= st and strk[j+1]!=strk[j]+1:
                        lst.append(strk[j])
                        overall.append(strk[j])
                else:
                    if strk[j]>= st and strk[j-1]==strk[j]-1:
                        lst.append(strk[j])
                        overall.append(strk[j])
            total_winstreaks_per_team_per_season.update({i:lst})
    else:
# ******* losing streaks ********
        for i in dct:
            lst = []
            strk = dct.get(i)
            for j in range(len(strk)):
                if j != len(strk)-1:
                    if strk[j] <= st and strk[j+1]!=strk[j]-1:
                        lst.append(strk[j])
                        overall.append(strk[j])
                else:
                    if strk[j]<= st and strk[j-1]==strk[j]+1:
                        lst.append(strk[j])
                        overall.append(strk[j])
            total_winstreaks_per_team_per_season.update({i:lst})
    return total_winstreaks_per_team_per_season , overall

def percentage(dct,lst, cnt1,cnt2=0,cnt3=0):
    count_teams_with_none = 0
    team_means = []
    for i in dct:
        c1 = dct.get(i).count(cnt1)
        c2 = dct.get(i).count(cnt2)
        c3 = dct.get(i).count(cnt3)
        dct.get(i)
        print(i)
        if len(dct.get(i)) == 0:
            count_teams_with_none+=1
        else:
            perc = (c1+c2+c3)/len(dct.get(i))
            team_means.append(perc)
            for j in dct.get(i):
                print(j)
            print(perc)
    print(stats.average(team_means))
    print(count_teams_with_none)
teams = data_form(nhl,yr,start,df_or_dict=1)
print(teams)
# teams = data_form(nhl,yr,start)
# dct,lst = win_streak_per_team_per_season(teams,-3,w=0)
# st_len=[]
# cnts=[]
# print(lst)
# for i in range(-3,min(lst)-1,-1):
#     st_len.append(i)
#     cnts.append(lst.count(i))
# print(lst.count(-3),st_len,cnts)
# print((lst.count(-3))/len(lst))
# fig, ax = plt.subplots(1,1)
# ax.hist(st_len,cnts)
# plt.show()
# plt.bar(st_len,cnts)
# plt.show()

# +dct.get(i).count(5)+dct.get(i).count(6)
# df = pd.DataFrame()
# for i in tms:
#     df = df.append(tms.get(i))
# df.to_csv('df.csv',encoding='utf-8')
d={}
# for i in tms:
#     if i.endswith('2010'):
#         j = tms.get(i)
#         for f in range(17):
#             tot = j.count(f)
#             d.update({f:})
# total_winstreaks_per_team_per_season = {}
# def win_streak_per_season_per_team(dct,st,w=1):
df = pd.read_csv('df.csv')
all_teams_by_season = df.copy()
# df = nhl
# season = df[(df['date_time'] > '2010-09-30') & (df['date_time'] < '2010-10-08')]
# print(season)
# on a date check wins assign points to appropriate teams
# after all points added check conf and sort by points
# def get_standings():
# pass in df get back df + standings
# points dict

# win_streaks = {}
# stk_arr=[]
# for team_year in tms:
#     for streak in tms.get(team_year):
#         if streak>3:
#             stk_arr.append(streak)
#     win_streaks.update({team_year:stk_arr})
# print(win_streaks)
# s1 = Season(nhl2,'2018-09-03')
# print(s1.get_team_ids()[7])
# s1.season_team(s1.get_team_ids())
# print(s1.create_win_column(5))
# s1.team_streak()
# print(nhl2)
# lst =nhl2.away_team_id.tolist()
# lst2 = nhl2.home_team_id.tolist()
# lst+=lst2
# print(lst)
# print(tm)
div = pd.read_csv('17-18divs.csv') # how to index a specific table on website then convert to and read csv
# print(div)
df = pd.read_csv('team_info.csv')
div_arr = []
# split conferences
teams = {}
# on a date check wins assign points to appropriate teams
# after all points added check conf and sort by points

# setup divisions by loading in team ids from team info df
# and getting a team name string from a divs df and comparing them to the team_info df
# if date > '2017-06-30':
#     divisions = [[6, 7, 8, 9, 10, 13, 14, 17], [1, 2, 3, 4, 5, 12, 15, 29], [16, 18, 19, 21, 25, 30, 52],
#                  [20, 22, 23, 24, 26, 28, 53, 54]]
#     for i in divisions:
#         df1 = df.copy()
#         div_arr.append(df1[df1['team_id'].isin(i)])

# elif date > '2013-07-01':
# df1 = df.copy()
# div1 = div.copy()
# div1 = div1.loc[div1['year']>2016]
# names = div1['team_name']
# ids = []
# for i in names:
#     name = i.split(' ')
#     stripped_name = name[-1].strip('*')
#     #     how to check for how many occurances of the name there are and select only the last occurance
#     #     need to deal with both occurances of coyotes
#     if stripped_name.lower() == 'coyotes':
#         ids.append(53)
#     else:
#         tms = df1[df1['teamName'].str.contains(stripped_name)]
#         print(tms)
#         for id in tms['team_id']:
#             ids.append(id)
# def print_ids(lst):
#     print(lst)
# print_ids(ids)
# class Standings():
#     def __init__(self,date):
#         div = pd.read_csv('17-18divs.csv')
#         df = pd.read_csv('team_info.csv')
#         div_df = []
#         if date < '2017-6-30':
#             divisions = [[6,7,8,9,10,13,14,17],[1,2,3,4,5,12,15,29],[16,18,19,21,25,30,52],[20,22,23,24,26,28,53,54]]
#             for i in divisions:
#                 df1 = df.copy()
#                 div_df.append(df1[df1['team_id'].isin(i)])
#         elif date < '2013-06-13':
#
#         #     fill in appropriate division teams
#         elif date > '2011-6-15':
#         #     fill for winnipeg
#         elif date <= '2011-6-15':
#         #     fill for atlanta
#
#         for i in df:
#
#     def add_team(self):
#         pass
#     def update(self):
#         pass
#     def show_standings(self):
#
#         pass
#     def get_team(self):
#         pass
# class Team():
#     def __init__(self, name, city, team_id):
#         self.name = name
#         self.city = city
#         self.team_id = team_id
#         self.points = 0
#         self.row = 0
#         self.streak = []
#         self.wins = 0
#         self.losses = 0
# Stands = Standings()

# def ids_from_date(date):

# ar = np.arange(82)
#
# def win_lose(visitor,home,gv,gh,team):
#     if ((visitor == team) and gv>gh) or ((home==team) and gh>gv):
#         return 'w'
#     elif (visitor ==team) or home == team:
#         return 'l'
#     else:
#         np.nan
# team = 'Boston Bruins'
# df['win'] = nhl18.apply(lambda col: win_lose([1],col[3],int(col[2]),int(col[4]),team),axis=1)
# arr = nhl18.copy()
# arr = arr.loc[arr['Visitor']=='Boston Bruins']
# arr2 = nhl18.copy()
# arr2 = arr2.loc[arr2['Home']=='Boston Bruins']
# print(arr)

# a = df[ df.win.notnull()]
# print(a)
# lstw =[]
# lstl =[]
# count=0
# counter=0
# b = list(a.win)
# for i in range(len(b)-1):
#     if counter==81:
#         if b[i] == 'l':
#             count += 1
#             lstl.append(count)
#         else:
#             count += 1
#             lstw.append(count)
#     else:
#         if b[i+1]==b[i]:
#             count+=1
#         else:
#             if count==1:
#                 if b[i] == 'l':
#                     lstw.append(1)
#                 else:
#                     lstl.append(1)
#             if count>1:
#                 if b[i+1] == 'l':
#                     count+=1
#                     lstw.append(count)
#                     count=1
#                 else:
#                     count += 1
#                     lstl.append(count)
#                     count=1
#     counter+=1
# print('losses', lstl)
# print('Wins', lstw)
# print('sums',sum(lstl)," ",sum(lstw))