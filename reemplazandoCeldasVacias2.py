import pandas as pd

df=pd.read_csv('productividad.csv')

promedio=df['Materiales'].mean()
# Se usa la funcion mean() para calcular el 
# promedio. Esta es una de las muchas 
# funciones de calculo estadistico disponibles 
# en el Python

df["Materiales"].fillna(promedio, inplace=True)
print(df.head(15))