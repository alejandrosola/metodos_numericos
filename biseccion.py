import sympy as smp
from sympy.calculus.util import continuous_domain

ITERACIONES = 10000
TOLERANCIA = 0.1e-3

x = smp.symbols("x")

locals = {
    "e": smp.E,
    "cos": smp.cos,
    "abs": smp.Abs,
    "sin": smp.sin,
    "tan": smp.tan,
    "acos": smp.acos,
    "asin": smp.asin,
    "atan": smp.atan,
    "ln": smp.ln,
    "log": smp.log,
    "pi": smp.pi,
    "sqrt": smp.sqrt,
    "diff": smp.diff,
}


# Pedir la función al usuario
expresion = input("Ingrese la función f(x): ")
# Intentar parsear la expresión
try:
    f = smp.sympify(expresion, evaluate=False, locals=locals)
except smp.SympifyError:
    print("Error al parsear la función. Asegúrese de ingresar una expresión válida.")
    exit()


def is_continuous_on_interval(f, x, a, b):
    return continuous_domain(f, x, smp.Interval(a, b)).is_Interval


def biseccion(funcion, a, b):
    """
    Algoritmo de bisección o búsqueda binaria para encontrar una raíz de
    una función dentro del intervalo [a, b]
    """
    i = 0

    fa = round(funcion.evalf(subs={x: a}), 15)

    while i < ITERACIONES:
        p = a + (b - a) / 2  # Calcular p-i
        fp = round(funcion.evalf(subs={x: p}), 15)

        # Si se encontró la raiz (o cercana) devolver p
        if smp.Abs(fp) < TOLERANCIA:
            return p

        i += 1
        # Seguir buscando por izq o derecha
        if smp.sign(fa) * smp.sign(fp) > 0:
            a = p
            fa = fp
        else:
            b = p

    return None


try:
    a = float(input("Ingrese a: "))
    b = float(input("Ingrese b: "))
    if a <= b:
        ok = True
    else:
        ok = False
        print("Ingrese un intervalo válido")
except ValueError:
    print("Ingrese un número válido")
    ok = False


# if not continuous_domain(f, x, smp.Interval(a, b)).is_Interval:
if not is_continuous_on_interval(f, x, a, b):
    ok = False
    print(f"La función {f} no es continua en [{a}, {b}]")

if not smp.Interval(a, b).intersect(
    continuous_domain(f, x, smp.Interval(a, b))
) == smp.Interval(a, b):
    ok = False
    print(f"La función {f} no está definida en [{a}, {b}]")

""" if smp.sign(f.evalf(subs={x: a})) * smp.sign(f.evalf(subs={x: b})) > 0:
    ok = False
    print(
        f"f({a}) y f({b}) tienen el mismo signo, no hay raíz en el intervalo [{a}, {b}]."
    ) """


if ok:
    res = biseccion(f, a, b)
    print(
        "Raíz de "
        + str(f)
        + " en el intervalo ["
        + str(a)
        + ", "
        + str(b)
        + "]: "
        + str(round(res, 10))
        if res is not None
        else "El método fracasó despues de " + str(ITERACIONES) + " N iteraciones"
    )
