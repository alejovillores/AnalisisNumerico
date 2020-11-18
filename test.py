import numpy as np

def fuerza_bruta(n_random):
    encontrado  = False
    iteraciones = 0
    
    while encontrado != True:
        if iteraciones == n_random:
            encontrado = True
        else:
            iteraciones += 1
    
    return iteraciones


def posicion_del_numero(n_iteraciones):
    
    # Divido el numero por 10 para acotar el rango
    # Lo paso a string para tener control de la posicion     
    n_iteraciones = str(n_iteraciones/10)
    
    # Busco la posicion de la coma
    posicion_coma = n_iteraciones.index(".")
    
    # Devuelvo el numero sin la coma que representa la pos
    return n_iteraciones[:posicion_coma]

# hist = [0-10,10-20,20-30,30-14,...]



def test01AlgoritmoFuerzaBruta():
    iteraciones = fuerza_bruta(765)
    print("Numero de iteraciones: " + str(iteraciones))

def test02AlgoritmoFuerzaBruta():
    iteraciones = fuerza_bruta(1000)
    print("Numero de iteraciones: " + str(iteraciones))    
    
def test03AlgoritmoFuerzaBrutaConPoscion():
    iteraciones = fuerza_bruta(765)
    pos = posicion_del_numero(iteraciones)
    
    print("Numero de iteraciones: " + str(iteraciones))
    print("Posicion en lista : " + pos)

def test04AlgoritmoFuerzaBrutaConPoscion():
    iteraciones = fuerza_bruta(9901)
    pos = posicion_del_numero(iteraciones)
    
    print("Numero de iteraciones: " + str(iteraciones))
    print("Posicion en lista : " + pos)
def creacionListaNumpy():
    
    histograma = np.zeros((5), dtype=int)
    print(histograma)

def test05AlgoritmoFuerzaBrutaConPoscionYagregoaLista():
    iteraciones = fuerza_bruta(9901)
    pos = posicion_del_numero(iteraciones)
    histograma = np.zeros((1000), dtype=int)
    histograma[int(pos)] +=1
    
    print("Numero de iteraciones: " + str(iteraciones))
    print("Posicion en lista : " + pos)
    print(histograma[int(pos)])

def test6AlgoritmoFuerzaBrutaConPoscionYagregoaLista():
    iteraciones = fuerza_bruta(9901)
    pos = posicion_del_numero(iteraciones)
    histograma = np.zeros((1000), dtype=int)
    histograma[int(pos)] +=1
    
    iteraciones = fuerza_bruta(9905)
    pos = posicion_del_numero(iteraciones)
    histograma[int(pos)] +=1
    
    
    iteraciones = fuerza_bruta(9903)
    pos = posicion_del_numero(iteraciones)
    histograma[int(pos)] +=1
    
    print("Numero de iteraciones: " + str(iteraciones))
    print("Posicion en lista : " + pos)
    print(histograma[int(pos)])
    
    
    
    
'''test01AlgoritmoFuerzaBruta()
test02AlgoritmoFuerzaBruta()
test03AlgoritmoFuerzaBrutaConPoscion()
test04AlgoritmoFuerzaBrutaConPoscion()
creacionListaNumpy()
test05AlgoritmoFuerzaBrutaConPoscionYagregoaLista()'''
test6AlgoritmoFuerzaBrutaConPoscionYagregoaLista()