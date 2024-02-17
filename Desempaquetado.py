#Cuando nosotros tenemos una lista, una tupla, un set o un diccionario se pueden entener como variables empaquetadas
#Se tiene un operador que permite "desempaquetar" los tipos de datos
def hi(name,last_name, age, ocupation):
    print('Hola',name, last_name)
    print('Tu edad es: ', age)
    print('Te dedicas a ser', ocupation)

args1=['Jesus','Camacho','21','develpoer']
hi(*args1)#el * expande la lista y posiciona los elementos de la lista de forma "correcta"

args2={
    'name' : 'Jesus', 
    'last_name':'Camacho',
    'age' : 21 , 
    'ocupation' :'developer'
}
hi(**args2) # Los dobles ** hacen el desempaquetado de los diccionarios

#También se puede hacer que permanezcan ciertos datos o que se mantengan siempre y cuando hallan sido definidos anteriormente 
#por ejemplo si al momento de definir la función tenemos 
#Por buena práctica se recomienda poner el tipo de dato que espera cada uno de los argumentos al momento de llenarlo
def hi1(last_name:str, name :str = 'koder', age:int = 20 , ocupation:str = 'unemployed'):
    print('Hola',name, last_name)
    print('Tu edad es: ', age)
    print('Te dedicas a ser', ocupation)

hi1('Zavala') #por el orden python entiende que zavala es last_name, name no lo estoy definiendo, age y ocupation
#Si lo deseo lo puedo definir sino no pasa nada pq son opcionales


def sum(num1:int,num2:int):
    result =num1 + num2
    return result

resultado = sum(1,2)
print(resultado)

