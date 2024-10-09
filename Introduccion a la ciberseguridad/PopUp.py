import tkinter

# CREACION DE LA VENTANA DE NOTIFICACION Y SU TITULO
ventana_notificacion = tkinter.Tk()
ventana_notificacion.geometry("400x300")
ventana_notificacion.title("Este es el titulo de la notificacion")

# CREACION Y AÑADIDO DEL TEXTO COMPLEMENTARIO DE LA NOTIFICACION
texto_complementario = tkinter.Label(ventana_notificacion, text="Este es un texto que sirve de ejemplo\n"
                                                                "Para representar como se ve el mensaje\n"
                                                                "Dentro de la notificación.")
texto_complementario.pack()

# CREACION DEL BOTON QUE CIERRA LA VENTANA
def cerrar_notificacion():
    ventana_notificacion.destroy()

boton = tkinter.Button(ventana_notificacion, text="ok", command=cerrar_notificacion)
boton.pack()

ventana_notificacion.mainloop()
