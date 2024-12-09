import tkinter as tk

n1 = 0
n2 = 0
operacion = "nada"

# FUNCIONES PARA LA MANIPULACION DE LOS DATOS
def mostrar_numero_1():
    numero_juntar = "1"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_2():
    numero_juntar = "2"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_3():
    numero_juntar = "3"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_4():
    numero_juntar = "4"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_5():
    numero_juntar = "5"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_6():
    numero_juntar = "6"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_7():
    numero_juntar = "7"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_8():
    numero_juntar = "8"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_9():
    numero_juntar = "9"
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        numero_mostrar = numero_juntar
    else:
        numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def mostrar_numero_0():
    numero_juntar = "0"
    numero_actual = texto_numero.cget("text")
    numero_mostrar = numero_actual + numero_juntar
    texto_numero.config(text=numero_mostrar)

def borrado_numero():
    global n1, operacion
    numero_actual = texto_numero.cget("text")
    if numero_actual == "0":
        n1 = 0
        texto_ayuda.config(text="")
        operacion = "nada"
    numero_mostrar = "0"
    texto_numero.config(text=numero_mostrar)

def sumar():
    global n1, operacion
    n1 = texto_numero.cget("text")
    operacion = "suma"
    texto_numero.config(text="0")
    texto_ayuda.config(text=n1)

def restar():
    global n1, operacion
    n1 = texto_numero.cget("text")
    operacion = "resta"
    texto_numero.config(text="0")
    texto_ayuda.config(text=n1)

def multiplicar():
    global n1, operacion
    n1 = texto_numero.cget("text")
    operacion = "multiplicacion"
    texto_numero.config(text="0")
    texto_ayuda.config(text=n1)

def dividir():
    global n1, operacion
    n1 = texto_numero.cget("text")
    operacion = "division"
    texto_numero.config(text="0")
    texto_ayuda.config(text=n1)

def resultado():
    global n1, n2, operacion
    if operacion == "nada":
        texto_ayuda.config(text="No hay operacion")
    n1 = int(n1)
    n2 = int(texto_numero.cget("text"))
    match operacion:
        case "suma":
            resultado = int(n1 + n2)
        case "resta":
            resultado = int(n1 - n2)
        case "multiplicacion":
            resultado = int(n1 * n2)
        case "division":
            resultado = float(n1 / n2)
    texto_numero.config(text="0")
    texto_ayuda.config(text=resultado)
    n1 = int(resultado)

ventana = tk.Tk()
# CONFIGURACION DE LAS FILAS Y COLUMNAS DE LA VENTANA
for _ in range(0,6):
    ventana.rowconfigure(_, weight=1)
    if _ < 4:
        ventana.columnconfigure(_, weight=1)

# DISTRIBUCION DE LOS BOTONES DE LA CALCULADORA
texto_ayuda = tk.Label(ventana, text="")
texto_ayuda.grid(column=0, row=0)

texto_numero = tk.Label(ventana, text="0")
texto_numero.grid(column=1, row=0, sticky="nsew")

boton_borrado = tk.Button(ventana, text="AC", command=borrado_numero)
boton_borrado.grid(column=2, row=0, columnspan=2, sticky="nsew")

numero_1 = tk.Button(ventana, text="1", command=mostrar_numero_1)
numero_1.grid(column=0 , row=1, sticky="nsew")

numero_2 = tk.Button(ventana, text="2", command=mostrar_numero_2)
numero_2.grid(column=1, row=1, sticky="nsew")

numero_3 = tk.Button(ventana, text="3", command=mostrar_numero_3)
numero_3.grid(column=2, row=1, sticky="nsew")

boton_suma = tk.Button(ventana, text="+", command=sumar)
boton_suma.grid(column=3, row=1, sticky="nsew")

numero_4 = tk.Button(ventana, text="4", command=mostrar_numero_4)
numero_4.grid(column=0, row=2, sticky="nsew")

numero_5 = tk.Button(ventana, text="5", command=mostrar_numero_5)
numero_5.grid(column=1, row=2, sticky="nsew")

numero_6 = tk.Button(ventana, text="6", command=mostrar_numero_6)
numero_6.grid(column=2, row=2, sticky="nsew")

boton_resta = tk.Button(ventana, text="-", command=restar)
boton_resta.grid(column=3, row=2, sticky="nsew")

numero_7 = tk.Button(ventana, text="7", command=mostrar_numero_7)
numero_7.grid(column=0, row=3, sticky="nsew")

numero_8 = tk.Button(ventana, text="8", command=mostrar_numero_8)
numero_8.grid(column=1, row= 3, sticky="nsew")

numero_9 = tk.Button(ventana, text="9", command=mostrar_numero_9)
numero_9.grid(column=2, row=3, sticky="nsew")

boton_division = tk.Button(ventana, text="/", command=dividir)
boton_division.grid(column=3, row=3, sticky="nsew")

numero_0 = tk.Button(ventana, text="0", command=mostrar_numero_0)
numero_0.grid(column=0, row=4, sticky="nsew")

boton_igualdad = tk.Button(ventana, text="=", command=resultado)
boton_igualdad.grid(column=1, row=4, columnspan=2, sticky="nsew")

boton_multiplicacion = tk.Button(ventana, text="*", command=multiplicar)
boton_multiplicacion.grid(column=3, row=4, sticky="nsew")

ventana.mainloop()