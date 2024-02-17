#Las funciones son bloques de código reutilizables
#print es una función nativa del lenguaje  (existen funciones)
#se componen de nombre y argumentos: print --> ()
#funciones de casting --> int(), float(), dict(), list(), set(), str(), bool(), len ()
#convierten los argumentos al tipo de dato
#len() sirve para saber la cantidad de elementos en una lista
#No solo las listas son iterables, también las cadenas los set, las tuplas ojetos etc...
#los operadores "in" también se pueden ocupar en strings 
#En python todo lo que tenga parentesis se entiende que es una función.
#se puede hacer una referencia a ciertas funciones, por decir: 
#si quiero ocupar len() para saber la longitud de algun dato puedo decir que longitud = len 
#Siendo así ahora en lugar de len() puedo usar longitud()
#def sirve para declarar funciones

#Definiendo una función
#los argumentos pueden ser opcionales (definiendolos con cualquier cosa llendo así al final, caso contrario son obligatorios y estos van al inicio)
#def saludo(nombre = 'null' ):
def hi(name,last_name, age, ocupation):
    """ Saluda al usuario """
    print('Hola',name, last_name)
    print('Tu edad es: ', age)
    print('Te dedicas a ser', ocupation)

#Ejecutando una función
#puedo ponerlo en diferente orden simplemente poniendo el nombre de la variable 
hi('jesus', 'Camacho',21,'developer')
hi(last_name='Lozano', name='Hugo', ocupation='developer', age=24)



