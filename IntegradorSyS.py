import tkinter
from tkinter import messagebox
from tkinter.constants import BOTTOM, RIGHT, SE, SW

silos = []
silos2 = []
silos3= []

def abrirVentanaGerente():
    ventanaSeleccion.withdraw()
    ventanaGerente = tkinter.Tk()
    ventanaGerente.geometry("800x400")
    ventanaGerente.config(background = "old lace")
    ventanaGerente.title("Copra S.A")

    etiquetaSilo = tkinter.Label(ventanaGerente, text = "Seleccionar Silo:",bg = "old lace", font = ("Consolas", 10))
    etiquetaSilo.grid(row = 0, column = 0)

    varsel = tkinter.StringVar(ventanaGerente)
    varsel.set("Seleccione Nº silo")
    opciones = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
    opcion = tkinter.OptionMenu(ventanaGerente, varsel, *opciones)
    opcion.config(width = 20, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
    opcion.grid(row = 0, column = 1)

    etiquetaBlanca3= tkinter.Label(ventanaGerente, text = "", bg = "old lace", font = ("Consolas", 10))
    etiquetaBlanca3.grid(row = 2, column = 1)

    def ingresoSilo():
        for i in range (4, 30):
            movimiento= tkinter.Label(ventanaGerente, text = "                                             ", bg = "old lace", font = ("Consolas", 10))
            movimiento.grid(row = i, column = 1)
        for i in range (4, 30):
            movimiento= tkinter.Label(ventanaGerente, text = "                                             ", bg = "old lace", font = ("Consolas", 10))
            movimiento.grid(row = i, column = 0)
        numeroSilo = varsel.get()
        silonum = int(numeroSilo) 
        contador = 4
        if silos[silonum] == "Este silo no posee informacion":
            movimiento= tkinter.Label(ventanaGerente, text = "Este silo no posee informacion", bg = "old lace", font = ("Consolas", 10))
            movimiento.grid(row = 5, column = 1)
        else:
            etiquetaSector = tkinter.Label(ventanaGerente, text = "Sector:", bg = "old lace", font = ("Consolas", 10))
            etiquetaSector.grid(row = contador, column = 0)
            etiquetaFecha = tkinter.Label(ventanaGerente, text = "Fecha:", bg = "old lace", font = ("Consolas", 10))
            etiquetaFecha.grid(row = contador+1, column = 0)
            etiquetaToneladas = tkinter.Label(ventanaGerente, text = "Toneladas movidas:", bg = "old lace", font = ("Consolas", 10))
            etiquetaToneladas.grid(row = contador+2, column = 0) 
            for posicion in silos[silonum]:
                movimiento= tkinter.Label(ventanaGerente, text = "                                             ", bg = "old lace", font = ("Consolas", 10))
                movimiento.grid(row = contador, column = 1)
                movimiento= tkinter.Label(ventanaGerente, text = posicion, bg = "old lace", font = ("Consolas", 10))
                movimiento.grid(row = contador, column = 1)
                contador = contador + 1
        if silos2[silonum] == "Este silo no posee informacion":
                b = 1
        else:
            etiquetaBlanca3= tkinter.Label(ventanaGerente, text = "", bg = "old lace", font = ("Consolas", 10))
            etiquetaBlanca3.grid(row = contador, column = 0)
            etiquetaBlanca4= tkinter.Label(ventanaGerente, text = "", bg = "old lace", font = ("Consolas", 10))
            etiquetaBlanca4.grid(row = contador, column = 1)
            etiquetaSector = tkinter.Label(ventanaGerente, text = "Sector:", bg = "old lace", font = ("Consolas", 10))
            etiquetaSector.grid(row = contador+1, column = 0)
            etiquetaFecha = tkinter.Label(ventanaGerente, text = "Fecha:", bg = "old lace", font = ("Consolas", 10))
            etiquetaFecha.grid(row = contador+2, column = 0)
            etiquetaToneladas = tkinter.Label(ventanaGerente, text = "Toneladas movidas:", bg = "old lace", font = ("Consolas", 10))
            etiquetaToneladas.grid(row = contador+3, column = 0) 
            for posicion in silos2[silonum]:
                movimiento= tkinter.Label(ventanaGerente, text = "                                             ", bg = "old lace", font = ("Consolas", 10))
                movimiento.grid(row = contador+1, column = 1)
                movimiento= tkinter.Label(ventanaGerente, text = posicion, bg = "old lace", font = ("Consolas", 10))
                movimiento.grid(row = contador+1, column = 1)
                contador = contador + 1
        if silos3[silonum] == "Este silo no posee informacion":
            b = 1
        else:
            etiquetaSector = tkinter.Label(ventanaGerente, text = "Sector:", bg = "old lace", font = ("Consolas", 10))
            etiquetaSector.grid(row = contador+2, column = 0)
            etiquetaFecha = tkinter.Label(ventanaGerente, text = "Fecha:", bg = "old lace", font = ("Consolas", 10))
            etiquetaFecha.grid(row = contador+3, column = 0)
            etiquetaToneladas = tkinter.Label(ventanaGerente, text = "Toneladas movidas:", bg = "old lace", font = ("Consolas", 10))
            etiquetaToneladas.grid(row = contador+4, column = 0) 
            for posicion in silos3[silonum]:
                movimiento= tkinter.Label(ventanaGerente, text = "                                             ", bg = "old lace", font = ("Consolas", 10))
                movimiento.grid(row = contador+2, column = 1)
                movimiento= tkinter.Label(ventanaGerente, text = posicion, bg = "old lace", font = ("Consolas", 10))
                movimiento.grid(row = contador+2, column = 1)
                contador = contador + 1
    
    def ayuda():
        ventanaGerente.withdraw()
        inicio()
       
    botonIngresoDatos = tkinter.Button(ventanaGerente, width = 24, text = "Ver informacion del silo", command = ingresoSilo, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
    botonIngresoDatos.grid(row = 1, column = 1)

    etiquetaBlanca3 = tkinter.Label(ventanaGerente, text = "", bg = "old lace")
    etiquetaBlanca3.grid(row = 2, column = 1)

    botonIngresoDatos = tkinter.Button(ventanaGerente, text = "Volver al inicio", command = ayuda, font = ("Consolas", 11), bg = "burlywood1", fg = "black")
    botonIngresoDatos.grid(row = 1, column = 2)
    
def abrirVentanaEmpleado():
    ventanaSeleccion.withdraw()
    ventanaEmpleado = tkinter.Tk()
    ventanaEmpleado.geometry("800x400")
    ventanaEmpleado.config(background = "old lace")
    ventanaEmpleado.title("Copra S.A")

    etiquetaSilo = tkinter.Label(ventanaEmpleado, text = "Silo:", bg = "old lace", font = ("Consolas", 10))
    etiquetaSilo.grid(row = 0, column = 0)

    etiquetaArea = tkinter.Label(ventanaEmpleado, text = "Area:", bg = "old lace", font = ("Consolas", 10))
    etiquetaArea.grid(row = 1, column = 0)

    etiquetaFecha = tkinter.Label(ventanaEmpleado, text = "Fecha de la accion(dd/mm/aa):", bg = "old lace", font = ("Consolas", 10))
    etiquetaFecha.grid(row = 2, column = 0)

    etiquetaToneladas = tkinter.Label(ventanaEmpleado, text = "Cantidad de toneladas movidas:", bg = "old lace", font = ("Consolas", 10))
    etiquetaToneladas.grid(row = 3, column = 0)

    var = tkinter.StringVar(ventanaEmpleado)
    var.set("Seleccione Nº silo")
    opciones = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18"]
    opcion = tkinter.OptionMenu(ventanaEmpleado, var, *opciones)
    opcion.config(width = 20, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
    opcion.grid(row = 0, column = 1)

    var2 = tkinter.StringVar(ventanaEmpleado)
    var2.set("Seleccione su area")
    opciones2 = ["Almacenamiento","Carga","Descarga","Secado","Mantenimiento granos"]
    opcion2 = tkinter.OptionMenu(ventanaEmpleado, var2, *opciones2)
    opcion2.config(width = 20, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
    opcion2.grid(row = 1, column = 1)

    cajaFecha = tkinter.Entry(ventanaEmpleado)
    cajaFecha.config(width = 26, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
    cajaFecha.grid(row = 2, column = 1)

    cajaToneladas = tkinter.Entry(ventanaEmpleado)
    cajaToneladas.config(width = 26, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
    cajaToneladas.grid(row = 3, column = 1)

    def accionBotonIngresoDatos():
        sector = []

        numSilo = var.get()
        area = var2.get()
        sector.append(area)
        fecha = cajaFecha.get()
        sector.append(fecha) 
        toneladas = cajaToneladas.get()
        sector.append(toneladas)
        
        if silos[int(numSilo)] == "Este silo no posee informacion":
            silos.insert(int(numSilo), sector)
        elif silos2[int(numSilo)] == "Este silo no posee informacion":
            silos2.insert(int(numSilo), sector)
        else:
            silos3.insert(int(numSilo), sector)

        messagebox.showinfo("Copra S.A", "Creado exitosamente")

    def ayuda():
        ventanaEmpleado.withdraw()
        inicio()

    botonIngresoDatos = tkinter.Button(ventanaEmpleado, text = "Finalizar movimiento - agregar uno nuevo", command = accionBotonIngresoDatos, font = ("Consolas", 11), bg = "burlywood1", fg = "black")
    botonIngresoDatos.grid(row = 5, column = 1)

    etiquetaBlanca3 = tkinter.Label(ventanaEmpleado, text = "", bg = "old lace")
    etiquetaBlanca3.grid(row = 6, column = 1)

    botonIngresoDatos = tkinter.Button(ventanaEmpleado, text = "Volver al inicio", command = ayuda, font = ("Consolas", 11), bg = "burlywood1", fg = "black")
    botonIngresoDatos.grid(row = 7, column = 1)

def inicio():
    ventanaSeleccion.withdraw() 
    ventanaSeleccion.deiconify()

ventanaSeleccion = tkinter.Tk()
ventanaSeleccion.title("Copra S.A")
ventanaSeleccion.geometry("800x400")
ventanaSeleccion.config(background = "old lace")

etiquetaSeleccion = tkinter.Label(ventanaSeleccion, text = "Seleccione su puesto", font = ("Consolas", 20),  bg = "old lace")
etiquetaSeleccion.pack()

etiquetaBlanca1 = tkinter.Label(ventanaSeleccion, text = "", bg = "old lace")
etiquetaBlanca1.pack()

botonGerente = tkinter.Button(ventanaSeleccion, text = "Gerente", width = 15, command = abrirVentanaGerente, font = ("Consolas", 11), bg = "burlywood1", fg = "black")
botonGerente.pack()

etiquetaBlanca2 = tkinter.Label(ventanaSeleccion, text = "", bg = "old lace")
etiquetaBlanca2.pack()

botonEmpleado = tkinter.Button(ventanaSeleccion, text = "Empleado", width = 15, command = abrirVentanaEmpleado, font = ("Consolas", 11), bg = "burlywood1", fg = "black")
botonEmpleado.pack()

# logoCopra = tkinter.PhotoImage(file = "imagenCopra.png")
# etiquetaLogo1 = tkinter.Label(ventanaSeleccion, image = logoCopra, bg = "old lace")
# etiquetaLogo1.pack(side = BOTTOM)

# logoSyS = tkinter.PhotoImage(file = "logoSyS.png")
# etiquetalogoSyS = tkinter.Label(ccion, image = logoSyS, bg = "old lace")
# etiquetalogoSyS.pack(side = BOTTOM)

for i in range(0,19):
        silos.insert(i, "Este silo no posee informacion")
for i in range(0,19):
        silos2.insert(i, "Este silo no posee informacion")
for i in range(0,19):
        silos3.insert(i, "Este silo no posee informacion")
        
inicio()
ventanaSeleccion.mainloop()