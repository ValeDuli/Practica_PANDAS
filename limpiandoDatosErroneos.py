import pandas as pd

df=pd.read_csv('productividad.csv')
for x in df.index:
    if df.loc[x,"Horas"]>8:
        df.loc[x,"Horas"]=8
    # El limite de la jornada laboral de 8 horas. 
    # Usando un ciclo, localiza todos los elementos 
    # de la serie etiquetada con "Horas" que excedan 
    # de ese limite, y los sustituye por un 8.
print(df.head(10))