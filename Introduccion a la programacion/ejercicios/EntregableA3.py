import tkinter as tk
import string
import random

# FUNCIONES PARA LA MANIPULACION DE DATOS EN EL PROGRAMA
def generar_contraseña():
    """
    Genera una contraseña basada en los parámetros proporcionados por el usuario.

    Los parámetros se obtienen de los campos de entrada de la interfaz gráfica:
    - Longitud de la contraseña
    - Cantidad de mayúsculas
    - Cantidad de caracteres especiales
    - Cantidad de dígitos

    La función verifica que la suma de los caracteres especiales, mayúsculas y dígitos
    no supere la longitud de la contraseña. Si es válido, genera una contraseña aleatoria
    y la muestra en el campo de texto final.

    Si los valores no son válidos, muestra un mensaje de error en el campo de texto final.
    """    
    # OBTENCION DE LOS VALORES QUE SE NECESITAN PARA GENERAR LA CONTRASEÑA DE TKINTER
    try:
        longitud_contraseña = int(entry_longitud.get())
        cantidad_mayusculas = int(entry_mayusculas.get())
        cantidad_especiales = int(entry_especiales.get())
        cantidad_digitos = int(entry_digitos.get())
    except ValueError:
        texto_final.config(text="Alguno de los valores requeridos no es válido")
        return
    
    # Verificar que la suma de los parámetros no supere la longitud de la contraseña
    if cantidad_especiales + cantidad_mayusculas + cantidad_digitos > longitud_contraseña:
        texto_final.config(text="La suma de caracteres especiales, mayúsculas y dígitos no puede superar la longitud de la contraseña.")
    
    # Definir los conjuntos de caracteres
    especiales = string.punctuation
    mayusculas = string.ascii_uppercase
    digitos = string.digits
    minusculas = string.ascii_lowercase
    
    # Crear una lista inicial con los caracteres especiales, mayúsculas y dígitos
    contraseña = []
    contraseña.extend(random.choices(especiales, k=cantidad_especiales))
    contraseña.extend(random.choices(mayusculas, k=cantidad_mayusculas))
    contraseña.extend(random.choices(digitos, k=cantidad_digitos))
    
    # Calcular cuántos caracteres faltan para alcanzar la longitud deseada
    faltan = longitud_contraseña - len(contraseña)
    
    # Completar con caracteres minúsculas
    contraseña.extend(random.choices(minusculas, k=faltan))
    
    # Mezclar los caracteres para que no estén agrupados por tipo
    random.shuffle(contraseña)
    
    # Convertir la lista de caracteres en una cadena
    contraseña_final = ''.join(contraseña)
    
    texto_final.config(text=f"La contraseña generada es: {contraseña_final}")

def guardar_contraseña_fichero():
    """
    Guarda la contraseña generada en un archivo de texto especificado por el usuario.

    La contraseña se obtiene del campo de texto final. Si no hay una contraseña generada,
    muestra un mensaje de error. Si el archivo no se especifica, también muestra un error.

    Si todo es válido, la contraseña se escribe en el archivo especificado.

    En caso de error al guardar, muestra un mensaje de error en el campo de texto final.
    """
    archivo = entry_archivo_guardado.get()
    if not archivo:
        texto_final.config(text="Por favor, especifique un archivo para guardar la contraseña.")
        return
    
    contraseña = texto_final.cget("text").split(": ")[-1]
    if not contraseña:
        texto_final.config(text="No hay contraseña generada para guardar.")
        return
    
    try:
        with open(archivo, "w") as f:
            f.write(contraseña)
        texto_final.config(text=f"Contraseña guardada en {archivo}")
    except Exception as e:
        texto_final.config(text=f"Error al guardar la contraseña: {e}")

def recuperacion_contraseña():
    """
    Recupera una contraseña previamente guardada desde un archivo de texto.

    El archivo se especifica en el campo de entrada correspondiente. Si el archivo no
    existe o no se puede leer, muestra un mensaje de error en el campo de texto final.

    Si la recuperación es exitosa, muestra la contraseña recuperada en el campo de texto final.
    """
    archivo = entry_archivo_recuperar.get()
    if not archivo:
        texto_final.config(text="Por favor, especifique un archivo para recuperar la contraseña.")
        return
    
    try:
        with open(archivo, "r") as f:
            contraseña = f.read().strip()
        texto_final.config(text=f"Contraseña recuperada: {contraseña}")
    except Exception as e:
        texto_final.config(text=f"Error al recuperar la contraseña: {e}")

