import pandas as pd         # Se establece pd como un alias de Pandas

dias=[31,28,31,30]          # La lista contiene los datos que se agregarian a la serie

meses=pd.Series(dias, index=["enero","febrero","marzo","abril"])
                            # usando la opcion "index" podemos designar nuestras propias 
                            # etiquetas. Por omision, estas serian numeros del 0 en adelante 
print(meses)                # Se muestra el DataFrame en la pantalla

print(meses["marzo"])