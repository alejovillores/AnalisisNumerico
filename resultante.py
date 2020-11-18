# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:54:22 2020

@author: alejo
"""

#a.Programar un algoritmo para hallar las ra´ıces reales de un polinomio de orden dos de forma convencional (sin l´ogica adicional).

#Vamos a recurrir a pedir los coeficientes de un polinomio de orden dos para poder averiguar las raices.
import math

        
def resolvente(a,b,c):
    primera_raiz = (-b + math.sqrt(b*b -4*a*c))/(2*a)
    segunda_raiz = (-b - math.sqrt(b*b -4*a*c))/(2*a)
    
    return primera_raiz,segunda_raiz

def obtener_raices():
    #Título
    print("Polinomio de segundo orden: cálculo de raices")

    #Solicitud de coeficientes mediante input
    print("Escriba los coeficientes de el polinomio de segundo orden")

    #Obtención de los coeficientes como a, b y c.
    a = float(input("Proponga el coeficiente que acompaña al x**2: "))
    b = float(input("Proponga el coeficiente que acompaña al x: "))

    c = float(input("Proponga el término independiente: "))
    
    if (b**2-4*a*c) >= 0:
        primera_raiz , segunda_raiz = resolvente(a, b, c)
        print("La primera raiz econtrada es:" + str(primera_raiz))
        print("La segunda raiz econtrada es:" + str(segunda_raiz))
    else:
        print("No hay raíz 2 real")
        
def  test01PolinomioConRaizReal():
    a =  2 
    b = -3 
    c = -5
    
    x1,x2 = resolvente(a, b, c)
    print('Test 01')
    if(x1 == 2.5 ) and (x2 == -1 ):
        print('Bien'+'\n')
    else:
        print('Mal'+'\n')

def  test02PolinomioConRaizReal():
    a =  1 
    b = -5 
    c =  6
    
    x1,x2 = resolvente(a, b, c)
    print('Test 02')
    if(x1 == 3 ) and (x2 == 2 ):
        print('Bien'+'\n')
    else:
        print('Mal'+'\n')

def  test03PolinomioConRaizNoReal():
    a =  2 
    b = -3 
    c =  5
    
    print('Test 03')
    if (b**2-4*a*c) < 0:
        print('Bien'+'\n')
    else:
        print('Mal'+'\n')

obtener_raices()

            

        
        
    
    

