import tkinter as tk

ventana = tk.Tk()
ventana.geometry("300x200")

# AL USAR EL PLACE HAY QUE ESPECIFICAR LA POSICION MEDIANTE PIXELES
texto = tk.Label(ventana, text=("Hola"))
texto.place(x=50, y=50)

boton = tk.Button(ventana, text="Pez")
# EL ANCHOR LO QUE HACE ES ESPECIFICARLE AL PLACE EN FUNCION A QUE POSICION TENDRA QUE MOVERSE EL BOTON CON LOS PARAMETROS RELX Y RELY
boton.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

ventana.mainloop()