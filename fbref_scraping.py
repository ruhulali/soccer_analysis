# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 20:34:49 2024
@author: Ruhul.Ali
"""
###############################################################################
# Links Used:
# Ricardo André: 
# https://medium.com/@ricardoandreom/how-to-scrape-and-personalize-data-from-fbref-with-python-a-guide-to-unlocking-football-insights-7e623607afca
###############################################################################
# Season 2023_24

# import library
import pandas as pd

# fbref page link
url23_24 = 'https://fbref.com/en/comps/Big5/2023-2024/stats/players/2023-2024-Big-5-European-Leagues-Stats'

# create dataframe from link
df23_24 = pd.read_html(url23_24)
df23_24 = pd.read_html(url23_24)[0]

# creating data with same headers without multi indexing
df23_24.columns = [' '.join(col).strip() for col in df23_24.columns]
df23_24 = df23_24.reset_index(drop=True)

# rename Matches col as Season and value as dataframe season
df23_24.rename(columns = {'Unnamed: 37_level_0 Matches':'Unnamed: 37_level_0 Season'}, inplace = True)
df23_24 = df23_24.replace('Matches','2023-24', regex=True)

###############################################################################
# Season 2022_23

# fbref page link
url22_23 = 'https://fbref.com/en/comps/Big5/2022-2023/stats/players/2022-2023-Big-5-European-Leagues-Stats'

# create dataframe from link
df22_23 = pd.read_html(url22_23)
df22_23 = pd.read_html(url22_23)[0]

# creating data with same headers without multi indexing
df22_23.columns = [' '.join(col).strip() for col in df22_23.columns]
df22_23 = df22_23.reset_index(drop=True)

# rename Matches col as Season and value as dataframe season
df22_23.rename(columns = {'Unnamed: 37_level_0 Matches':'Unnamed: 37_level_0 Season'}, inplace = True)
df22_23 = df22_23.replace('Matches','2022-23', regex=True)

###############################################################################
# Season 2021_22

# fbref page link
url21_22 = 'https://fbref.com/en/comps/Big5/2021-2022/stats/players/2021-2022-Big-5-European-Leagues-Stats'

# create dataframe from link
df21_22 = pd.read_html(url21_22)
df21_22 = pd.read_html(url21_22)[0]

# creating data with same headers without multi indexing
df21_22.columns = [' '.join(col).strip() for col in df21_22.columns]
df21_22 = df21_22.reset_index(drop=True)

# rename Matches col as Season and value as dataframe season
df21_22.rename(columns = {'Unnamed: 37_level_0 Matches':'Unnamed: 37_level_0 Season'}, inplace = True)
df21_22 = df21_22.replace('Matches','2021-22', regex=True)

###############################################################################
# append all seasons
std_plr_21_24 = pd.concat([df23_24, df22_23, df21_22], axis=0)

# creating a list with new names
new_columns = []
for col in std_plr_21_24.columns:
	if 'level_0' in col:
		new_col = col.split()[-1]  # takes the last name
	else:
		new_col = col
	new_columns.append(new_col)

# rename columns
std_plr_21_24.columns = new_columns
std_plr_21_24 = std_plr_21_24.fillna('')

# remove rows with column headings
df_n = std_plr_21_24[ (std_plr_21_24['Rk'] == 'Rk') | (std_plr_21_24['Player'] == 'Player') ].index
std_plr_21_24.drop(df_n , inplace=True)

print(std_plr_21_24)

###############################################################################
# pbi advanced query

let
    Source = Python.Execute("# Season 2023_24#(lf)#(lf)# import library#(lf)import pandas as pd#(lf)#(lf)# fbref page link#(lf)url23_24 = 'https://fbref.com/en/comps/Big5/2023-2024/stats/players/2023-2024-Big-5-European-Leagues-Stats'#(lf)#(lf)# create dataframe from link#(lf)df23_24 = pd.read_html(url23_24)#(lf)df23_24 = pd.read_html(url23_24)[0]#(lf)#(lf)# creating data with same headers without multi indexing#(lf)df23_24.columns = [' '.join(col).strip() for col in df23_24.columns]#(lf)df23_24 = df23_24.reset_index(drop=True)#(lf)#(lf)# rename Matches col as Season and value as dataframe season#(lf)df23_24.rename(columns = {'Unnamed: 37_level_0 Matches':'Unnamed: 37_level_0 Season'}, inplace = True)#(lf)df23_24 = df23_24.replace('Matches','2023-24', regex=True)#(lf)#(lf)################################################################################(lf)# Season 2022_23#(lf)#(lf)# fbref page link#(lf)url22_23 = 'https://fbref.com/en/comps/Big5/2022-2023/stats/players/2022-2023-Big-5-European-Leagues-Stats'#(lf)#(lf)# create dataframe from link#(lf)df22_23 = pd.read_html(url22_23)#(lf)df22_23 = pd.read_html(url22_23)[0]#(lf)#(lf)# creating data with same headers without multi indexing#(lf)df22_23.columns = [' '.join(col).strip() for col in df22_23.columns]#(lf)df22_23 = df22_23.reset_index(drop=True)#(lf)#(lf)# rename Matches col as Season and value as dataframe season#(lf)df22_23.rename(columns = {'Unnamed: 37_level_0 Matches':'Unnamed: 37_level_0 Season'}, inplace = True)#(lf)df22_23 = df22_23.replace('Matches','2022-23', regex=True)#(lf)#(lf)################################################################################(lf)# Season 2021_22#(lf)#(lf)# fbref page link#(lf)url21_22 = 'https://fbref.com/en/comps/Big5/2021-2022/stats/players/2021-2022-Big-5-European-Leagues-Stats'#(lf)#(lf)# create dataframe from link#(lf)df21_22 = pd.read_html(url21_22)#(lf)df21_22 = pd.read_html(url21_22)[0]#(lf)#(lf)# creating data with same headers without multi indexing#(lf)df21_22.columns = [' '.join(col).strip() for col in df21_22.columns]#(lf)df21_22 = df21_22.reset_index(drop=True)#(lf)#(lf)# rename Matches col as Season and value as dataframe season#(lf)df21_22.rename(columns = {'Unnamed: 37_level_0 Matches':'Unnamed: 37_level_0 Season'}, inplace = True)#(lf)df21_22 = df21_22.replace('Matches','2021-22', regex=True)#(lf)#(lf)################################################################################(lf)# append all seasons#(lf)std_plr_21_24 = pd.concat([df23_24, df22_23, df21_22], axis=0)#(lf)#(lf)# creating a list with new names#(lf)new_columns = []#(lf)for col in std_plr_21_24.columns:#(lf)#(tab)if 'level_0' in col:#(lf)#(tab)#(tab)new_col = col.split()[-1]  # takes the last name#(lf)#(tab)else:#(lf)#(tab)#(tab)new_col = col#(lf)#(tab)new_columns.append(new_col)#(lf)#(lf)# rename columns#(lf)std_plr_21_24.columns = new_columns#(lf)std_plr_21_24 = std_plr_21_24.fillna('')#(lf)#(lf)# remove rows with column headings#(lf)df_n = std_plr_21_24[ (std_plr_21_24['Rk'] == 'Rk') | (std_plr_21_24['Player'] == 'Player') ].index#(lf)std_plr_21_24.drop(df_n , inplace=True)#(lf)#(lf)print(std_plr_21_24)#(lf)"),
    std20_1 = Source{[Name="std_plr_21_24"]}[Value],
    #"Split Column by Delimiter3" = Table.SplitColumn(std20_1, "Age", Splitter.SplitTextByDelimiter("-", QuoteStyle.Csv), {"Age.1", "Age.2"}),
    #"Removed Columns3" = Table.RemoveColumns(#"Split Column by Delimiter3",{"Age.2"}),
    #"Renamed Columns3" = Table.RenameColumns(#"Removed Columns3",{{"Age.1", "Age"}}),
    #"Changed Type" = Table.TransformColumnTypes(#"Renamed Columns3",{{"Rk", Int64.Type}, {"Player", type text}, {"Nation", type text}, {"Pos", type text}, {"Squad", type text}, {"Comp", type text}, {"Age", Int64.Type}, {"Born", Int64.Type}, {"Playing Time MP", Int64.Type}, {"Playing Time Starts", Int64.Type}, {"Playing Time Min", Int64.Type}, {"Playing Time 90s", type number}, {"Performance Gls", Int64.Type}, {"Performance Ast", Int64.Type}, {"Performance G+A", Int64.Type}, {"Performance G-PK", Int64.Type}, {"Performance PK", Int64.Type}, {"Performance PKatt", Int64.Type}, {"Performance CrdY", Int64.Type}, {"Performance CrdR", Int64.Type}, {"Expected xG", type number}, {"Expected npxG", type number}, {"Expected xAG", type number}, {"Expected npxG+xAG", type number}, {"Progression PrgC", Int64.Type}, {"Progression PrgP", Int64.Type}, {"Progression PrgR", Int64.Type}, {"Per 90 Minutes Gls", type number}, {"Per 90 Minutes Ast", type number}, {"Per 90 Minutes G+A", type number}, {"Per 90 Minutes G-PK", type number}, {"Per 90 Minutes G+A-PK", type number}, {"Per 90 Minutes xG", type number}, {"Per 90 Minutes xAG", type number}, {"Per 90 Minutes xG+xAG", type number}, {"Per 90 Minutes npxG", type number}, {"Per 90 Minutes npxG+xAG", type number}, {"Season", type text}}),
    #"Split Column by Delimiter" = Table.SplitColumn(#"Changed Type", "Nation", Splitter.SplitTextByEachDelimiter({" "}, QuoteStyle.Csv, false), {"Nation.1", "Nation.2"}),
    #"Changed Type1" = Table.TransformColumnTypes(#"Split Column by Delimiter",{{"Nation.1", type text}, {"Nation.2", type text}}),
    #"Removed Columns" = Table.RemoveColumns(#"Changed Type1",{"Nation.1"}),
    #"Renamed Columns" = Table.RenameColumns(#"Removed Columns",{{"Nation.2", "Nation"}}),
    #"Split Column by Delimiter1" = Table.SplitColumn(#"Renamed Columns", "Pos", Splitter.SplitTextByEachDelimiter({","}, QuoteStyle.Csv, false), {"Pos.1", "Pos.2"}),
    #"Changed Type2" = Table.TransformColumnTypes(#"Split Column by Delimiter1",{{"Pos.1", type text}, {"Pos.2", type text}}),
    #"Removed Columns1" = Table.RemoveColumns(#"Changed Type2",{"Pos.2"}),
    #"Renamed Columns1" = Table.RenameColumns(#"Removed Columns1",{{"Pos.1", "Pos"}}),
    #"Split Column by Delimiter2" = Table.SplitColumn(#"Renamed Columns1", "Comp", Splitter.SplitTextByEachDelimiter({" "}, QuoteStyle.Csv, false), {"Comp.1", "Comp.2"}),
    #"Changed Type3" = Table.TransformColumnTypes(#"Split Column by Delimiter2",{{"Comp.1", type text}, {"Comp.2", type text}}),
    #"Removed Columns2" = Table.RemoveColumns(#"Changed Type3",{"Comp.1"}),
    #"Renamed Columns2" = Table.RenameColumns(#"Removed Columns2",{{"Comp.2", "Comp"}})
in
    #"Renamed Columns2"
    
