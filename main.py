import numpy as np
import numpy.polynomial.legendre as leg
import scipy.linalg as la
import matplotlib.pyplot as plt
import csv

class MontanaRusa:
    
    # Funcion para aplicar el metodo de trazador cubico sujeto
    def trazador_cubico_sujeto(self, x_valores, y_valores, dy_inicial, dy_final):
        
        n = len(x_valores)
        diferencia_valores_x = np.diff(x_valores)

        # Construimos la matriz A
        matriz = np.zeros((n, n))
        matriz[0, 0] = 2 * diferencia_valores_x[0]
        matriz[0, 1] = diferencia_valores_x[0]

        for i in range(1, n - 1):
            matriz[i, i - 1] = diferencia_valores_x[i - 1]
            matriz[i, i] = 2 * (diferencia_valores_x[i - 1] + diferencia_valores_x[i])
            matriz[i, i + 1] = diferencia_valores_x[i]

        matriz[n - 1, n - 2] = diferencia_valores_x[n - 2]
        matriz[n - 1, n - 1] = 2 * diferencia_valores_x[n - 2]

        # Construir el vector b
        b = np.zeros(n)
        b[0] = 3 * ((y_valores[1] - y_valores[0]) / diferencia_valores_x[0]) - 3 * dy_inicial

        for i in range(1, n - 1):
            b[i] = 3 * ((y_valores[i + 1] - y_valores[i]) / diferencia_valores_x[i]) - 3 * ((y_valores[i] - y_valores[i - 1]) / diferencia_valores_x[i - 1])

        b[n - 1] = 3 * dy_final - 3 * ((y_valores[n - 1] - y_valores[n - 2]) / diferencia_valores_x[n - 2])

        # Resolvemos el sistema de ecuaciones Ax = b
        resolucion = la.solve(matriz, b)

        # Calcular los coeficientes a, b, d
        a = y_valores[:-1]
        b = (np.diff(y_valores) / diferencia_valores_x) - (diferencia_valores_x / 3) * (2 * resolucion[:-1] + resolucion[1:])
        d = np.diff(resolucion) / (3 * diferencia_valores_x)
       
        def grafico_curva(xi):
            
            i = np.searchsorted(x_valores, xi) - 1
            i = np.clip(i, 0, n - 2)
            dx = xi - x_valores[i]

            return a[i] + b[i] * dx + resolucion[i] * dx**2 + d[i] * dx**3
        
        return grafico_curva
    
    
    # Funcion que calculo los coeficiente del polinomio de minimo cuadrado
    def polinomios_minimos_cuadrados(self, x_valores, y_valores, grado_polonomio):
        coeficientes = np.polyfit(x_valores, y_valores, grado_polonomio)
        return coeficientes
    
    # Funcion que calculo los coeficientes de polinomios ortogonales
    def polinomios_ortogonales(self, x_valores, y_valores, grado_polonomio):
        coeficientes = leg.legfit(x_valores, y_valores, grado_polonomio)
        return coeficientes
    
    # Funcion que resuelve las ecuaciones
    def resolucion_ecuaciones(self, matriz, vector):
        print('\nResolucion del sistema de ecuaciones: ',np.linalg.solve(matriz, vector))
        return np.linalg.solve(matriz, vector)
    
class Grafico:

    def __init__(self):
        self.fig, self.ax = plt.subplots(2, 2, figsize = (12, 7))


    def graficar_paso1(self, puntos_x, puntos_y, valores_x, valores_y):
        self.ax[0][0].plot(valores_x, valores_y, '-', color='blue', label='Trazador cubico sujeto')
        self.ax[0][0].plot(puntos_x, puntos_y, 'o', color='black', label='Puntos de control')
        self.ax[0][0].legend()
        self.ax[0][0].set_title('Interpolacion de trazador cubico sujeto')
        self.ax[0][0].grid(True)

    def graficar_paso2(self, puntos_x, puntos_y, valores_x, valores_y, grado):
        self.ax[0][1].plot(valores_x, valores_y, '-', color='red', label=f'Polinomio de grado {grado}')
        self.ax[0][1].plot(puntos_x, puntos_y, 'o', color='black', label='Datos experimentales')
        for i in range(len(puntos_x)):
            self.ax[0][1].vlines(puntos_x[i], min(puntos_y[i], valores_y[i]), max(puntos_y[i], valores_y[i]), color='red', linestyle='dotted')
        self.ax[0][1].legend()
        self.ax[0][1].set_title('Ajuste de polinomio de mínimos cuadrados')
        self.ax[0][1].grid(True)

    def graficar_paso3(self, puntos_x, puntos_y, valores_x, valores_y, grado):
        self.ax[1][0].plot(valores_x, valores_y, '-', color='green', label=f'Polinomio ortogonal grado {grado}')
        self.ax[1][0].plot(puntos_x, puntos_y, 'o', color='black', label='Puntos')
        self.ax[1][0].legend()
        self.ax[1][0].set_title('Ajuste con polinomios ortogonales')
        self.ax[1][0].grid(True)

    def graficar_paso4(self, variables, solucion):
        # Crear valores x para el plot (índices de las variables)
        x_vals = np.arange(len(variables))
        
        # Graficar línea continua para la solución
        self.ax[1][1].plot(x_vals, solucion, '-o', color='purple', 
                          label='Solución del sistema', markersize=8)
                
        # Configuración del gráfico
        self.ax[1][1].set_xticks(x_vals)
        self.ax[1][1].set_xticklabels(variables)
        self.ax[1][1].legend()
        self.ax[1][1].set_title('Solución del Sistema de Ecuaciones')
        self.ax[1][1].set_xlabel('Variables')
        self.ax[1][1].set_ylabel('Valor')
        self.ax[1][1].grid(True)


    def mostrar(self):
        plt.tight_layout()
        plt.show()


