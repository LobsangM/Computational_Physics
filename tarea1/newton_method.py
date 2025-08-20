import numpy as np
import sys
class polinomio:
    def __init__(self, grado, coeficientes):
        try:
            self.n = int(grado)
        except:
            print("El grado del polinomio debe ser un número entero")
            sys.exit()
        try:
            self.coefs = np.array( coeficientes, dtype= float)
        except:
            print("Los coeficientes deben ser números")

        if self.coefs.size != (self.n + 1) :
            print("El número de coeficientes debe ser ", self.n + 1, self.coefs)
            sys.exit()
        
    def derivada(self):
        if self.n == 0:
            return polinomio(grado=0, coeficientes=0)
        nuevos_coefs= [self.coefs[i]*(self.n -i) for i in range(self.n)]
        return polinomio(grado=self.n-1, coeficientes=nuevos_coefs)
    
    def evaluar(self, x):
        return sum(coef * x**(self.n - i) for i, coef in enumerate(self.coefs))

class Newton_Method(polinomio):
    def __init__(self, grado, coeficientes, max_inter, tolerancia):
        super().__init__(grado, coeficientes)
        self.max_inter= max_inter
        self.tolerancia= tolerancia

    def calulo(self, x0):
        x= x0
        for i in range(self.max_inter):
            f_x= self.evaluar(x)
            if abs(f_x) < self.tolerancia:
                print(f"Convergio en {i} interaciones.")
                return x
            f_prima_x= self.derivada().evaluar(x)
            if f_prima_x == 0:
                print("Error: Derivada cero. No se puede continuar.")
                return None
            x = x - f_x / f_prima_x
        return x
    def calcular_todas_raices(self, x0s):
        resultados=[]
        for x0 in x0s:
            resultados.append(self.calulo(x0))
        return resultados
    
    def agrupar_raices(self, raices):
        grupos= []
        for r in raices:
            found = False
            for g in grupos:
                if abs(r-g) < self.tolerancia:
                    found = True
                    break
            if not found:
                grupos.append(r)
        return grupos
    
    def encontrar_raices(self, valores_iniciales):
        raices = self.calcular_todas_raices(valores_iniciales)
        raices_unicas = self.agrupar_raices([r for r in raices if r is not None])
        return raices_unicas 


if __name__ == "__main__":
    grado = 3
    coef = [1, 0, 0, -1]

    solver = Newton_Method(grado, coef, max_inter=100, tolerancia=1e-8)

    valores_iniciales = [0.1, -0.5, 2, -2, 1j, -1j]

    raices = solver.encontrar_raices(valores_iniciales)
    print("Raíces aproximadas:", raices)

