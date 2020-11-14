# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 09:25:44 2020

@author: Alejo Villores 
"""
import matplotlib.pyplot as plt
import numpy as np
import random

#Constante
INTENTOS = 100000
COLUMNAS = 1000


# Pre:  Recibe un numero random
# Post: Devuelve la cantidad de iteraciones hechas hasta coinicidir
def fuerza_bruta(n_random):
    encontrado  = False
    iteraciones = 0
    
    while encontrado != True:
        if iteraciones == n_random:
            encontrado = True
        else:
            iteraciones += 1
    
    return iteraciones

# Pre:  Recibe un numero de iteraciones.
# Post: Devuelve la posicion donde debe ir ese numero.
def posicion_del_numero(n_iteraciones):
    
    # Divido el numero por 10 para acotar el rango
    # Lo paso a string para tener control de la posicion     
    n_iteraciones = str(n_iteraciones/10)
    
    # Busco la posicion de la coma
    posicion_coma = n_iteraciones.index(".")
    
    # Devuelvo el numero sin la coma que representa la pos
    return n_iteraciones[:posicion_coma]

# Pre:  - 
# Post: Muestra un histograma con los intentos del problema candado
def candado():
    
    #Inicializo un array con 1000 posiciones.
    histograma = np.zeros(COLUMNAS)
    
    for i in range(INTENTOS):
        
        n_random        = random.randint(0, 9999)
        n_iteraciones   = fuerza_bruta(n_random)
        pos_iteraciones = posicion_del_numero(n_iteraciones) 
        
        histograma[int(pos_iteraciones)] += 1
        
    return histograma

resultado = candado()

plt.hist(resultado,bins = COLUMNAS)
plt.title("Distribución de 10000 claves")
plt.xlabel("Iteraciones medias")
plt.grid()
plt.show()




