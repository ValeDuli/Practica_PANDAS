import pandas as pd

df=pd.read_csv('productividad.csv')

df["Materiales"].fillna(500, inplace=True)
# La instruccion fillna() remplaza la celdas 
# vacias con un valor especifico, en este caso, 
# el valor de 500, en las celdas de Materiales.

print(df.head(15))