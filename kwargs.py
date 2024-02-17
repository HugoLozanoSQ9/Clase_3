def saludar(**kwargs): # El ** doble asterisco me va a convertir todos los argumentos con nombre en un diccionario
    print('Hola',kwargs['nombre'], kwargs['apellido'])


saludar(nombre='Alfredo', apellido='Altamirano', ocupacion='mentor')
#Al momento de ejecutar esto ahora estoy empaquetando en un diccionario la inforamción 
#Dandome como resultado {'arg1':'Hola','arg2':'Koders'}


#adicional, también puedo meter los *args (con un solo *)



def saludar1(nombre, apellido,*args,**kwargs): # El ** doble asterisco me va a convertir todos los argumentos con nombre en un diccionario
#Pero como también tenemos datos definidos, podemos entender que solicita 2 datos obligatorios y los demás pueden ser 'x' datos 
    """
    Saludar
    args:
    nombre(str) : Nombre del koder
    apellido(str) : Apellido del koder
    *args y **Kwargs(str):más elementos 
    """   
    print('Hola',nombre,apellido) 
    
    for arg in args:
        print(arg)

    #print(kwargs) #se pueden imprimir estos datos y recordando que son un diccionario { :  }
    for key, value in kwargs.items(): #recuerda que items(hace que se separen TODOS los elementos y queden como tuplas ordenadas)
        print(key, value) #Aqui solo estoy imprimiendo los valores específicos  y no la tupla como tal 
    
     #Es lo mismo si digo:
    #for key in kwargs:       iteramos key para cada elemento de kwargs
    #   print(key, kwargs[key]) y por cada key iterada consultamos el valor de kwargs[key]
    #Cuando key = 1 --> kwargs[elemento 1 en el valor del diccionario]

saludar1('Alfredo', 'Altamirano', 1,2,3,4,5,6, ocupacion='mentor', edad='36', arg1=5,arg2='Más conetnido')

"""
    Si yo lo pongo de esta forma:
    for values in kwargs.items():  # Cambiamos a 'values' en lugar de 'key, value'
       print(values)  # Imprime cada tupla clave-valor
       por defecto va a imprimir una tupla y mostrará en consola: 
            ('ocupacion', 'mentor')
            ('edad', '36')
            ('arg1', 5)
            ('arg2', 'Más contenido')
    Para este bloque de código en específico

"""

