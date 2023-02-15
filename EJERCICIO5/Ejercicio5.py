import pandas as pd

leerArchivo = pd.read_excel('Estudiantes.xlsx')

leerArchivo.to_csv("Estudiantes.csv",
                    index = False,
                    header=True)

df = pd.DataFrame(pd.read_csv("Estudiantes.csv"))

print(df)