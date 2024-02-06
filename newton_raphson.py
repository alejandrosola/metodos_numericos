import sympy as smp

ITERACIONES = 1000
TOLERANCIA = 0.1e-5

x = smp.symbols("x")

# f = x - ((x**3 + 4 * x**2 - 10) / (3 * x**2 + 8 * x))
# f = x**3 + 4 * x**2 - 10
# f = x + 2
f = smp.cos(x) - x


def newton_raphson(f, aproximacion):
    i = 0
    while i < ITERACIONES:
        derivada = smp.diff(f)

        if smp.N(derivada.evalf(subs={x: aproximacion}), 5) == 0:
            raise Exception("f'(x) = 0")

        p = aproximacion - (
            smp.N(f.evalf(subs={x: aproximacion}), 5)
            / (smp.N(derivada.evalf(subs={x: aproximacion}), 5))
        )
        if smp.Abs(p - aproximacion) < TOLERANCIA:
            return p
        i += 1
        aproximacion = p
    return None


print(newton_raphson(f, 1.5))
