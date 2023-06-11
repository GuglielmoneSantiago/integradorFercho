import tkinter
from tkinter import messagebox
from tkinter.constants import BOTTOM, RIGHT, SE, SW

datos=[["sa","sa"]]

def menu():
    def asistencia():
        ventanaMenu.withdraw()
        ventanaAsistencia = tkinter.Tk()
        ventanaAsistencia.title("Empresa")
        ventanaAsistencia.geometry("800x400")
        ventanaAsistencia.config(background = "old lace")

        etiquetaSeleccion2 = tkinter.Label(ventanaAsistencia , text = "Asistencia al cliente", font = ("Consolas", 20),  bg = "old lace")
        etiquetaSeleccion2.pack()

        etiquetaSeleccion2 = tkinter.Label(ventanaAsistencia , text = "Correo: Guglielmonesantiago@gmail.com", font = ("Consolas", 20),  bg = "old lace")
        etiquetaSeleccion2.place(x=150,y=150)

        etiquetaSeleccion2 = tkinter.Label(ventanaAsistencia , text = "Numero: 37914508394", font = ("Consolas", 20),  bg = "old lace")
        etiquetaSeleccion2.place(x=250,y=200)
        
    ventanaInicio.withdraw()
    ventanaMenu= tkinter.Tk()
    ventanaMenu.title("Empresa")
    ventanaMenu.geometry("800x400")
    ventanaMenu.config(background = "old lace")

    etiquetaSeleccion2 = tkinter.Label(ventanaMenu , text = "Menu", font = ("Consolas", 20),  bg = "old lace")
    etiquetaSeleccion2.pack()

    botonAsistencia=tkinter.Button(ventanaMenu, text = "Asistencia", font = ("Consolas", 15),command= asistencia, bg = "burlywood1", fg = "black")
    botonAsistencia.place(x=650,y=350)  
   

def registro():
    ventanaInicio.withdraw()
    ventanaRegistro = tkinter.Tk()
    ventanaRegistro.title("Empresa")
    ventanaRegistro.geometry("800x400")
    ventanaRegistro.config(background = "old lace")

    etiquetaSeleccion2 = tkinter.Label(ventanaRegistro , text = "Registro", font = ("Consolas", 20),  bg = "old lace")
    etiquetaSeleccion2.pack()

    etiquetaBlanca12 = tkinter.Label(ventanaRegistro , text = "", bg = "old lace")
    etiquetaBlanca12.pack()

    etiquetaNombre2 = tkinter.Label(ventanaRegistro , text = "Nombre: ", bg = "old lace",font = ("Consolas", 15))
    etiquetaNombre2.pack()

    cajaNombre2 = tkinter.Entry(ventanaRegistro)
    cajaNombre2.config(width = 26, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
    cajaNombre2.pack()

    etiquetaContrasena2 = tkinter.Label(ventanaRegistro , text = "Contraseña: ", bg = "old lace",font = ("Consolas", 15))
    etiquetaContrasena2.pack()
    cajaContrasena2 = tkinter.Entry(ventanaRegistro)
    cajaContrasena2.config(width = 26, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
    cajaContrasena2.pack()

    def accionBotonIngresoDatos():
        contrasena = cajaContrasena2.get()
        nombre = cajaNombre2.get()
        datos.append([nombre,contrasena])
        ventanaRegistro.withdraw()
        ventanaInicio.deiconify()
    botonIngresoDatos = tkinter.Button(ventanaRegistro, text = "Finalizar", command = accionBotonIngresoDatos, font = ("Consolas", 11), bg = "burlywood1", fg = "black")
    botonIngresoDatos.pack()

    

ventanaInicio = tkinter.Tk()
ventanaInicio.title("Copra S.A")
ventanaInicio.geometry("800x400")
ventanaInicio.config(background = "old lace")

etiquetaSeleccion = tkinter.Label(ventanaInicio , text = "Inicio de sesión", font = ("Consolas", 20),  bg = "old lace")
etiquetaSeleccion.pack()

etiquetaBlanca1 = tkinter.Label(ventanaInicio , text = "", bg = "old lace")
etiquetaBlanca1.pack()

etiquetaNombre = tkinter.Label(ventanaInicio , text = "Nombre: ", bg = "old lace",font = ("Consolas", 15))
etiquetaNombre.pack()

cajaNombre = tkinter.Entry(ventanaInicio)
cajaNombre.config(width = 26, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
cajaNombre.pack()

etiquetaContrasena = tkinter.Label(ventanaInicio , text = "Contraseña: ", bg = "old lace",font = ("Consolas", 15))
etiquetaContrasena.pack()

cajaContrasena = tkinter.Entry(ventanaInicio)
cajaContrasena.config(width = 26, font = ("Consolas", 10), bg = "burlywood1", fg = "black")
cajaContrasena.pack()

etiquetaBlanca1 = tkinter.Label(ventanaInicio , text = "", bg = "old lace")
etiquetaBlanca1.pack()

botonRegistro=tkinter.Button(ventanaInicio, text = "Registrarse",command = registro, font = ("Consolas", 11), bg = "burlywood1", fg = "black")
botonRegistro.pack()

def controlContrasena():
    control=0
    contrasena = cajaContrasena.get()
    nombre = cajaNombre.get()
    if(len(datos)>0):
        for i in range(len(datos)):
            if(datos[i][0]==nombre):
                if(datos[i][1]==contrasena):
                    control=1
                    menu()

        if(control==0):
            etiquetaContraIncorrecta = tkinter.Label(ventanaInicio , text = "Contraseña o usuario incorrectos", bg = "old lace",font = ("Consolas", 15))
            etiquetaContraIncorrecta.pack()
    else:
        etiquetaNoUsuarios = tkinter.Label(ventanaInicio , text = "No hay usuarios registrados", bg = "old lace",font = ("Consolas", 15))
        etiquetaNoUsuarios.pack()

                
botonInicio=tkinter.Button(ventanaInicio, text = "Ingresar",command = controlContrasena, font = ("Consolas", 11), bg = "burlywood1", fg = "black")
botonInicio.pack()

def inicio():
    ventanaInicio.withdraw() 
    ventanaInicio.deiconify()
inicio()
ventanaInicio.mainloop()