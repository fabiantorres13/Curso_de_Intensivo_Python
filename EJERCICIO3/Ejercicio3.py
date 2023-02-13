# Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.

def Primos(N):

    listaPrimos = []
    contadorDivisores = 0
    

    for i in range (2,N+1):
        primos = True
        for j in range (2,i):
            if i == j:
                break
            elif i%j == 0:
                primos = False
            else:
                continue
        if primos == True:
            listaPrimos.append(i)
            contadorDivisores += 1

    return f'Los números primos entre 1 y {N} son : {listaPrimos}'

print(Primos(100))


      
        
    
    



