from typing import Callable # Type hints for functions
from math import sin, cos

def bisection(
        f: Callable[[float], float], 
        a: float, 
        b: float, 
        tol: float = 10**(-10)
    ):
    """
    Runs the bisection algorithm until a root is found within tolerance.
    """

    c = a
    count = 0
    print("x0 =", c)
    while (abs(f(c)) > tol):
        c = do_bisect(f, a, b)
        count += 1
        print(f"x{count} =", c)

        fc = f(c) # Reduce function evaluation
        if f(a)*fc < 0:
            b = c
        elif fc*f(b) < 0:
            a = c
        else:
            return c
    return c

def do_bisect(f: Callable[[float], float], a: float, b: float) -> float:
    """
    Helper function to run one iteration of bisection.
    """

    if f(a)*f(b) > 0:
        raise ValueError(f"No roots in [{a}, {b}].")
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b
    return (a+b)/2

### Test bisection ###

def func(x: float) -> float:
    return cos(sin(cos(x))) - sin(cos(sin(x)))

print(
    bisection(func, 1, 3)
)