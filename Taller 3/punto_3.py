# Ejecutar fórmula para calcular ganancia con interés compuesto
import math

def formula_int_comp(P, n, r, t):
    A = P * (1 + (r / n )) ** (n * t)
    return A

t = input("> Ingrese el numero de años: ")
t = float(t)

valor_final = round(formula_int_comp(10000, 12, 0.08, t), 2)
valor_final = str(valor_final)
print("> El valor fina es de: " + valor_final)