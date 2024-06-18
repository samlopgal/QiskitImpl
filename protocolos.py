from aleatoriedad import *
import random

def lanzamientoDeMoneda(n, AliceMiente):
    
    basesBob = []     
    lecturasBob = []
    bitsAlice = []
    tablaRectilinea = []
    tablaDiagonal = []
    baseAlice = getNumeroAleatorio(0, 1)
    result = []
    
    #---------------  Implementación del circuito cuántico de transmisión
    
    a=ClassicalRegister(1, "Alice")
    b=ClassicalRegister(2, "Bob")
        
    q=QuantumRegister(2)   
    qc=QuantumCircuit(q,b,a)
      
    qc.h(q[0])
    qc.measure(q[0],a[0]) #Bit aleatorio de Alice
        
    if baseAlice == 1:
        qc.h(q[0]) #Aplicación de la base de Alice
    
    qc.h(q[1])  
    qc.measure(q[1],b[0]) #Base aleatoria de Bob 
        
    qc.append(HGate(), [q[0]]).c_if(b[0],1) #Aplicación de la base de Bob
    qc.measure(q[0],b[1]) #Bit medido por Bob
                
    backend=Aer.get_backend("qasm_simulator")
    qjob=execute(qc,backend,shots=n, memory=True)
    
    #-----------------------------------------
    #--------------------------------  Extraccion de los datos del circuito
    
    # (Este paso es propio del funcionamiento de la librería y no del protocolo implementado)
    
    for i in str(qjob.result().get_memory()).replace('[', '').replace(']', '').replace(' ','').split(','):
        bitsAlice.append(i[1])
        basesBob.append(i[3])
        lecturasBob.append(i[2])
    
    #qc.draw('latex', filename='../CoinTossing2.png',cregbundle=False, reverse_bits=True, plot_barriers=False, initial_state=True)
    
    #-----------------------------------------
    #---------------------- Bob crea las tablas y decide que base cree que utilizó Alice
    #Estas tablas tendrán los índices de los bits de la lista de bits de Alice que las forman
    for i in range(len(lecturasBob)):
        if(int(basesBob[i]) == 0):
            tablaRectilinea.append(i)
        else:    
            tablaDiagonal.append(i)
    
    eleccionBob = getNumeroAleatorio(0, 1)
    #-----------------------------------------
    #---------------------- Alice comprueba si Bob acertó 
    aciertaBob = eleccionBob == baseAlice
    #-----------------------------------------
    #---------------------- Alice notifica a Bob y envía sus bits
    
    if AliceMiente == 1 and aciertaBob:
        mensaje = "Has perdido"
        bitsEnviadosAlice = randomBit(len(bitsAlice))
    else:    
        mensaje = "Has ganado"
        bitsEnviadosAlice = bitsAlice.copy()
    #----------------------------------------
    #Bob comprueba el resultado
    aliceMintio = False
    if(baseAlice) == 0:
        for i in tablaRectilinea:
            if lecturasBob[i] != bitsEnviadosAlice[i]:
                aliceMintio = True
                break;    
    else:
        for i in tablaDiagonal:
            if lecturasBob[i] != bitsEnviadosAlice[i]:
                aliceMintio = True
                break;    
    #----------------------------------------
    result.append(bitsAlice)
    result.append(baseAlice)
    result.append(basesBob)
    result.append(lecturasBob)
    result.append(tablaRectilinea)
    result.append(tablaDiagonal)
    result.append(eleccionBob)
    result.append(mensaje)
    result.append(bitsEnviadosAlice)
    result.append(aliceMintio)
    
    return result
    
