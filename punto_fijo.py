import sympy as smp

ITERACIONES = 1000
TOLERANCIA = 0.1e-2
x = smp.symbols("x")


# f = (x**2 - 1) / 3
# f = x - x**3 - 4 * x**2 + 10
f = x - ((x**3 + 4 * x**2 - 10) / (3 * x**2 + 8 * x))


def punto_fijo(f):
    # Aproximación inicial
    aproximacion = 1.5
    i = 1
    while i <= ITERACIONES:
        p = smp.N(f.evalf(subs={x: aproximacion}), 5)
        if smp.Abs(p - aproximacion) < TOLERANCIA:
            return p
        i += 1
        aproximacion = p
    return (p, aproximacion)


print(punto_fijo(f))
