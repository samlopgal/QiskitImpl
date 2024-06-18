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
    dict['False (Intruso obtuvo los mismos bits, es indetectable)'] = 0
        
    for i in range(repeticiones):
        result = bb84(n, 1)
        if(result[12] == True):
            dict['True'] += 1
        else:
            if str(result[0]) == str(result[3]): #Comparamos los bits de Alice y Eva
                dict['False (Intruso obtuvo los mismos bits, es indetectable)'] += 1
            else:    
                dict['False'] += 1
    
    print(Fore.LIGHTBLUE_EX + Back.RESET+ str(dict))
    print(Fore.GREEN + Back.RESET+ "-------------------------------------------------------")
    
    
def testProbabilidadDeteccionVariandoN(nInicial, repeticiones):
    
    ''' La duración de esta prueba se demostró excesiva. Si se quiere reducir su duración,
     se recomienda comentar la generación cuántica de números aleatorios y descomentar a línea que usa la librería random
     en la función bb84 (línea de código 255 aproximadamente)'''
    
    listaN = []
    listaDetecciones = []
    
    for i in range(0,7):
        listaN.append(nInicial * 2**i)
    
    for i in listaN:
        acum = 0
        for j in range(0,repeticiones): 
            result = bb84(i, 1)
            if(result[12] == True):
                acum += 1
        listaDetecciones.append(acum)    
    
    fig, ax = plt.subplots()
    ax.plot(listaN, listaDetecciones)
    ax.set_xlabel("Bits transmitidos", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_ylabel("Detecciones de intruso / 200 transmisiones", fontdict = {'fontsize':10, 'fontweight':'bold', 'color':'tab:blue'})
    ax.set_yticks(range(0, 201, 10))
    
    plt.savefig('diagramaLineas.png')
    
    
def testBB84(n, intruso):
    print(Fore.GREEN + Back.RESET+"---------------------- Test BB84 ----------------------")
    
    result = bb84(n, intruso)
    print( Fore.LIGHTBLUE_EX + Back.RESET + "/ Bits a enviar por Alice: " + Fore.GREEN + Back.RESET+str(result[0]))
    print( Fore.LIGHTBLUE_EX + Back.RESET+ "/ Bases de Alice: " + Fore.GREEN + Back.RESET+ str(result[1]) )
    if(intruso == 1):
        print(Fore.LIGHTBLUE_EX + Back.RESET+ "/ Bases de Eva: " +Fore.GREEN + Back.RESET+str(result[2]) )
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Lecturas de Eva: " + Fore.GREEN + Back.RESET+str(result[3]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Bases de Bob: " + Fore.GREEN + Back.RESET+str(result[4]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Lecturas de Bob: " + Fore.GREEN + Back.RESET+str(result[5]) )
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Lista de comparaciones de bases: " + Fore.GREEN + Back.RESET+str(result[6]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Key Alice: "+ Fore.GREEN + Back.RESET+str(result[7]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Key Bob: " + Fore.GREEN + Back.RESET+str(result[8]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Posiciones de los bits compartidos: " + Fore.GREEN + Back.RESET+str(result[9]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Key definitiva Alice: " + Fore.GREEN + Back.RESET+str(result[10]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Key definitiva Bob: " +Fore.GREEN + Back.RESET+str(result[11]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"Intruso detectado: " + Fore.GREEN + Back.RESET+ str(result[12]))
    else:
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Bases de Bob: " + Fore.GREEN + Back.RESET+str(result[2]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Lecturas de Bob: " + Fore.GREEN + Back.RESET+str(result[3]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Lista de comparaciones de bases: " + Fore.GREEN + Back.RESET+str(result[4]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Key Alice: " + Fore.GREEN + Back.RESET+str(result[5]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Key Bob: " + Fore.GREEN + Back.RESET+str(result[6]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Posiciones de los bits compartidos: " + Fore.GREEN + Back.RESET+str(result[7]))
        print(Fore.LIGHTBLUE_EX + Back.RESET + "/ Key definitiva Alice: " + Fore.GREEN + Back.RESET+str(result[8]))
        print(Fore.LIGHTBLUE_EX + Back.RESET+"/ Key definitiva Bob: " + Fore.GREEN + Back.RESET+str(result[9]))
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
  #testBB84(16, 1)
  #testProbabilidadDeteccionIntruso(8, 500)
  #testLanzMoneda(16, 1)
  testProbabilidadDeteccionVariandoN(4, 200)
pass