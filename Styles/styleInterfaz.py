import tkinter as tk


def aplicarEstiloInterfaz(root):
    # Configuración de la interfaz gráfica
    root.title("Método Euler")
    root.config(bg="lightblue")

    # Hacer que la ventana sea responsiva
    root.rowconfigure(0, weight=1)
    root.columnconfigure([0, 1, 2], weight=1)
    root.rowconfigure(1, weight=1)

    #Configuración del marco principal
    frame = tk.Frame(root, bg="lightblue", padx=20, pady=20)
    frame.grid(sticky="nsew")

    # Ajustar el tamaño mínimo de la ventana
    root.minsize(400, 223)
    
    # Etiquetas
    etiquetaFuncion = tk.Label(frame, text="Ingresa la función EDOs")
    etiquetaFuncion.grid(sticky="w", row=0, column=0, padx=10, pady=5)
    
    etiquetaCondicionY = tk.Label(frame, text="Ingresa la condición inicial Y:")
    etiquetaCondicionY.grid(sticky="w", row=1, column=0, padx=10, pady=5)
    
    etiquetaTamañoH = tk.Label(frame, text="Ingresa el tamaño del paso h:")
    etiquetaTamañoH.grid(sticky="w", row=2, column=0, padx=10, pady=5)
    
    etiquetaNumeroPasos = tk.Label(frame, text="Ingresa el número de pasos N:")
    etiquetaNumeroPasos.grid(sticky="w", row=3, column=0, padx=10, pady=5)
    
    etiquetaX0 = tk.Label(frame, text="Ingresa el valor inicial de X0:")
    etiquetaX0.grid(sticky="w", row=4, column=0, padx=10, pady=5)
    
    etiquetaXf = tk.Label(frame, text="Ingresa el valor inicial de Xf:")
    etiquetaXf.grid(sticky="w", row=5, column=0, padx=10, pady=5)
    
    # Entrys o TextBox
    entryFuncion = tk.Entry(frame)
    entryFuncion.grid(row=0, column=1, padx=10, pady=5)
    
    entryCondicionY = tk.Entry(frame)
    entryCondicionY.grid(row=1, column=1, padx=10, pady=5)
    
    entryTamañoH = tk.Entry(frame)
    entryTamañoH.grid(row=2, column=1, padx=10, pady=5)
    
    entryNumeroPasos = tk.Entry(frame)
    entryNumeroPasos.grid(row=3, column=1, padx=10, pady=5)
    
    entryX0 = tk.Entry(frame)
    entryX0.grid(row=4, column=1, padx=10, pady=5)
    
    entryXf = tk.Entry(frame)
    entryXf.grid(row=5, column=1, padx=10, pady=5)
    
    # Botón para calcular
    botonCalcular = tk.Button(frame, text="Calcular")
    botonCalcular.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="ew")
    
    # Loop principal de la aplicación
    return (entryFuncion, entryCondicionY, entryTamañoH, entryNumeroPasos, entryX0, entryXf, botonCalcular)
    