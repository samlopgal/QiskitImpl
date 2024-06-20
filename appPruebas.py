import tkinter
from tkinter import ttk, Label, Entry, scrolledtext, Button
from protocolos import *
import matplotlib.pyplot as plt

def escribeTexto(text, texto):
    text.configure(state="normal")
    text.insert(tkinter.INSERT, texto)
    text.configure(state="disabled")
    
def borrarTexto(text):
    text.configure(state="normal")
    text.delete('1.0', tkinter.END)
    text.configure(state="disabled")
    
def DeteccionVariandoN():
    n = e7.get()
    repeticiones = e8.get()
    
    n = n.strip()
    repeticiones = repeticiones.strip()
    
    if(n.isdigit() == False or int(n) < 4):
        borrarTexto(txt)
        escribeTexto(txt, "El valor del número de bits debe ser numérico y mayor o igual que 4")
    else:
        if(repeticiones.isdigit() == False or (int(repeticiones) <= 0)):
            borrarTexto(txt)
            escribeTexto(txt, "El valor de 'Repeticiones' debe ser numérico y mayor que 0")
        else:
            n= int(n)
            repeticiones = int(repeticiones)
            listaN = []
            listaDetecciones = []
            listaProbabilidad = []
            
            for i in range(0,7):
                listaN.append(n * 2**i)
            
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

def pruebaDeteccionIntruso():
    n = e5.get()
    repeticiones = e6.get()
    
    n = n.strip()
    repeticiones = repeticiones.strip()
    
    if(n.isdigit() == False or int(n) <= 0):
        borrarTexto(txt)
        escribeTexto(txt, "El valor del número de bits debe ser numérico y mayor que 0")
    else:
        if(repeticiones.isdigit() == False or (int(repeticiones) <= 0)):
            borrarTexto(txt)
            escribeTexto(txt, "El valor de 'Repeticiones' debe ser numérico y mayor que 0")
        else:
            dict = {}
            dict['True'] = 0
            dict['False'] = 0
            n = int(n)
            repeticiones = int(repeticiones)
            
            for i in range(repeticiones):
                result = bb84(n, 1)
                if(result[12] == True):
                    dict['True'] += 1
                else:    
                    dict['False'] += 1
            
            mens = str(dict)
            borrarTexto(txt)
            escribeTexto(txt, mens)

def pruebaBB84():
    
    n = e1.get()
    intruso = e2.get()
    
    n = n.strip()
    intruso = intruso.strip()
    
    if(n.isdigit() == False or int(n) <= 0):
        borrarTexto(txt)
        escribeTexto(txt, "El valor del número de bits debe ser numérico y mayor que 0")
    else: 
        if(intruso.isdigit() == False or (int(intruso) != 0 and int(intruso) != 1)):
            borrarTexto(txt)
            escribeTexto(txt, "El valor de 'Intruso' debe ser 0 (sin intruso) o 1 (con intruso)")
        else:
            intruso = int(intruso)
            n = int(n)
            result = bb84(n, intruso)
            if(intruso == 0):
                borrarTexto(txt)
                mens = str(result[0])+ " / Bits de Alice\n" + str(result[1])+ " / Bases de Alice\n" + str(result[2])+ " / Bases de Bob\n"+str(result[3])+ " / Lecturas de Bob\n\n" + str(result[4]) +" / Comparaciones de bases\n\n" + str(result[5]) + " / Key de Alice provisional\n" +str(result[6]) + " / Key de Bob provisional\n" + str(result[7])+ "/ Posiciones de los bits compartidos\n" +str(result[8])+ "/ Key definitiva de Alice\n" +  str(result[9])+ "/ Key definitiva de Bob\n" + "Intruso detectado: " + str(result[10])  
                escribeTexto(txt, mens)
            else:
                borrarTexto(txt)
                mens = str(result[0])+ " / Bits de Alice\n" + str(result[1])+ " / Bases de Alice\n" +str(result[2])+ " / Bases de Eva\n"+str(result[3])+ " / Lecturas de Eva\n" + str(result[4])+ " / Bases de Bob\n"+str(result[5])+ " / Lecturas de Bob\n\n" + str(result[6]) +" / Comparaciones de bases\n\n" + str(result[7]) + " / Key de Alice provisional\n" +str(result[8]) + " / Key de Bob provisional\n" + str(result[9])+ " / Posiciones de los bits compartidos\n" +str(result[10])+ " / Key definitiva de Alice\n" +  str(result[11])+ " / Key definitiva de Bob\n" + "Intruso detectado: " + str(result[12])  
                escribeTexto(txt, mens)
                
