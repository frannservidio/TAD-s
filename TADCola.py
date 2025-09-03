### TAD COLA ####

def crearCola():
    #Crea una cola vacia
    cola = []
    return cola
   
def esVacia(cola):
    #Retorna Verdadero si la cola no tiene elementos
    return len(cola)==0
    
def encolar(cola, elem):
    #Agrega un elemento al final de la cola
    cola.append(elem)

def desencolar(cola):
    #Retorna y elimina el primer elemento de la cola
    elem=cola[0]
    del cola[0]
    return elem
    
def tamanio(cola):
    #Retorna la cantidad de elementos de la cola
    return len(cola)

def copiarCola(cola1,cola2):
    #Copia los datos de una cola a otra
    aux=crearCola() 
    while not esVacia(cola2):
        elem=desencolar(cola2)
        encolar(aux,elem) 
    while not esVacia(aux):
        elem=desencolar(aux)
        encolar(cola1,elem)
        encolar(cola2,elem) 