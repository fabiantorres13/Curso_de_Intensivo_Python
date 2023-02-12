import os


carpetaPersonal = r"\Users\Administrador\Desktop\Anda_Pa_Alla"

contadorSubdirectorio = 0
contadorFichero = 1

for nombre_directorio, dirs, ficheros in os.walk(carpetaPersonal):
    
    if contadorSubdirectorio == 0:
        print(f'Directorio Principal: {nombre_directorio}')
        contadorSubdirectorio += 1
    else:
        print(f'Subdirectorio {contadorSubdirectorio}: {nombre_directorio}')
        for nombre_fichero in ficheros:
            print(f'Fichero : {nombre_fichero}')
        contadorSubdirectorio += 1
        

