import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

match_data = pd.read_csv('./IPL Dataset/IPL Matches 2008-2020.csv')
ball_data = pd.read_csv('./IPL Dataset/IPL Ball-by-Ball 2008-2020.csv')


# 1. To print the dataset in match_data frame
print(match_data.head())

# 2. To print the dataset in ball_data frame
print(ball_data.head())

# 3. To figure out how many null values are present in each column
print(match_data.isnull().sum())

# 4. To get the total number of rows and columns in a dataset
print(match_data.shape)
print(ball_data.shape)

# 5. To print the matches played so far
print('Matches played so far: ', match_data.shape[0])

# 6. To print cities in which matches played
print('Cities played at: ', match_data['city'].unique())

# 7. To print the team names
print('Teams played: ', match_data['team1'].unique())

# 8.To print a new column named Season
match_data['Season'] = pd.DatetimeIndex(match_data['date']).year
print(match_data.head(10))

# 9. Matches played at each season.
match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id':'matches'})
print(match_per_season)

# 10. To plot a Graph to display Total matches played
sns.countplot(match_data['Season'])
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Season', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Total Matches Played in each season', fontsize=10, fontweight='bold')
plt.show()

# 11. To merge the match_data and ball_data frames using left join with the column 'id'
season_data = match_data[['id','Season']].merge(ball_data, left_on = 'id', right_on = 'id', how = 'left').drop('id',axis =1)

# 12. To visualize the total runs scored in each season
season = season_data.groupby(['Season'])['total_runs'].sum().reset_index()
p = season.set_index('Season')
ax = plt.axes()
ax.set(facecolor= '#E6E6FA')
sns.lineplot(data= p, palette= "magma")
plt.title('Total runs in each season', fontsize=12, fontweight= 'bold')
plt.show()

# 13. Runs scored per match in each season
runs_per_season = pd.concat([match_per_season, season.iloc[:,1]], axis=1)
runs_per_season['Runs scored per match'] = runs_per_season['total_runs']/runs_per_season['matches']
runs_per_season.set_index('Season', inplace=True)
print(runs_per_season.head())

# 14. Number of tosses won per team in each season
toss = match_data['toss_winner'].value_counts()
ax = plt.axes()
ax.set(facecolor = "grey")
sns.set(rc={'figure.figsize':(15, 10)},style = 'darkgrid')
ax.set_title('No.of toss won by each team', fontsize=15, fontweight="bold")
sns.barplot(y=toss.index, x=toss, orient='h', palette="icefire", saturation = 1)
plt.xlabel('# of tosses won')
plt.ylabel('Teams')
plt.show()

# 15. Toss Decision Across Seasons
ax = plt.axes()
ax.set(facecolor = "grey")
sns.countplot(x = 'Season', hue = 'toss_decision', data = match_data, palette = "flare", saturation = 1)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel('\n Season', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.title('Toss decision across seasons', fontsize=15, fontweight="bold")
plt.show()
