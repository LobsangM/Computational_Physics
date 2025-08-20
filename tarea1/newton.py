import numpy as np
import sys

class Polinomio:
    def __init__(self, grado, coeficientes):
        try:
            self.n = int(grado)
        except:
            print("El grado del polinomio debe ser un número entero")
            sys.exit()
        try:
            self.coefs = np.array(coeficientes, dtype=float)
        except:
            print("Los coeficientes deben ser números")
            sys.exit()

        if self.coefs.size != (self.n + 1):
            print("El número de coeficientes debe ser ", self.n + 1, self.coefs)
            sys.exit()
        
    def derivada(self):
        if self.n == 0:
            return Polinomio(grado=0, coeficientes=[0])
        nuevos_coefs = [self.coefs[i] * (self.n - i) for i in range(self.n)]
        return Polinomio(grado=self.n - 1, coeficientes=nuevos_coefs)
    
    def evaluar(self, x):
        return sum(coef * x**(self.n - i) for i, coef in enumerate(self.coefs))
        


class NewtonMethod(Polinomio):
    def __init__(self, grado, coeficientes, max_inter=100, tolerancia=1e-8):
        super().__init__(grado, coeficientes)
        self.max_inter = max_inter
        self.tolerancia = tolerancia

    def calcular(self, x0):
        x = x0
        for i in range(self.max_inter):
            f_x = self.evaluar(x)
            if abs(f_x) < self.tolerancia:
                return x
            f_prima_x = self.derivada().evaluar(x)
            if f_prima_x == 0:
                return None
            x_new = x - f_x / f_prima_x
            if abs(x_new - x) < self.tolerancia:
                return x_new
            x = x_new
        return x
    
    def calcular_todas(self, x0s):
        resultados = []
        for x0 in x0s:
            resultados.append(self.calcular(x0))
        return resultados
    
    def agrupar_raices(self, raices):
        grupos = []
        for r in raices:
            if r is None:
                continue
            found = False
            for g in grupos:
                if abs(r - g) < self.tolerancia:
                    found = True
                    break
            if not found:
                grupos.append(r)
        return grupos
    
    def encontrar_raices(self, valores_iniciales):
        raices = self.calcular_todas(valores_iniciales)
        return self.agrupar_raices(raices)
