import pandas as pd
import numpy as np
pd.set_option("display.max_rows",999)
caps2018 = pd.read_csv('data/caps2018.csv')
c18 = caps2018.copy()
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# reading csv file from url

new = c18["Streak"].str.split("W", n=1, expand=True)

# making separate first name column from new data frame
c18["W/L"] = new[0]

# making separate last name column from new data frame
c18["Streak Count"] = new[1]

# Dropping old Name columns
del c18['Streak']
del c18['GP']
print(c18)
# print(c18['Streak Count'].value_counts())
a = ['w','w','w','w','l','l','w','l','l','l','w','w','l']
b = [4,1,2]
print(len(a))
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
print(get_streak(a))