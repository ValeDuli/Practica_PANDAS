import pandas as pd
df=pd.read_csv('productividad.csv')

print(df.head(10))
print(df.tail())

#Informacion general

print(df.info())