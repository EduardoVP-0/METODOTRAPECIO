import sympy as sp
import matplotlib.pyplot as mtp
import numpy as np

expresion = input("Introduce la funcion en terminos de x ( +, -, *, /, **, (, ) ):" )
x = sp.symbols('x')

#PASAMOS LA EXPRESION QUE METIMOS A UN LENGUAJE DE LA LIBRERIA
funcion = sp.sympify(expresion)
#CALCULAMOS LA SEGUNDA DERIVADA DE LA FUNCION
derivada1 = sp.diff(funcion, x)
derivada2 = sp.diff(derivada1, x)

a = float(input("Introduce el valor de 'a': "))
b = float(input("Introduce el valor de 'b': "))

#PASO 1
funcion_a = funcion.subs(x, a)
funcion_b = funcion.subs(x, b)

#PASO 2 Y 3
a_curva = ((b - a)/2) * (funcion_a + funcion_b)

#PASO 4
e = b - a
derivada2_e = derivada2.subs(x, e)
error = -(1/12) * derivada2_e * (b-a)**3

a_total = a_curva + error

print(f"El area bajo la curva es igual a: {a_curva}")

if error == 0:
    print("Es una funcion lineal y su error es 0")
else:
    print(f"El error es igual a: {error}")

print(f"El area total bajo la curva es igual a: {a_total}")

x_vals1 = np.linspace(a-0.5, b+0.5, 100) # Valores de x para la funcion
y_vals1 = [funcion.subs(x, val) for val in x_vals1]

x_vals = np.linspace(a, b, 100)  # Valores de 'x' para el trapecio
y_vals = [float(funcion.subs(x, val)) for val in x_vals]  # Valores de 'y' correspondientes

mtp.scatter([a],[funcion_a],color="red")
mtp.scatter([b],[funcion_b],color="red")
mtp.plot(x_vals1, y_vals1,label='Funcion')
mtp.plot(x_vals, y_vals,label='Trapecio')
mtp.plot([a, b], [funcion_a, funcion_b], linestyle='--', color='blue')
mtp.fill_between(x_vals, 0, y_vals, where=(x_vals >= a) & (x_vals <= b), alpha=0.5, color='gray', label='Área Total')
mtp.title("Gráfica de la Función")
mtp.xlabel("x")
mtp.ylabel("f(x)")
mtp.legend()
mtp.grid()

mtp.show()