def pruebaLanzamiento():
    
    n = e3.get()
    aliceMiente = e4.get()
        
    n = n.strip()
    aliceMiente = aliceMiente.strip()
        
    if(n.isdigit() == False or int(n) <= 0):
        borrarTexto(txt)
        escribeTexto(txt, "El valor del número de bits debe ser numérico y mayor que 0")
    else: 
        if(aliceMiente.isdigit() == False or (int(aliceMiente) != 0 and int(aliceMiente) != 1)):
            borrarTexto(txt)
            escribeTexto(txt, "El valor de 'Alice miente' debe ser 0 (no miente) o 1 (miente)")
        else:
            aliceMiente = int(aliceMiente)
            n = int(n)
            result = lanzamientoDeMoneda(n,aliceMiente)

            borrarTexto(txt)
            mens = str(result[0])+ " / Bits de Alice\n" + str(result[1])+ " / Base de Alice\n" + str(result[2])+ " / Bases de Bob\n"+str(result[3])+ " / Lecturas de Bob\n" + str(result[4]) +" / Tabla rectilínea (índices de los bits)\n" + str(result[5]) + " / Tabla diagonal (índices de los bits) \n" + "/ Elección de Bob: "+str(result[6])  +"\n" + "/ Respuesta de Alice: "+ str(result[7]) +"\n" +str(result[8])+ " / Bits enviados por Alice\n" +  "/ Comprobación por Bob (¿Mintió Alice?): " +str(result[9]) 
            escribeTexto(txt, mens)

if __name__ == '__main__':
    master = tkinter.Tk()
    master.title("Pruebas")
    
    notebook = ttk.Notebook(master)
    notebook.pack(fill='both', expand='yes')
    frame1 = ttk.Frame(notebook)
    frame2 = ttk.Frame(notebook)
    frame3 = ttk.Frame(notebook)
    frame4 = ttk.Frame(notebook)
   
    #Preparamos Frame 1
    notebook.add(frame1, text='BB84')
    labelN = Label(frame1, text="Bits transmitidos:",font=('Arial', 10))
    labelIntruso = Label(frame1, text="Intruso:",font=('Arial', 10))
    e1 = Entry(frame1)
    e2 = Entry(frame1)
    txt = scrolledtext.ScrolledText(master, undo=True)
    txt['font'] = ('consolas', '14')
    txt.pack(expand=True, fill='both')
    txt.config(foreground='white', background='black')
    
    B = Button(frame1, text ="Ejecutar", command=pruebaBB84)
    
    #Preparamos Frame 2
    notebook.add(frame2, text='CoinTossing')
    labelN2 = Label(frame2, text="Bits transmitidos:",font=('Arial', 10))
    labelIntruso2 = Label(frame2, text="Alice miente:",font=('Arial', 10))
    e3 = Entry(frame2)
    e4 = Entry(frame2)
    B2 = Button(frame2, text ="Ejecutar", command=pruebaLanzamiento)
    
    #Preparamos Frame 3
    notebook.add(frame3, text='Prueba detección')
    labelN3 = Label(frame3, text="Bits transmitidos:",font=('Arial', 10))
    labelRepeticiones= Label(frame3, text="Repeticiones:", font=('Arial', 10))
    e5 = Entry(frame3)
    e6 = Entry(frame3)
    
    B3 = Button(frame3, text ="Ejecutar", command=pruebaDeteccionIntruso)
    
    #Preparamos Frame 4
    notebook.add(frame4, text='Gráfica detecciones')
    labelN4 = Label(frame4, text="N inicial:", font=('Arial', 10))
    labelRepeticiones2= Label(frame4, text="Repeticiones:", font=('Arial', 10))
    labelRepeticiones3= Label(frame4, text="Se recomienda (N = 4 y Repeticiones <= 300)", font=('Arial', 10))
    e7 = Entry(frame4)
    e8 = Entry(frame4)
    
    B4 = Button(frame4, text ="Ejecutar", command=DeteccionVariandoN)
    ##########
    master.geometry('800x600')
    labelN.grid(row=0, column=0, sticky="nsew")
    labelIntruso.grid(row=1, column=0, sticky="nsew")
    e1.grid(row=0, column=1, sticky="nsew")
    e2.grid(row=1, column=1, sticky="nsew")
    B.grid(row=2, column=2, sticky="nsew")
    #txt.grid(column = 0, row = 4, columnspan =11, sticky = tkinter.W+tkinter.E)
    
    labelN2.grid(row=0, column=0, sticky="nsew")
    labelIntruso2.grid(row=1, column=0, sticky="nsew")
    e3.grid(row=0, column=1, sticky="nsew")
    e4.grid(row=1, column=1, sticky="nsew")
    B2.grid(row=2, column=2, sticky="nsew")
    
    labelN3.grid(row=0, column=0, sticky="nsew")
    labelRepeticiones.grid(row=1, column=0, sticky="nsew")
    e5.grid(row=0, column=1, sticky="nsew")
    e6.grid(row=1, column=1, sticky="nsew")
    B3.grid(row=2, column=2, sticky="nsew")
    
    labelN4.grid(row=0, column=0, sticky="nsew")
    labelRepeticiones2.grid(row=1, column=0, sticky="nsew")
    labelRepeticiones3.grid(row=0, column=6, columnspan = 5,sticky="nsew")
    e7.grid(row=0, column=1, sticky="nsew")
    e8.grid(row=1, column=1, sticky="nsew")
    B4.grid(row=2, column=2, sticky="nsew")
    
    filas = 2
    columnas = 2
    for i in range(columnas):
        master.grid_columnconfigure(i, weight=1)
    for i in range(filas):
        master.grid_rowconfigure(i, weight=1)
    master.mainloop()
    
    
    pass

