from typing import Callable # Type hints for functions
from math import sin, cos

def newtons_method(
        f: Callable[[float], float], 
        initial_guess: float = 0.0, 
        tol: float = 10**(-10)
    ) -> float:
    """
    Implements Newton's Method to find a root of a function f.
    x[n+1] = x[n] - f(x[n]) / f'(x[n])
    """

    x = initial_guess
    print("x0 =", x)
    counter = 0

    while (abs(f(x)) > tol): 
        x = do_newton(f, x)
        counter += 1
        print(f"x{counter} =", x)
    return x

def do_newton(f: Callable[[float], float], x: float):
    f_prime = derivative(f)
    return x - (f(x) / f_prime(x))

def derivative(f: Callable[[float], float]) -> float:
    def compute_derivative(x: float, dx = 10**(-5)) -> float:
        """
        Numerically approximates the derivative of f. 
        """
        return (f(x + dx) - f(x)) / dx
    return compute_derivative

### Test Newton's method ###

def func(x: float) -> float:
    return cos(sin(cos(x))) - sin(cos(sin(x)))

print( 
    newtons_method(func, 2)
)