import yaml
import pandas as pd
from derivada import Polynomial, derivative_definition, derivative_central, derivative_forward

def main():
    #Abrir la confirguración
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)

        coefficients = config['polynomial']['coefficients']
        points = config['points']
        h = float(config['h'])

        #Crear un polinomio
        p = Polynomial(coefficients)

        #Tabla de resultados
        data = []
        for x in points:
            row = {
                'x': x,
                'f(x)': p(x),
                'Exacta': p.derivative_exact(x),
                'Por Definición': derivative_definition(p, x, h),
                'Central': derivative_central(p, x, h),
                'Adelante': derivative_forward(p, x, h)
            }
            data.append(row)
        df = pd.DataFrame(data)

        print(df)

if __name__ == "__main__":
    main()