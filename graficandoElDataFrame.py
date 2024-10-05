import pandas as pd
import matplotlib.pyplot as plt
# Esta libreria se usa para graficar los datos.

df=pd.read_csv('productividad.csv')
promedio=df['Materiales'].mean()
df["Materiales"].fillna(promedio, inplace=True)
for x in df.index:
    if df.loc[x,"Horas"]>8:
        df.loc[x,"Horas"]=8

df.plot()
# Genera la grafica en base al DataFrame especificado.

plt.show()
# Despliega el grafico generado en pantalla