def borrado_campos():
    """
    Borra todos los campos de entrada y el texto final de la interfaz gráfica.

    Esta función limpia los campos de entrada para la longitud de la contraseña,
    cantidad de mayúsculas, caracteres especiales, dígitos, archivos de guardado
    y recuperación, así como el texto final que muestra la contraseña generada.
    """
    entry_longitud.delete(0, tk.END)
    entry_mayusculas.delete(0, tk.END)
    entry_especiales.delete(0, tk.END)
    entry_digitos.delete(0, tk.END)
    entry_archivo_guardado.delete(0, tk.END)
    entry_archivo_recuperar.delete(0, tk.END)
    texto_final.config(text="")

ventana = tk.Tk()
ventana.title("Generador de contraseñas")

# CONFIGURACION DEL GRID DE LA VENTANA
for _ in range(9):
    if _ < 2:
        ventana.columnconfigure(_, weight=1)
    ventana.rowconfigure(_, weight=1)

# OBTENCION DE LA LONGITUD DE LA CONTRASEÑA
texto_longitud = tk.Label(ventana, text="Longitud de contraseña:")
texto_longitud.grid(column=0, row=0)

entry_longitud = tk.Entry(ventana, width=7)
entry_longitud.grid(column=1, row=0)

# OBTENCION DE LA CANTIDAD DE MAYUSCULAS
texto_mayusculas = tk.Label(ventana, text="Cantidad de mayúsculas:")
texto_mayusculas.grid(column=0, row=1)

entry_mayusculas = tk.Entry(ventana, width=7)
entry_mayusculas.grid(column=1, row=1)

# OBTENCION DE LA CANTIDAD DE ESPECIALES
texto_especiales = tk.Label(ventana, text="Cantidad de especiales:")
texto_especiales.grid(column=0, row=2)

entry_especiales = tk.Entry(ventana, width=7)
entry_especiales.grid(column=1, row=2)

# OBTENCION DE LA CANTIDAD DE DIGITOS
texto_digitos = tk.Label(ventana, text="Cantidad de dígitos:")
texto_digitos.grid(column=0, row=3)

entry_digitos = tk.Entry(ventana, width=7)
entry_digitos.grid(column=1, row=3)

# OBTENCION DE ARCHIVO PARA GUARDAR LA CONTRASEÑA
texto_archivo_guardado = tk.Label(ventana, text="Archivo para guardar:")
texto_archivo_guardado.grid(column=0, row=4)

entry_archivo_guardado = tk.Entry(ventana, width=20)
entry_archivo_guardado.grid(column=1, row=4)

# OBTENCION DE ARCHIVO EN EL QUE RECUPERAR LA CONTRASEÑA
texto_archivo_recuperar = tk.Label(ventana, text="Archivo para recuperar:")
texto_archivo_recuperar.grid(column=0, row=5)

entry_archivo_recuperar = tk.Entry(ventana, width=20)
entry_archivo_recuperar.grid(column=1, row=5)

# BOTON PARA PODER GENERAR LA CONTRASEÑA
boton_generar_contra = tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña)
boton_generar_contra.grid(column=0, row=6)

# BOTON PARA PODER GUARDAR LA CONTRASEÑA EN UN FICHERO
boton_guardado_contra = tk.Button(ventana, text="Guardar Contraseña en Fichero", command=guardar_contraseña_fichero)
boton_guardado_contra.grid(column=1, row=6)

# BOTON PARA PODER RECUPERAR LA CONTRASEÑA DE UN FICHERO
boton_recuperar_contra = tk.Button(ventana, text="Recuperar contraseña", command=recuperacion_contraseña)
boton_recuperar_contra.grid(column=0, row=7)

# BOTON PARA BORRAR TODOS LOS CAMPOS
boton_borrado = tk.Button(ventana, text="Borrar campos", command=borrado_campos)
boton_borrado.grid(column=1, row=7)

# TEXTO FINAL DEL PROGRAMA
texto_final = tk.Label(ventana, text="")
texto_final.grid(column=0, row=8, columnspan=2)

# BUCLE DE LA VENTANA EN TKINTER
ventana.mainloop()