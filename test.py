from colorama import Fore , Back
import matplotlib.pyplot as plt
from aleatoriedad import *
from protocolos import *

def testRandomBits(n):
    print( Fore.LIGHTBLUE_EX + Back.RESET +"-------------- Test de la función que genera n bits aleatorios --------------")
    for i in range(4):
        lista = randomBit(n)
        print(Fore.GREEN + Back.RESET + str(lista))
    print( Fore.LIGHTBLUE_EX + Back.RESET  +"-------------------------------------------------------")
    
def testProbabilidadDeteccionIntruso(n, repeticiones):
    print(Fore.GREEN + Back.RESET+"-------------- Test de la función que contabiliza las detecciones de intruso --------------")
    dict = {}
    dict['True'] = 0
    dict['False'] = 0
        
    for i in range(repeticiones):
        result = bb84(n, 1)
        if(result[12] == True):
            dict['True'] += 1        
        else:    
            dict['False'] += 1
    
    print(Fore.LIGHTBLUE_EX + Back.RESET+ str(dict))
    print(Fore.GREEN + Back.RESET+ "-------------------------------------------------------")
    
    
def testProbabilidadDeteccionVariandoN(nInicial, repeticiones):
    
    ''' La duración de esta prueba se demostró excesiva. Si se quiere reducir su duración,
     se recomienda comentar la generación cuántica de números aleatorios y descomentar la línea que usa la librería random
     en la función bb84'''
    
    listaN = []
    listaDetecciones = []
    listaProbabilidad = []
    
    for i in range(0,7):
        listaN.append(nInicial * 2**i)
    
    for i in listaN:
        acum = 0
        for j in range(0,repeticiones): 
            result = bb84(i, 1)
            if(result[12] == True):
                acum += 1
        listaDetecciones.append(acum)    
    
    for i in listaN:
        valor = (1 - (0.75)**(i/4)) * repeticiones
        listaProbabilidad.append(valor)
    
    fig, ax = plt.subplots()
    ax.plot(listaN, listaDetecciones, label="Implementación")
    ax.plot(listaN, listaProbabilidad, '-.',label="Cálculo teórico")
    ax.set_xlabel("Bits transmitidos", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel("Detecciones de intruso / "+ str(repeticiones) + " transmisiones", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_yticks(range(0, repeticiones+1, 10))
    plt.legend()
    plt.savefig('diagramaLineas.png')
    
    
def testBB84(n, intruso):
    print(Fore.GREEN + Back.RESET+"---------------------- Test BB84 ----------------------")
    
    result = bb84(n, intruso)
    print(Fore.GREEN + Back.RESET+str(result[0]) + Fore.LIGHTBLUE_EX + Back.RESET + " / Bits a enviar por Alice " )
    print(Fore.GREEN + Back.RESET+ str(result[1]) +Fore.LIGHTBLUE_EX + Back.RESET+ " / Bases de Alice " )
    if(intruso == 1):
        print(Fore.GREEN + Back.RESET+str(result[2]) + Fore.LIGHTBLUE_EX + Back.RESET+ " / Bases de Eva ")
        print(Fore.GREEN + Back.RESET+str(result[3]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Lecturas de Eva ")
        print(Fore.GREEN + Back.RESET+str(result[4]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Bases de Bob ")
        print(Fore.GREEN + Back.RESET+str(result[5]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Lecturas de Bob \n")
        print(Fore.GREEN + Back.RESET+str(result[6]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Lista de comparaciones de bases \n")
        print(Fore.GREEN + Back.RESET+str(result[7]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Key Alice ")
        print(Fore.GREEN + Back.RESET+str(result[8]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Key Bob ")
        print(Fore.GREEN + Back.RESET+str(result[9]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Posiciones de los bits compartidos ")
        print(Fore.GREEN + Back.RESET+str(result[10]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Key definitiva Alice ")
        print(Fore.GREEN + Back.RESET+str(result[11]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Key definitiva Bob ")
        print(Fore.LIGHTBLUE_EX + Back.RESET+"Intruso detectado: " + Fore.GREEN + Back.RESET+ str(result[12]))
    else:
        print( Fore.GREEN + Back.RESET+str(result[2]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Bases de Bob ")
        print( Fore.GREEN + Back.RESET+str(result[3]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Lecturas de Bob \n")
        print(Fore.GREEN + Back.RESET+str(result[4]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Lista de comparaciones de bases \n")
        print(Fore.GREEN + Back.RESET+str(result[5]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Key Alice ")
        print(Fore.GREEN + Back.RESET+str(result[6]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Key Bob ")
        print(Fore.GREEN + Back.RESET+str(result[7]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Posiciones de los bits compartidos ")
        print(Fore.GREEN + Back.RESET+str(result[8]) + Fore.LIGHTBLUE_EX + Back.RESET + " / Key definitiva Alice ")
        print(Fore.GREEN + Back.RESET+str(result[9]) + Fore.LIGHTBLUE_EX + Back.RESET+" / Key definitiva Bob ")
        print(Fore.LIGHTBLUE_EX + Back.RESET+"Intruso detectado: " + Fore.GREEN + Back.RESET + str(result[10]))
    print(Fore.GREEN + Back.RESET+"-------------------------------------------------------")
    
def testLanzMoneda(n, AliceMiente):
    print(Fore.GREEN + Back.RESET+"---------------------- Test lanzamiento de moneda ----------------------")
        
    result = lanzamientoDeMoneda(n, AliceMiente)
    print( Fore.LIGHTBLUE_EX + Back.RESET + "/ Bits a enviar por Alice: " + Fore.GREEN + Back.RESET+str(result[0]))
    print( Fore.LIGHTBLUE_EX + Back.RESET+ "/ Base de Alice: " + Fore.GREEN + Back.RESET+ str(result[1]) )
    print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Bases de Bob: " + Fore.GREEN + Back.RESET+str(result[2]))
    print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Lecturas de Bob: " + Fore.GREEN + Back.RESET+str(result[3]))
    print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Tabla rectilínea (índices de los bits): " + Fore.GREEN + Back.RESET+str(result[4]))
    print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Tabla diagonal (índices de los bits): " + Fore.GREEN + Back.RESET+str(result[5]))
    print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Elección de Bob: " + Fore.GREEN + Back.RESET+str(result[6]))
    print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Respuesta de Alice: " + Fore.GREEN + Back.RESET+str(result[7]))
    print(Fore.LIGHTBLUE_EX + Back.RESET + "/ Bits enviados por Alice: " + Fore.GREEN + Back.RESET+str(result[8]))
    print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Comprobación por Bob (¿Mintió Alice?): " + Fore.GREEN + Back.RESET+str(result[9]))
    print(Fore.GREEN + Back.RESET+"-------------------------------------------------------")

if __name__ == '__main__':
  #testRandomBits(8)
  testBB84(8, 1)
  #testProbabilidadDeteccionIntruso(32, 500)
  #testLanzMoneda(8, 1)
  #testProbabilidadDeteccionVariandoN(4, 200)
pass