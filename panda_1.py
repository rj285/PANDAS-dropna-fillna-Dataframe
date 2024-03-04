import pandas as pd

data = {
    "cals":[420,380,390],
    "duration":[50,40,45]
    }

df = pd.DataFrame(data) #converting to dataframe
print(df)

print(df.loc[0]) #display zero th index

df = pd.DataFrame(data,index= ["day1","day2","day3"]) #adding new index insted of 0,1,2
print(df)

print(df.loc['day2']) #retriving data of day2
