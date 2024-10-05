#--------------------------------------------------------------------------
#           Introduccion
# import pandas as pd
# print(pd.DataFrame({'A': [1, 2, 3]}))

#--------------------------------------------------------------------------
#           Creación de objetos: Series
#   Creando un Seriespasando una lista de valores, permitiendo que pandas 
#   cree un valor predeterminado RangeIndex
import numpy as np
import pandas as pd
# s = pd.Series([1, 3, 5, np.nan, 6, 8])        
# print(s)

#--------------------------------------------------------------------------
#           Creación de objetos: DataFrame
#   Creación de un DataFramemétodo pasando una matriz NumPy con un índice 
#   de fecha y hora utilizando date_range() columnas etiquetadas:
dates = pd.date_range("20130101", periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

#   Creando un DataFramepasando un diccionario de objetos donde las claves 
#   son las etiquetas de columna y los valores son los valores de columna.
df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)

#   Las columnas del resultado DataFrametienen diferentes tipos de datos:
print(df2.dtypes)

#--------------------------------------------------------------------------
#           Visualizacion de datos
#   Utilice DataFrame.head()y DataFrame.tail()para ver las filas superior e 
#   inferior del marco respectivamente:
print(df.head(1))
print(df.tail(1))

#   Mostrar el DataFrame.indexo DataFrame.columns:
print(df.index)
print(df.columns)

#   Devuelve una representación NumPy de los datos subyacentes sin 
#   DataFrame.to_numpy() las etiquetas de índice o columna:
print(df.to_numpy())

#   describe()muestra un resumen estadístico rápido de sus datos:
print(df.describe())

#   Transposición de sus datos:
print(df.T)

#   DataFrame.sort_index()ordena por un eje:
print(df.sort_index(axis=1, ascending=False))

#   DataFrame.sort_values()ordena por valores:
print(df.sort_values(by="B"))

#--------------------------------------------------------------------------
#           Selección
#   Si bien las expresiones estándar de Python/NumPy para seleccionar y 
#   configurar son intuitivas y resultan útiles para el trabajo interactivo, 
#   para el código de producción recomendamos los métodos de acceso a datos 
#   de pandas optimizados, DataFrame.at(), DataFrame.iat()y .DataFrame.loc()
#   DataFrame.iloc()

#       Obtener elemento
#   Para a DataFrame, al pasar una sola etiqueta se seleccionan columnas y 
#   se obtiene un Seriesequivalente a df.A:
print(df["A"])

#   Para a DataFrame, al pasar una porción :se seleccionan las filas 
#   coincidentes:
print(df[0:3])
print(df["20130102":"20130104"])

#       Selección por etiqueta
#   Seleccionar una fila que coincida con una etiqueta:
print(df.loc[dates[0]])

#   Seleccionar todas las filas ( :) con etiquetas de columna de selección:
print(df.loc[:, ["A", "B"]])

#   Para el corte de etiquetas, se incluyen ambos puntos finales:
print(df.loc["20130102":"20130104", ["A", "B"]])

#   Al seleccionar una sola etiqueta de fila y columna se obtiene un valor 
#   escalar:
print(df.loc[dates[0], "A"])

#   Para obtener acceso rápido a un escalar (equivalente al método anterior):
print(df.at[dates[0], "A"])

#       Selección por posición
#   Seleccionar a través de la posición de los enteros pasados:
print(df.iloc[3])

#   Las porciones de enteros actúan de manera similar a NumPy/Python:
print(df.iloc[3:5, 0:2])

#   Listas de ubicaciones de posiciones de números enteros:
print(df.iloc[[1, 2, 4], [0, 2]])

#   Para cortar filas explícitamente:
print(df.iloc[1:3, :])

#   Para dividir columnas explícitamente:
print(df.iloc[:, 1:3])

#   Para obtener un valor explícitamente:
print(df.iloc[1, 1])

#   Para obtener acceso rápido a un escalar (equivalente al método anterior):
print(df.iat[1, 1])

#       Indexación booleana
#   Seleccionar filas donde df.A sea mayor que 0.
print(df[df["A"] > 0])

#   Seleccionar valores de un DataFramevalor donde se cumple una condición 
#   booleana:
print(df[df > 0])

#   Usando isin()el método para filtrar:
df2 = df.copy()
df2["E"] = ["one", "one", "two", "three", "four", "three"]
print(df2)
print(df2[df2["E"].isin(["two", "four"])])
#--------------------------------------------------------------------------

#--------------------------------------------------------------------------

