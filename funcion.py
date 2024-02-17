
def sum(num1:int,num2:int)-> int: #el -> sirve igual para saber que el resultado es un int
    #Se pueden devolver listas, diccionarios, set etc...
    """Regresa la suma de num1 y num2""" #buena practica indicar lo que hacen las funciones y nomrarlas con lo que hacen
    if isinstance(num1,int) and isinstance(num2,int):
        return num1 + num2
    else:
        print('No se pudo sumar', num1, 'y', num2)
#Acá si no se cumple la condición del if (si no es un numero entero), por defecto va a devolver un none 
#por defecto todas las funciones no devuelven nada

resultado = sum(1,2)

print(resultado)

isinstance(10,str) #permite preguntar si 10 es instancia de str --> retorna falso 
#Tambień funciona con diccionarios

#También puede servir el tema del desempaquetado, sirve para crear funciones con argumentos indeterminados

def suma(*args) -> int: #el * hace mencion a un n numero de argumentos que puedo tener 
    """Regresa la suma de varios numeros """
    result= 0
    for argument in args:
        result += argument
    return result


print(suma(1,2,3,4,5,6))#va a imprimir una tupla con los elementos 