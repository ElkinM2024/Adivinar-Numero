import tkinter as tk
from tkinter import messagebox
import random

# Función para iniciar un nuevo juego
def nuevo_juego():
    global numero_secreto, intentos
    numero_secreto = random.randint(1, 100)  # Generar número secreto entre 1 y 100
    intentos = 0
    resultado_label.config(text="¡Juego iniciado! Adivina el número entre 1 y 100.")
    intentos_label.config(text=f"Intentos: {intentos}")
    entrada_numero.delete(0, tk.END)  # Limpiar la entrada

# Función para verificar el intento del jugador
def verificar_intento():
    global intentos
    try:
        numero_intento = int(entrada_numero.get())  # Obtener el número ingresado
    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un número válido.")
        return
    
    intentos += 1
    intentos_label.config(text=f"Intentos: {intentos}")

    if numero_intento < numero_secreto:
        resultado_label.config(text="¡El número es mayor!")
    elif numero_intento > numero_secreto:
        resultado_label.config(text="¡El número es menor!")
    else:
        resultado_label.config(text=f"¡Felicidades! Has adivinado el número {numero_secreto} en {intentos} intentos.")
        messagebox.showinfo("¡Ganaste!", f"¡Has adivinado el número en {intentos} intentos! ¿Quieres jugar de nuevo?")
        nuevo_juego()  # Iniciar un nuevo juego

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Juego de Adivinar el Número")
root.geometry("400x300")

# Variables globales
numero_secreto = None
intentos = 0

# Etiquetas y campos
resultado_label = tk.Label(root, text="¡Adivina el número entre 1 y 100!", font=("Arial", 14))
resultado_label.pack(pady=20)

entrada_numero = tk.Entry(root, font=("Arial", 14))
entrada_numero.pack(pady=10)

intentos_label = tk.Label(root, text="Intentos: 0", font=("Arial", 12))
intentos_label.pack(pady=10)

# Botones
verificar_button = tk.Button(root, text="Verificar intento", font=("Arial", 12), command=verificar_intento)
verificar_button.pack(pady=10)

nuevo_juego_button = tk.Button(root, text="Nuevo Juego", font=("Arial", 12), command=nuevo_juego)
nuevo_juego_button.pack(pady=10)

# Iniciar el primer juego
nuevo_juego()

# Iniciar la aplicación
root.mainloop()
