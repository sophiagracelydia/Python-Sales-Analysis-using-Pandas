# IPL Data Analysis Using Python
We have so much data today that it’s used everywhere today, for example, to help a business understand a client’s needs or to help a dating app find the perfect fit for you. So when we analyze a large amount of data to find relationships between different characteristics, it is nothing more than data analysis. To perform IPL Data Analysis using Python also covers how to analyze and visualize data using top libraries in Python. Python's built-in analytics tools make it a perfect tool for processing complex data.

## 1. To print the dataset in match_data frame
### `print(match_data.head())`
![image](https://user-images.githubusercontent.com/52828894/151186133-3eb2c49f-29cd-419b-a46e-68fc4e91096c.png)

## 2. To print the dataset in ball_data frame
### `print(ball_data.head())`
![image](https://user-images.githubusercontent.com/52828894/151186251-3fb9e728-1a35-43fe-a3d4-f9db23bcab2d.png)

## 3. To figure out how many null values are present in each column
### `print(match_data.isnull().sum())`
![image](https://user-images.githubusercontent.com/52828894/151187021-369adb0e-be44-43d0-bc7d-3ec237a6ed65.png)

## 4. To get the total number of rows and columns in a dataset
### `print(match_data.shape)`
### `print(ball_data.shape)`
![image](https://user-images.githubusercontent.com/52828894/151187388-508b79f3-43e8-4137-a021-83fff9995fb2.png)

## 5. To print the matches played so far
### `print('Matches played so far: ', match_data.shape[0])`
![image](https://user-images.githubusercontent.com/52828894/151194614-3fe15188-feae-48da-9916-b1dc2eebab65.png)

## 6. To print cities in which matches played
### `print('Cities played at: ', match_data['city'].unique())`
![image](https://user-images.githubusercontent.com/52828894/151484851-c86e8155-bc50-4d34-86fe-e2ee30774d27.png)

## 7. To print the team names
### `print('Teams played: ', match_data['team1'].unique())`
![image](https://user-images.githubusercontent.com/52828894/151485940-5e195e9a-a5e9-4d65-82b6-d645da906126.png)


