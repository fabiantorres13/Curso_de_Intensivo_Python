# ENUNCIADO -> Imprime todos los ficheros existentes en tu carpeta de Descargas.

# Este código logra el objetivo del Ejercicio pero sólo hasta el item 1 de la parte de Ampliación. 
# El item 2 de la parte de Ampliación está en el archivo 'Ampliacion.py'

import os
from humanize import naturalsize

directorio = r"\Users\Administrador\Documents"
contenido = os.listdir(directorio)

contadorFicheros = 1
print("")
print("Los ficheros en este directorio son:")
print("")
for i in contenido:
    if os.path.isfile(os.path.join(directorio, i)):
        tamaño = os.stat(f'C:\\Users\\Administrador\\Documents\\{i}')
        print(contadorFicheros,":",i," - ", naturalsize(tamaño.st_size))
        contadorFicheros += 1

    
        

    