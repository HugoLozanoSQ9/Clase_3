def ejecutar(funcion, *args):
    return funcion(*args)
            #Estoy definiendo que funcion va a ser tal cual (*args) la podemos ejecutar o visualizar pq tenemos el return

def suma(*args) -> int: #el * hace mencion a un n numero de argumentos que puedo tener 
    """Regresa la suma de varios numeros """
    result= 0
    for argument in args:
        result += argument
    return result

ejecutar(print, 'Hola', 'Koder')

print(ejecutar(suma, 1,2,3,4,5,6))
#ejecutar ( funcion --> suma , *args --> del 1 al 6)