def bb84(n, intruso):
       
    bitsA = []
    basesAlice = []
    basesBob = []     
    lecturasBob = []
    listaComparacionesBases = []
    keyAlice = []
    keyBob = []
    listaIndicesBitsComparar= []
    result = []
    
    if(intruso == 1):
        basesEva = []
        listEva = []
 
    #--------------------------------  Implementación del circuito cuántico
    a=ClassicalRegister(2, "Alice")
    b=ClassicalRegister(2, "Bob")
        
    if(intruso == 1):    # Si hay intruso necesitamos mas registros
        q=QuantumRegister(4)
        e=ClassicalRegister(2, "Eva")
        qc=QuantumCircuit(q,b,e,a)
    else:   # Si no hay intruso necesitamos menos registros
        q=QuantumRegister(3)   
        qc=QuantumCircuit(q,b,a)
      
    qc.h(q[0])
    qc.measure(q[0],a[1]) #Bit aleatorio de Alice
    qc.h(q[1])
    qc.measure(q[1],a[0]) #Base aleatoria de Alice
    qc.append(HGate(), [q[0]]).c_if(a[0],1) #Aplicación de la base de Alice

    if intruso == 1:
        qc.h(q[3])
        qc.measure(q[3],e[0]) #Base aleatoria de Eva
        qc.append(HGate(), [q[0]]).c_if(e[0],1) #Aplicación de la base de Eva
        
        qc.measure(q[0],e[1]) #Bit medido por Eva
    qc.h(q[2])  
    qc.measure(q[2],b[0]) #Base aleatoria de Bob 
    
    qc.append(HGate(), [q[0]]).c_if(b[0],1) #Aplicación de la base de Bob
    qc.measure(q[0],b[1]) #Bit medido por Bob
            
    backend=Aer.get_backend("qasm_simulator")
    qjob=execute(qc,backend,shots=n, memory=True)
    
    #-----------------------------------------
    
    #--------------------------------  Extraccion de los datos del circuito
    
    # (Este paso es propio del funcionamiento de la librería y no del protocolo implementado)
    
    if(intruso == 1):
        for i in str(qjob.result().get_memory()).replace('[', '').replace(']', '').replace(' ','').split(','):
            basesAlice.append(i[6])
            bitsA.append(i[5])
            basesEva.append(i[4])
            listEva.append(i[3])
            basesBob.append(i[2])
            lecturasBob.append(i[1])
    else:
        for i in str(qjob.result().get_memory()).replace('[', '').replace(']', '').replace(' ','').split(','):
            basesAlice.append(i[4])
            bitsA.append(i[3])
            basesBob.append(i[2])
            lecturasBob.append(i[1])
    #-----------------------------------------
    
    #--------------------------------  Comparación de las bases usadas por Alice y Bob
    for i in range(0,len(basesAlice)):
        if(basesAlice[i] == basesBob[i]):
            listaComparacionesBases.append(True)
        else:
            listaComparacionesBases.append(False)
    #-----------------------------------------
    
    #--------------------------------  Bob y Alice descartan los bits de la clave leídos incorrectamente por Bob
    for i in range(0,len(listaComparacionesBases)):
        if(listaComparacionesBases[i] == True):
            keyAlice.append(bitsA[i])
            keyBob.append(lecturasBob[i])
    
    
    #-----------------------------------------
    #--------------------------------  Bob y Alice comparan la mitad de sus claves para detectar a un intruso
    
    listaIndicesPosibles = list(range(0, len(keyAlice)))
    hayIntruso = False
    keyDefinitivaAlice = keyAlice.copy()
    keyDefinitivaBob = keyBob.copy()
    
    for i in range(0,round((len(keyAlice)/2))):
        
        #Implementación cuántica de la elección aleatoria de los bits
        #indice = listaIndicesPosibles[getNumeroAleatorio(0, len(listaIndicesPosibles)-1)]
        
        #Implementación clásica de la elección aleatoria de los bits
        indice = random.choice(listaIndicesPosibles)
        
        listaIndicesBitsComparar.append(indice)
        listaIndicesPosibles.remove(indice)
        #

    listaIndicesBitsComparar.sort(reverse=True)
    
    for i in listaIndicesBitsComparar:
        if(keyAlice[i] != keyBob[i]):
            hayIntruso = True
        keyDefinitivaAlice.pop(i)
        keyDefinitivaBob.pop(i)
        
    #-----------------------------------------
    #qc.draw('latex', filename='../BB84ConIntruso.png',cregbundle=False, reverse_bits=True, plot_barriers=False, initial_state=True)
    
    result.append(bitsA)
    result.append(basesAlice)
    if intruso == 1:
        result.append(basesEva)
        result.append(listEva)
    result.append(basesBob)
    result.append(lecturasBob)
    result.append(listaComparacionesBases)
    result.append(keyAlice)
    result.append(keyBob)
    result.append(listaIndicesBitsComparar)
    result.append(keyDefinitivaAlice)
    result.append(keyDefinitivaBob)
    result.append(hayIntruso)
    return result