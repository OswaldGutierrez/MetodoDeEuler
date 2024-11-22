import tkinter as tk
import subprocess

def abrirEuler():
    subprocess.Popen(["python", "C:/Users/David/Documents/Python/Euler/Metodos/eulerMetodo.py"])
    botonEuler.config(state=tk.DISABLED)
    
def abrirError():
    subprocess.Popen(["python", "C:/Users/David/Documents/Python/Euler/Metodos/error.py"])
    botonError.config(state=tk.DISABLED)


# Configuración de la ventana principal 'main'
root = tk.Tk()
root.title("Interfaz principal")

# Hacemos la ventana responsiva
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

# Configura marco principal
frame = tk.Frame(root, bg="#F0F8FF", padx=20, pady=20)
frame.grid(sticky="nsew")

# Botón para los 2 métodos
botonEuler = tk.Button(frame, text="Euler", command=abrirEuler, font=("Helvetica", 16), bg="#ADD8E6", relief="raised", padx=10, pady=5)
botonEuler.pack(pady=20)

botonError = tk.Button(frame, text="Euler y Análisis de error", command=abrirError, font=("Helvetica", 16), bg="#ADD8E6", relief="raised", padx=10, pady=5)
botonError.pack(pady=20)

# Ajustar el tamaño mínimo de la ventana
root.minsize(400, 200)

# Loop principal de la aplicación
root.mainloop()