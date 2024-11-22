import sys
import os
import tkinter as tk
from sympy import symbols, lambdify, sympify, Derivative
import re

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleInterfaz


class Error:
    def __init__(self):
        self.root = tk.Tk()
        self.entryFuncion, self.entryCondicionY, self.entryTamañoH, self.entryNumeroPasos, self.entryX0, self.entryXf, self.botonCalcular, self.entrySol = styleInterfaz.aplicarEstiloInterfaz(self.root)
        
        # Configurar el botón
        self.botonCalcular.config(command=self.calcularErrorEuler)
        
    def calcularErrorEuler(self):
        try:
            # Obtener valores de las entradas
            funcionStr = self.entryFuncion.get().strip()
            condicionY = float(self.entryCondicionY.get())
            tamañoH = float(self.entryTamañoH.get())
            x0 = float(self.entryX0.get())
            xf = float(self.entryXf.get())
            solucionAnalítica = self.entrySol.get().strip()  # Nueva entrada
            
            # Validar y calcular número de pasos si no está definido
            if self.entryNumeroPasos.get().strip():
                numPasos = int(self.entryNumeroPasos.get())
            else:
                numPasos = int((xf - x0) / tamañoH)
            
            # Limpiar y transformar las entradas de las ecuaciones
            if "=" in funcionStr:
                _, funcionStr = funcionStr.split("=")
                funcionStr = funcionStr.strip()
            
            # Reemplazar 'y' por la derivada 'Derivative(y, x)' y asegurar el * entre variables
            funcionStr = re.sub(r"y'", "Derivative(y, x)", funcionStr)
            funcionStr = re.sub(r'(?<=[0-9a-zA-Z])(?=[a-zA-Z])', '*', funcionStr)  # Para coeficientes y variables
            
            solucionAnalítica = solucionAnalítica.replace("e**", "exp")  # Convertir 'e**' a 'exp'

            # Parsear las funciones
            x, y = symbols('x y')
            funcion = lambdify((x, y), sympify(funcionStr), "math")
            solucionExacta = lambdify(x, sympify(solucionAnalítica), "math")

            listaXs = [x0]
            listaYs = [condicionY]
            listaErrores = []
            
            # Implementación del método de Euler con cálculo del error
            for i in range(numPasos):
                xi, yi = listaXs[-1], listaYs[-1]
                yiNuevo = yi + tamañoH * funcion(xi, yi)
                xiNuevo = xi + tamañoH
                listaXs.append(xiNuevo)
                listaYs.append(yiNuevo)

                # Calcular error absoluto con la solución exacta
                error = abs(solucionExacta(xiNuevo) - yiNuevo)

                # Evaluar y formatear los errores numéricamente
                listaErrores.append(error)
            
            # Generar resultados en forma de texto
            resultados = "\n".join([f"x{i}: {listaXs[i]:.5f}, Aproximación{i}: {listaYs[i]:.5f}, Error Absoluto{i}: {listaErrores[i-1]:.5e}" for i in range(1, len(listaXs))])
            self.mostrarResultado(f"Resultados:\n{resultados}")
        
        except Exception as e:
            self.mostrarResultado(f"Error: {str(e)}")

    def mostrarResultado(self, mensaje):
        resultadoInterfaz = tk.Toplevel(self.root)
        resultadoInterfaz.title("Resultado")
        labelResultado = tk.Label(resultadoInterfaz, text=mensaje, justify="left")
        labelResultado.pack(padx=20, pady=20)
    
    def iniciar(self):
        self.root.mainloop()
        

if __name__ == "__main__":
    app = Error()
    app.iniciar()
