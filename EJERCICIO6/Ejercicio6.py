'''
ENUNCIADO:
- Crea una función que convierta un password (entre 6 y 12 caracteres) en una cadena de texto 
alfanumérica de 32 caracteres. La función SIEMPRE debe devolver el mismo resultado para la misma entrada.
'''
import getpass
import hashlib


def cifrarContraseña(password):
    password = hashlib.md5(password.encode())
    password_cifrada = password.hexdigest()
    return password_cifrada

password = getpass.getpass("Ingresa la contraseña: ")
print("Contraseña Hasheada:", cifrarContraseña(password))
print("Longitud:", len(cifrarContraseña(password)), "caracteres")





