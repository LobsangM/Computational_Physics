import yaml
import pandas as pd
from derivada import Polynomial, derivative_definition, derivative_central, derivative_forward
from newton import NewtonMethod

def ejecutar_derivadas(config):
    coeffs = config["polynomial"]["coefficients"]
    points = config["points"]
    h = float(config["h"])

    p = Polynomial(coeffs)

    data = []
    for x in points:
        exact = p.derivative_exact(x)
        defin = derivative_definition(p, x, h)
        central = derivative_central(p, x, h)
        forward = derivative_forward(p, x, h)
        data.append([x, exact, defin, central, forward])

    df = pd.DataFrame(data, columns=["x", "Derivada exacta", "Definición", "Central", "Adelante"])
    print("\nResultados de derivadas numéricas:\n")
    print(df)

def ejecutar_newton(config):
    grado = config["newton"]["grado"]
    coefs = [float(c) for c in config["newton"]["coefficients"]]
    initial_guesses = [complex(x) for x in config["newton"]["initial_guesses"]]
    max_iter = int(config["newton"]["max_iter"])
    tol = float(config["newton"]["tolerance"])

    solver = NewtonMethod(grado, coefs, max_inter=max_iter, tolerancia=tol)
    raices = solver.encontrar_raices(initial_guesses)

    print("\nRaíces encontradas con método de Newton:\n")
    print(raices)
    

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)

    ejecutar_derivadas(config)
    ejecutar_newton(config)

if __name__ == "__main__":
    main()


