import pandas as pd

df = pd.read_csv('data.csv')
# print(df)
# print(type(df))
# print(len(df))
# print(df.head(10))
# print(df.tail(10))
# print(df.info()) #shows memmmory usage

# x = df.to_string()
# print(type(x))

# #finding row wise and fill empty area 
# df.dropna() #used to drop the row with the missing values
# df.fillna('NNN',inplace=True) #filling missing values with 666
# # print(df)

# #finding column wise and fill empty area
# df['Calories'].fillna('NNNN', inplace=True) #filling missing values with 999
# # print(df

x = df['Calories'].mean()
print(f"the mean of Calories:- {x}")

df.dropna()
df.fillna(x,inplace=True)
# df.fillna(df['Calories'].mean(),inplace=True)
print(df)
