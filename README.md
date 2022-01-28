# IPL Data Analysis Using Python
We have so much data today that it’s used everywhere today, for example, to help a business understand a client’s needs or to help a dating app find the perfect fit for you. So when we analyze a large amount of data to find relationships between different characteristics, it is nothing more than data analysis. To perform IPL Data Analysis using Python also covers how to analyze and visualize data using top libraries in Python. Python's built-in analytics tools make it a perfect tool for processing complex data.

### 1. To print the dataset in match_data frame
```python
print(match_data.head())
```
![image](https://user-images.githubusercontent.com/52828894/151186133-3eb2c49f-29cd-419b-a46e-68fc4e91096c.png)


### 2. To print the dataset in ball_data frame
```python
print(ball_data.head())
```
![image](https://user-images.githubusercontent.com/52828894/151186251-3fb9e728-1a35-43fe-a3d4-f9db23bcab2d.png)


### 3. To figure out how many null values are present in each column
```python
print(match_data.isnull().sum())
```
![image](https://user-images.githubusercontent.com/52828894/151187021-369adb0e-be44-43d0-bc7d-3ec237a6ed65.png)


### 4. To get the total number of rows and columns in a dataset
```python
print(match_data.shape)
print(ball_data.shape)
```
![image](https://user-images.githubusercontent.com/52828894/151187388-508b79f3-43e8-4137-a021-83fff9995fb2.png)


### 5. To print the matches played so far
```python
print('Matches played so far: ', match_data.shape[0])
```
![image](https://user-images.githubusercontent.com/52828894/151194614-3fe15188-feae-48da-9916-b1dc2eebab65.png)


### 6. To print cities in which matches played
```python
print('Cities played at: ', match_data['city'].unique())
```
![image](https://user-images.githubusercontent.com/52828894/151484851-c86e8155-bc50-4d34-86fe-e2ee30774d27.png)


### 7. To print the team names
```python
print('Teams played: ', match_data['team1'].unique())
```
![image](https://user-images.githubusercontent.com/52828894/151485940-5e195e9a-a5e9-4d65-82b6-d645da906126.png)


### 8. To print a new column named Season
```python
match_data['Season'] = pd.DatetimeIndex(match_data['date']).year
print(match_data.head(10))
```
![image](https://user-images.githubusercontent.com/52828894/151555324-80e715c7-8e71-42c9-8ca6-5ec314cc18f5.png)


### 9. Matches played at each season.
```python
match_per_season = match_data.groupby(['Season'])['id'].count().reset_index().rename(columns={'id':'matches'})
print(match_per_season)
```
![image](https://user-images.githubusercontent.com/52828894/151556698-d9b496a3-8d58-4978-8cad-4be5403b29a1.png)

### 10. Total number of matches played Graph
```python
sns.countplot(match_data['Season'])
plt.xticks(rotation=45, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel('Season', fontsize=10)
plt.ylabel('Count', fontsize=10)
plt.title('Total Matches Played in each season', fontsize=10, fontweight='bold')
plt.show()
```
![image](https://user-images.githubusercontent.com/52828894/151560764-e4617eb0-ce75-4c99-b675-3350a70c1e0e.png)

### 11. To merge the match_data and ball_data frames using left join with the column 'id'
```python
season_data = match_data[['id','Season']].merge(ball_data, left_on = 'id', right_on = 'id', how = 'left').drop('id',axis =1)
print(season_data.head())
```
![image](https://user-images.githubusercontent.com/52828894/151563185-2e09acd5-4e05-44b3-8059-37883d3cb9d8.png)

### 12. To visualize the total runs scored in each season
```python
season = season_data.groupby(['Season'])['total_runs'].sum().reset_index()
p = season.set_index('Season')
ax = plt.axes()
ax.set(facecolor= '#E6E6FA')
sns.lineplot(data= p, palette= "magma")
plt.title('Total runs in each season', fontsize=12, fontweight= 'bold')
plt.show()
```
![image](https://user-images.githubusercontent.com/52828894/151566834-8c18a71a-68a6-43b0-add1-b3e965fcefd0.png)

### 13. Runs scored per match in each season
```python
runs_per_season = pd.concat([match_per_season, season.iloc[:,1]], axis=1)
runs_per_season['Runs scored per match'] = runs_per_season['total_runs']/runs_per_season['matches']
runs_per_season.set_index('Season', inplace=True)
print(runs_per_season.head())
```
![image](https://user-images.githubusercontent.com/52828894/151569530-4728805b-1b00-4e10-afd0-c2f153a94e69.png)

### 14. Number of tosses won per team in each season
```python
toss = match_data['toss_winner'].value_counts()
ax = plt.axes()
ax.set(facecolor = "grey")
sns.set(rc={'figure.figsize':(15, 10)},style = 'darkgrid')
ax.set_title('No.of toss won by each team', fontsize=15, fontweight="bold")
sns.barplot(y=toss.index, x=toss, orient='h', palette="icefire", saturation = 1)
plt.xlabel('# of tosses won')
plt.ylabel('Teams')
plt.show()
```
![image](https://user-images.githubusercontent.com/52828894/151571657-839fe6cc-f24c-4402-9d9b-38ba9d52edc5.png)

### 15. Toss Decision Across Seasons
```python
ax = plt.axes()
ax.set(facecolor = "grey")
sns.countplot(x = 'Season', hue = 'toss_decision', data = match_data, palette = "crest", saturation = 1)
plt.xticks(rotation=90, fontsize=10)
plt.yticks(fontsize=15)
plt.xlabel('\n Season', fontsize=15)
plt.ylabel('Count', fontsize=15)
plt.title('Toss decision across seasons', fontsize=15, fontweight="bold")
plt.show()
```
![image](https://user-images.githubusercontent.com/52828894/151576323-b43bf468-b5c9-4e2a-ab8a-189a67f7ba5e.png)


