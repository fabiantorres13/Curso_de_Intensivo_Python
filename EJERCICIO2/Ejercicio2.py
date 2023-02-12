'''
ENUNCIADO -> Crea una agenda de teléfonos que se gestione por consola, que te permita:
            1. Añadir a cualquier persona, indicando nombre y después teléfono
            2. Buscar el teléfono de una persona
'''

import sys


contactos = {'Fabian': 3222560886, 'Má':3105454531, 'Pá':3229523647}

def agenda():
    print("")
    print("Hola, soy \U0001F916 #ContactBot y estas son las consultas con las que te puedo ayudar.")
    print("1. Añadir un contacto.","\n2. Buscar contactos.")

    
    
    while True:
        print("")
        user = input("Escribir mensaje: ")

        if "añadir" in user.lower() or "1"in user:
            añadirContacto()
            while True:
                print("")
                volverMenu = input("¿Quieres hacer otra consulta?: ")
                if volverMenu.lower() == "si":
                    print("-----------------------------------")
                    agenda()
                elif volverMenu.lower() == "no":
                    print("")
                    print("Fue un gusto poder ayudarte...")
                    sys.exit()
                else:
                    print("Opción no válida.")
                    continue


        elif "buscar" in user.lower() or "2"in user:
            buscarContacto()
            print("")
            volverMenu = input("¿Quieres hacer otra consulta?: ")
            if volverMenu.lower() == "si":
                print("-----------------------------------")
                agenda()
            elif volverMenu.lower() == "no":
                print("")
                print("Fue un gusto poder ayudarte...")
                print("")
                sys.exit()
        else: 
            print("Opción no válida.")
            continue
        




def añadirContacto():
    
    
    while True:

        print("")
        print("-----------------------------------")
        print("-- Añadir Nuevo Contacto")
        print("")
        nombre = input("Nombre: ")
        if nombre not in contactos:
            telefono = int(input("Teléfono: "))
            contactos[nombre] = telefono
            print("")
            print("Contacto añadido con éxito.")
            print("-----------------------------------")
            break
        else:
            print("")
            print("El nombre ingresado ya está en tus contactos")
            continue
        
        
    





def buscarContacto():
    
    print("")
    print("-----------------------------------")
    print("-- Buscar Contacto")
    print("")
    nombre = input("Nombre del contacto: ")
    Resultados = {}
    contador = 0
    for i in contactos:
        if nombre.lower() in i.lower():
            Resultados[i] = contactos[i]
            contador += 1
        else:
            continue
    
    if len(Resultados) != 0:
        print("")
        print(f'Resultados de la Búsqueda: {contador} resultados')
        print("")
        for j in Resultados:
            print(f'Contacto: {j}')
            print(f'Teléfono: {Resultados[j]}')
            print("")
        print("-----------------------------------")
    else:
        print("")
        print(f'Resultados de la Búsqueda: {0} resultados')
        print("-----------------------------------")

    
    





agenda()