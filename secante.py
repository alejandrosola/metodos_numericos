import sympy as smp
from sympy.calculus.util import continuous_domain

ITERACIONES = 100000
TOLERANCIA = 0.1e-3

x = smp.symbols("x")

# f = x - ((x**3 + 4 * x**2 - 10) / (3 * x**2 + 8 * x))
# f = x**3 + 4 * x**2 - 10
# f = x + 2
f = smp.cos(x) - x


def metodo_secante(f, p0, p1):
    # p0 y p1 son las aproximaciones iniciales
    i = 0
    q0 = smp.N(f.evalf(subs={x: p0}), 5)
    q1 = smp.N(f.evalf(subs={x: p1}), 5)
    while i < ITERACIONES:
        p = p1 - (q1 * (p1 - p0)) / (q1 - q0)
        if smp.Abs(p - p1) < TOLERANCIA:
            return p
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = smp.N(f.evalf(subs={x: p}), 5)


print(metodo_secante(f, 0.5, 4))