class Main():

    def lector(paso):

        def convertFloat(arr):
            return [float(i) for i in arr]
        
        def convertxParticiones(particiones):
            arr = []
            for part in particiones:
                arr.append(convertFloat(part.replace('[','').replace(']','').split(',')))
            return arr

        with open('data.csv', newline='') as file:
            reader = csv.reader(file, delimiter=';')
            data = list(reader)

        if paso == 1:
            x_puntos = np.array(convertFloat(data[1][0].strip('[]').split(',')), dtype=float)
            y_puntos = np.array(convertFloat(data[1][1].strip('[]').split(',')), dtype=float)
            return x_puntos, y_puntos
        elif paso == 2:
            x_puntos = np.array(convertFloat(data[3][0].strip('[]').split(',')), dtype=float)
            y_puntos = np.array(convertFloat(data[3][1].strip('[]').split(',')), dtype=float)
            return x_puntos, y_puntos
        else:
            particionesX = data[5][0].split('],[')
            x_puntos = np.array(convertxParticiones(particionesX), dtype=float)
            y_puntos = np.array(convertFloat(data[5][1].strip('[]').split(',')), dtype=float)
            return x_puntos, y_puntos

    '''Inicializar'''
    montana_rusa = MontanaRusa()
    grafica = Grafico()

    '''Paso 1'''
    # Datos de entrada para el Metodo trazador cubico sujeto
    x_data, y_data = lector(1)
    x_vals = np.linspace(0, 5, 100)

    # Calculo de derivadas dy_inicial y dy_final
    dy_0 = (y_data[1] - y_data[0]) / (x_data[1] - x_data[0])
    dy_n = (y_data[-1] - y_data[-2]) / (x_data[-1] - x_data[-2])

    # Calculo trazador cubico sujeto
    grafico_curva_var = montana_rusa.trazador_cubico_sujeto(x_data, y_data, dy_0, dy_n)

    # Evaluar el trazador cubico en los puntos x_vals
    y_vals = grafico_curva_var(x_vals)

    # Graficar los resultados
    grafica.graficar_paso1(x_data, y_data, x_vals, y_vals)
    
    '''Paso 2'''
    # Datos de entrada para calculo de polinomios minimos cuadrados
    x_polinomios_minimos_cuadrados, y_polinomios_minimos_cuadrados = lector(2)
    x_vals_minimos_cuadrados = np.linspace(0, 4, 5)

    # Suponemos el grado del polinomio
    grado = 1

    # Calcular los coeficientes del polinomio de mínimos cuadrados
    coeficientes_cuadrados = montana_rusa.polinomios_minimos_cuadrados(x_polinomios_minimos_cuadrados, y_polinomios_minimos_cuadrados, grado)

    # Evaluar el polinomio en los puntos x_vals
    y_vals_minimos_cuadrados = np.polyval(coeficientes_cuadrados, x_vals_minimos_cuadrados)

    # Graficacion de polinomios minimos cuadrados
    grafica.graficar_paso2(x_polinomios_minimos_cuadrados, y_polinomios_minimos_cuadrados, x_vals_minimos_cuadrados, y_vals_minimos_cuadrados, grado)
    print("\nCoeficientes del polinomio:\n", coeficientes_cuadrados)

    '''Paso 3'''
    # Datos de entrada para polinomio ortogonal
    x_puntos_ortogonal = np.array([-1, 0, 1, 2, 3, 4, 5, 6, 7, 8])
    y_puntos_ortogonal = np.array([0.2, 0.5, 0.8, 1.1, 1.3, 1.2, 0.9, 0.6, 0.3, 0.1])
    x_valores_ortogonal = np.linspace(-1, 8, 100)

    # Grado del polinomio
    grado_ortogonal = 10

    # Calcular los coeficientes del polinomio ortogonal
    coeficientes_ortogonal = montana_rusa.polinomios_ortogonales(x_puntos_ortogonal, y_puntos_ortogonal, grado_ortogonal)

    # Evaluar el polinomio en los puntos x_valores_ortogonal usando el polinomo de Legendre
    y_valores_ortogonal = leg.legval(x_valores_ortogonal, coeficientes_ortogonal)

    # Graficacion de polinomios ortogonales
    grafica.graficar_paso3(x_puntos_ortogonal, y_puntos_ortogonal, x_valores_ortogonal, y_valores_ortogonal, grado_ortogonal)
    print("\nCoeficientes del polinomio ortogonal:\n", coeficientes_ortogonal)

    '''Paso 4'''
    # Datos de entrada para la resolucion de ecuaciones
    A, b = lector(4)
    solucion = montana_rusa.resolucion_ecuaciones(A, b)

    # Graficar solucion de ecuaciones
    # variables = ['x1', 'x2', 'x3']
    # grafica.graficar_paso4(variables, solucion)
    # print("\nSolucion del sistema de ecuaciones:\n", solucion)


    '''Mostrar todos los graficos'''
    grafica.mostrar()


if __name__ == "__main__":
    Main()








