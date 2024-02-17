
#También puede servir el tema del desempaquetado, sirve para crear funciones con argumentos indeterminados

def suma(*args) -> int: #el * hace mencion a un n numero de argumentos que puedo tener 
    """Regresa la suma de varios numeros """
    result= 0
    for argument in args:
        result += argument
    return result


print(suma(1,2,3,4,5,6))#va a imprimir una tupla con los elementos 