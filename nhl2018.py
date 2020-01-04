import pandas as pd
import numpy as np
pd.set_option("display.max_rows",1300)
nhl18 = pd.read_csv('data/nhl18.csv')
pd.set_option("display.max_columns",50)
ar = np.arange(82)
df = pd.DataFrame(columns =['win'])
def win_lose(visitor,home,gv,gh,team):
    if ((visitor == team) and gv>gh) or (home==team)and gh>gv:
        return 'w'
    else:
        return 'l'
def get_streak(lst):
    ws = [0]
    for i in lst:
        if i == 'w':
            if ws[-1] >0:
                ws.append(ws[-1]+1)
            else:
                ws.append(1)
        elif i == 'l' and ws[-1] > 0:
            ws.append(-1)
        else:
            ws.append(ws[-1] - 1)
    ws.remove(ws[0])
    return ws
team = 'Boston Bruins'
df['win'] = nhl18.apply(lambda col: win_lose([1],col[3],int(col[2]),int(col[4]),team),axis=1)
arr = nhl18.copy()
arr = arr.loc[arr['Visitor']=='Boston Bruins']
arr2 = nhl18.copy()
arr2 = arr2.loc[arr2['Home']=='Boston Bruins']
y = [arr,arr2]
x = pd.concat(y)
x = x.sort_values(by='Date')
del x['Att.']
del x['LOG']
del x['Notes']
del x['OT']
x['w_l']= x.apply(lambda col: win_lose(col[1],col[3],int(col[2]),int(col[4]),team),axis=1)
x['streak'] = get_streak(x.w_l)
print(x)
x.to_csv('nhl_first_draft.csv',encoding='utf 8')
# a = x.copy()
# print('**************************','\n',a)
# lstw =[]
# lstl =[]
# count=0
# counter=0
# b = list(a.win)
# print('losses', lstl)
# print('Wins', lstw)
# print('sums',sum(lstl)," ",sum(lstw))