import tkinter as tk

ventana = tk.Tk()
ventana.geometry("400x300")

# Crear un Frame con tamaño fijo
frame = tk.Frame(ventana, width=200, height=100)
frame.pack()
frame.config(bg="blue")

# Añadir un Label dentro del Frame
texto = tk.Label(frame, text="Dentro del frame")
texto.pack()

ventana.mainloop()
