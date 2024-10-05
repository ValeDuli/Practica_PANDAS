import pandas as pd                                     # Aqui se importa la libreria Pandas

misdatos = {                                            # En esta coleccion de datos guarda la informacion
    'meses': ["enero","febrero","marzo","abril"],       # en forma tabular. Cada lista de datos representa
    'dias':[31,28,31,30]                                # una columna en el DataFrame
}

resultado=pd.DataFrame(misdatos)                        # Aqui se crea el DataFrame y se asigna a una variable

print(resultado)                                        # Con esto veremos la forma que toma el DataFrame en la pantalla