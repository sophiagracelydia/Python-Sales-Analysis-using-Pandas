## To print the dataset in match_data frame
### `print(match_data.head()`
![image](https://user-images.githubusercontent.com/52828894/151186133-3eb2c49f-29cd-419b-a46e-68fc4e91096c.png)

## To print the dataset in ball_data frame
### `print(ball_data.head()`
![image](https://user-images.githubusercontent.com/52828894/151186251-3fb9e728-1a35-43fe-a3d4-f9db23bcab2d.png)

## To figure out how many null values are present in each column
### `print(match_data.isnull().sum()`
![image](https://user-images.githubusercontent.com/52828894/151187021-369adb0e-be44-43d0-bc7d-3ec237a6ed65.png)

## To get the total number of rows and columns in a dataset
### `print(match_data.shape)`
### `print(ball_data.shape)`
![image](https://user-images.githubusercontent.com/52828894/151187388-508b79f3-43e8-4137-a021-83fff9995fb2.png)

## To print the matches played so far
### `print('Matches played so far: ', match_data.shape[0])`
![image](https://user-images.githubusercontent.com/52828894/151194614-3fe15188-feae-48da-9916-b1dc2eebab65.png)
