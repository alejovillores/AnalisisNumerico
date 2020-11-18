# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 08:35:12 2020

@author: alejo
"""

'''
1) Pedir a, b, y c
2) Buscar medio
3) Definir los intervalos para la raiz 1 y para la 2
4) Aplicar biseccion hasta la cota de error.
5) Devolver la raiz hallada, la cota , y las iteraciones
'''

#Constantes
TOLERANCIA = 0.000001
LIMITE     = 1000
ERROR      = 0


#Devuelve el punto absoluto mas alto de y
def obtener_medio(a,b):
    medio = (-b / 2*a)
    return medio

#Devuelve el valor de la funcion en ese punto
def f(a,b,c,x):
    y = a * (x*x) + b * x + c
    return y


def buscar_intervalo(coeficientes,lado_inicial,agregado):
    a = coeficientes[0]
    b = coeficientes[1]
    c = coeficientes[2]
    
    lado_final = lado_inicial
    #Buscamos los rangos , si i pasa limite , no hay 

    while (f(a,b,c,lado_inicial)*f(a,b,c,lado_final) > 0):
        lado_inicial = lado_final
        lado_final += (agregado)
    
    return lado_inicial,lado_final

def biseccion(coeficientes,punto_medio,extremo):
    
    a = coeficientes[0]
    b = coeficientes[1]
    c = coeficientes[2]
    
    punto            = (punto_medio + extremo)/2
    punto_anterior   = 0 
    cota             = abs(punto)
    iteraciones      = 0
   
    while (f(a,b,c,punto) != 0) and (cota > TOLERANCIA):
        
        if (f(a,b,c,punto)*f(a,b,c,extremo)) < 0:
            #Si el punto y un extremo dan negativo , entonces la raiz esta ahí. 
            punto_anterior = punto
            punto_medio    = punto
            punto          = (punto_medio + extremo)/2
            iteraciones    += 1
            cota           = abs(punto - punto_anterior)
        else:
            #De no ser asi , acoto el otro extremo
            punto_anterior = punto
            extremo        = punto
            punto          = (punto_medio + extremo)/2
            iteraciones    += 1
            cota           = abs((punto - punto_anterior))
    
    datos = [punto , iteraciones, cota]

    return datos


def busqueda_de_raices():
    a = -1e-7 #float(input("Proponga el coeficiente que acompaña al x**2: "))
    b =  2    #float(input("Proponga el coeficiente que acompaña al x: "))
    c =  1e+5 #float(input("Proponga el término independiente: "))
    
    punto_medio = obtener_medio(a, b)
    coeficientes = [a, b, c]
    
    #CASO 1
    if f(a,b,c,punto_medio) == 0: # Raiz doble..
        print('La funcion posee una raiz doble en:' + str(punto_medio) + '/n')
    else:
        
        #Buscamos los intervalos para la derecha y para la izquierda
        derecha_inicial,derecha_final     = buscar_intervalo(coeficientes,punto_medio, 10)
        izquierda_inicial,izquierda_final = buscar_intervalo(coeficientes,punto_medio,-10)
        
       #Acá basta con evaluar b o j dado que si hay raíz derecha-->hay raíz izquierda también.
       #Entonces , si hay intervalos
        if (derecha_final != ERROR) and (izquierda_final != ERROR):
            #Datos es una lista con : LA RAIZ , LAS ITERACIONES , ERROR.
            datos_derecha   = biseccion(coeficientes,derecha_inicial,derecha_final)
            datos_izquierda = biseccion(coeficientes,izquierda_inicial,izquierda_final)
            
            print('Raiz 1')
            print('X: ' + str(datos_derecha[0]))
            print('Error: '+ str(datos_derecha[2]))
            print('Iteracion numero: '+ str(datos_derecha[1]) + '\n')
            
            print('Raiz 2')
            print('X: ' + str(datos_izquierda[0]))
            print('Error: '+ str(datos_izquierda[2]))
            print('Iteracion numero: '+ str(datos_izquierda[1]) + '\n')
                      
            
        else:
            print("Dicha ecuación cuadrática no tiene raices")
            

busqueda_de_raices()