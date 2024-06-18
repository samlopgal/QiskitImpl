from qiskit import *
from qiskit.circuit.library import *
from qiskit.circuit import *
import math

def randomBit(n):

    if(n > 0):
        q=QuantumRegister(1)
        c=ClassicalRegister(1)
        qc=QuantumCircuit(q,c)
        qc.h(q)
        qc.measure(q,c)

        backend=Aer.get_backend("qasm_simulator")
        qjob=execute(qc,backend,shots=n, memory=True)
        list = qjob.result().get_memory();
        #qc.draw('latex', filename='../imagenRANDOM.png', cregbundle=False, plot_barriers=False, initial_state=True)
    else:
        print("Introduzca un número de bits válido.")
    return list

def getNumeroAleatorio(min, max):

    bitString = ""

    delta = max-min
    n = math.floor(math.log(delta,2))+1
    numero = delta + 1

    while(numero > delta):
        #Obtenemos los resultados del circuito y les damos el formato adecuado
        bitString=""
        bits = randomBit(n)
        #print(bits)
        for i in bits:
            bitString = bitString + i
        numero = int(bitString,2)
        #---------------------------------------
    numero += min
    return numero