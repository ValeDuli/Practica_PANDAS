import pandas as pd

df=pd.read_csv('productividad.csv')

nuevo_df=df.dropna()
# La instruccion dropna() elimina los 
# renglones que contengan celdas vacias
print(nuevo_df)