import sys
import os
import tkinter as tk

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Styles import styleInterfaz


##prueba
class Euler:
    def __init__(self):
        self.root = tk.Tk()
        self.entryFuncion, self.entryCondicionY, self.entryTamañoH, self.entryNumeroPasos, self.entryX0, self.entryXf, self.botonCalcular = styleInterfaz.aplicarEstiloInterfaz(self.root, returnTodos=False)
        
        self.botonCalcular.config(command=self.calcularEuler)
        
    def calcularEuler(self):
        try:
            # Obtener valores de las entradas
            funcion_str = self.entryFuncion.get().strip()
            condicion_y = float(self.entryCondicionY.get())
            tamañoH = float(self.entryTamañoH.get())
            x0 = float(self.entryX0.get())
            xf = float(self.entryXf.get())
            
            # Validar y calcular número de pasos si no está definido
            if self.entryNumeroPasos.get().strip():
                n_pasos = int(self.entryNumeroPasos.get())
            else:
                n_pasos = int((xf - x0) / tamañoH)
            
            # Validar formato de la ecuación ingresada
            if "=" in funcion_str:
                lhs, rhs = funcion_str.split("=")
                funcion_str = rhs.strip()  # Usar solo la parte derecha

            # Limpiar entrada de texto
            funcion_str = funcion_str.replace("'", "").replace('"', '').replace("²", "**2").replace("^", "**")
            
            # Parsear la función usando sympy
            from sympy import symbols, lambdify, sympify
            x, y = symbols('x y')
            funcion = lambdify((x, y), sympify(funcion_str), "math")

            listaXs = [x0]
            listaYs = [condicion_y]
            
            # Implementación del método de Euler
            for i in range(n_pasos):
                xi, yi = listaXs[-1], listaYs[-1]
                yiNuevo = yi + tamañoH * funcion(xi, yi)
                xiNuevo = xi + tamañoH
                listaXs.append(xiNuevo)
                listaYs.append(yiNuevo) 
            
            # Generar resultados en forma de texto
            resultado = "\n".join([f"x{i}: {listaXs[i]:.5f}, y{i}: {listaYs[i]:.5f}" for i in range(len(listaXs))])
            self.mostrarResultado(resultado)
        
        except Exception as e:
            self.mostrarResultado(f"Error: {str(e)}")
            
            
    def mostrarResultado(self, mensaje):
        resultadoInterfaz = tk.Toplevel(self.root)
        resultadoInterfaz.title("Resultado")
        labelResultado = tk.Label(resultadoInterfaz, text=mensaje)
        labelResultado.pack(padx=20, pady=20)
    
    def iniciar(self):
        self.root.mainloop()
        
if __name__ == "__main__":
    app = Euler()
    app.iniciar()





