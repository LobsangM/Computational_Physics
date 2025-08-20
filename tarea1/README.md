# Tarea: Derivadas numéricas con Functors en Python

En esta tarea vamos a resolver problemas matemáticos relacionados con polinomios y raíces utilizando **métodos numéricos**. En particular, se implementaron:

1. **Clase `Polinomio`** → permite evaluar polinomios en un punto dado.  
2. **Derivadas** → cálculo de la derivada de un polinomio.  
3. **Método de Newton-Raphson** → búsqueda de raíces de polinomios con un criterio de tolerancia y número máximo de iteraciones.  

Se hace uso de **functores en Python**, lo que permite que los objetos definidos se comporten como funciones.

---

## 🔹 Functores en Python
En Python, un **functor** es un objeto que puede ser llamado como una función. Esto se logra implementando el método especial `__call__`.  

### Tipos de Functors

1. Functores simples → Implementan __call__ para ejecutar una operación directa.
2. Functores con estado → Guardan información entre invocaciones.
3. Functores parametrizados → Permiten ajustar su comportamiento según parámetros iniciales.
