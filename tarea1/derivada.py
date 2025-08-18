import numpy as np
import pandas as pd

# Functor para representar polinomios
class Polynomial:
    def __init__(self, coefficients):
         self.coefficients = coefficients           # coefficients: lista [a0, a1, a2, ...] que representa a0 + a1*x + a2*x^2 + ...
        

    def __call__(self, x):
        """Evalúa el polinomio en x."""
        return sum(c * (x**i) for i, c in enumerate(self.coefficients))

    def derivative_exact(self, x):
        """Derivada exacta del polinomio evaluada en x."""
        return sum(i * c * (x**(i-1)) for i, c in enumerate(self.coefficients) if i > 0)

def derivative_definition(f, x, h=1e-5):
    return (f(x+h) - f(x)) / h

def derivative_central(f, x, h=1e-5):
    return (f(x+h) - f(x-h)) / (2*h)

def derivative_forward(f, x, h=1e-5):
    return (-3*f(x) + 4*f(x+h) - f(x+2*h)) / (2*h)