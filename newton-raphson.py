# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 08:27:22 2020

@author: alejo
"""

# 1Eva_IT2017_T2 Tanque esférico-volumen
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
fx = lambda h: 1 - np.pi*(h*2)+(np.pi/3)*h*3
dfx = lambda h: -2*np.pi*h+np.pi*(h**2)

# Parámetros de método
a = 0
b = 2
tolera = 0.01
x0 = 1.6
iteramax = 100

# parametros de gráfica
La = a
Lb = b
muestras = 21

# PROCEDIMIENTO
# Newton-Raphson
tabla = []
tramo = abs(2*tolera)
xi = x0
while (tramo>=tolera):
    xnuevo = xi - fx(xi)/dfx(xi)
    tramo = abs(xnuevo-xi)
    tabla.append([xi,xnuevo,tramo])
    xi = xnuevo
tabla = np.array(tabla)

# calcula para grafica
hi = np.linspace(La,Lb,muestras)
fi = fx(hi)
gi = dfx(hi)

# SALIDA  
print(' [ xi,             xnuevo,        tramo      ]')
print(tabla)
print('raiz', xnuevo)
plt.plot(hi,fi)
plt.plot(xi,fx(xi),'ro')
plt.axhline(0, color='green')
plt.xlabel('h')
plt.ylabel('V')
plt.title('Método Newton-Raphson')
plt.show()

#%%
%Defino las constantes:
R=4.25; %Radio del tanque
p=3.14; %Numero Pi

errorrel=1E-5; %Error relativo entre las distintas iteraciones
max_iter=1000; %Cantidad maxima de iteraciones
n=input('Ingrese el porcentaje (en [%]):');

vo=964.66*n; %Calculo el valor inicial
ho=8.5;
hk= ho;
hu=2; %Semilla"

h_tanque=hk; %Defino el vector de iteraciones para luego exportar el valor
k_iteracion=0;
 
while (abs(hk-hu)/abs(hk))>errorrel %Compruebo si hay que iterar una vez mas segun el error relativo
    if k_iteracion>max_iter %Si se ve que no va a converger, se corta el calculo
        disp('\nError: La soluciÃ³n no converge.');
        return
    end
    hu=hk; %Seteo el valor anterior
    hk=hk-(((((p)(hk*hk))(12.75 - hk))/3)-385)/((p/3)((2(12.75-hk)*hk)-(hk*hk))); %Calculo el valor de la siguiente iteracion
    k_iteracion=k_iteracion+1;
    h_tanque=[h_tanque hk]; %Agrego el nuevo valor al vector que contiene todos los valores de las distintas iteraciones
end
 
%Imprimo pantalla
 
fprintf('La altura del tanque es: %.2f\n',h_tanque(h_iteracion+1));