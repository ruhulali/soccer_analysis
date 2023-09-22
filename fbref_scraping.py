# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 16:39:27 2023
@author: Ruhul.Ali
"""
###############################################################################
Links Used:
Ricardo André: 
https://medium.com/@ricardoandreom/how-to-scrape-and-personalize-data-from-fbref-with-python-a-guide-to-unlocking-football-insights-7e623607afca

###############################################################################
### Season 2022-23
# import library
import pandas as pd

# fbref page link
url22_23 = 'https://fbref.com/en/comps/Big5/2022-2023/stats/players/2022-2023-Big-5-European-Leagues-Stats'

# create dataframe from link
df22_23 = pd.read_html(url22_23)
df22_23 = pd.read_html(url22_23)[0]

# creating data with same headers without multi indexing
df22_23.columns = [' '.join(col).strip() for col in df22_23.columns]
df22_23 = df22_23.reset_index(drop=True)

# creating a list with new names
new_columns = []
for col in df22_23.columns:
  if 'level_0' in col:
      new_col = col.split()[-1]  # takes the last name
  else:
      new_col = col
  new_columns.append(new_col)

# rename columns
df22_23.columns = new_columns
df22_23 = df22_23.fillna('')

# rename Matches col as Season and value as dataframe season
df22_23.rename(columns = {'Matches':'Season'}, inplace = True)
df22_23 = df22_23.replace('Matches','2022-23', regex=True)

# remove rows with column headings
df_n = df22_23[ (df22_23['Rk'] == 'Rk') | (df22_23['Player'] == 'Player') ].index
df22_23.drop(df_n , inplace=True)

###############################################################################
### Season 2021-22
# import library
import pandas as pd

# fbref page link
url21_22 = 'https://fbref.com/en/comps/Big5/2021-2022/stats/players/2021-2022-Big-5-European-Leagues-Stats'

# create dataframe from link
df21_22 = pd.read_html(url21_22)
df21_22 = pd.read_html(url21_22)[0]

# creating data with same headers without multi indexing
df21_22.columns = [' '.join(col).strip() for col in df21_22.columns]
df21_22 = df21_22.reset_index(drop=True)

# creating a list with new names
new_columns = []
for col in df21_22.columns:
  if 'level_0' in col:
      new_col = col.split()[-1]  # takes the last name
  else:
      new_col = col
  new_columns.append(new_col)

# rename columns
df21_22.columns = new_columns
df21_22 = df21_22.fillna('')

# rename Matches col as Season and value as dataframe season
df21_22.rename(columns = {'Matches':'Season'}, inplace = True)
df21_22 = df21_22.replace('Matches','2021-22', regex=True)

# remove rows with column headings
df_n = df21_22[ (df21_22['Rk'] == 'Rk') | (df21_22['Player'] == 'Player') ].index
df21_22.drop(df_n , inplace=True)

###############################################################################
### Season 2020-21
# import library
import pandas as pd

# fbref page link
url20_21 = 'https://fbref.com/en/comps/Big5/2020-2021/stats/players/2020-2021-Big-5-European-Leagues-Stats'

# create dataframe from link
df20_21 = pd.read_html(url20_21)
df20_21 = pd.read_html(url20_21)[0]

# creating data with same headers without multi indexing
df20_21.columns = [' '.join(col).strip() for col in df20_21.columns]
df20_21 = df20_21.reset_index(drop=True)

# creating a list with new names
new_columns = []
for col in df20_21.columns:
  if 'level_0' in col:
      new_col = col.split()[-1]  # takes the last name
  else:
      new_col = col
  new_columns.append(new_col)

# rename columns
df20_21.columns = new_columns
df20_21 = df20_21.fillna('')

# rename Matches col as Season and value as dataframe season
df20_21.rename(columns = {'Matches':'Season'}, inplace = True)
df20_21 = df20_21.replace('Matches','2020-21', regex=True)

# remove rows with column headings
df_n = df20_21[ (df20_21['Rk'] == 'Rk') | (df20_21['Player'] == 'Player') ].index
df20_21.drop(df_n , inplace=True)

###############################################################################
# append all seasons
std20_23 = pd.concat([df22_23, df21_22, df20_21], axis=0)
print(std20_23)
###############################################################################
