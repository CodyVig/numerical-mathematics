"""
Numerical ODE Solver
"""

from typing import Callable

def rk4(
        f: Callable[[float, float], float], 
        h: float, 
        x0: float, 
        y0: float, 
        xf: float
    ) -> float:
    """
    Uses Fourth Order Runge-Kutta method to solve y' = f(x, y) for y = y(x)
    at x = xf given the initial condition y(x0) = y0 using step size h.
    """
    number_of_steps = (xf - x0) / h
    if (not number_of_steps.is_integer()):
        raise ValueError(
            f"h = {h} must divide xf - x0 = {xf - x0}."
        )
    
    # Floating point rounding is causing problems. Round to number of digits in h:
    decimal_length = len(str(h).split(".")[1])

    x = x0
    y = y0
    half_h = 0.5*h
    while x < xf:
        k1 = f(x, y)
        k2 = f(x + half_h, y + half_h * k1)
        k3 = f(x + half_h, y + half_h * k2)
        k4 = f(x + h, y + h * k3)
        y += h / 6 * (k1 + 2*k2 + 2*k3 + k4)
        x = round(x + h, decimal_length)
    return y

# Example 1 in Zill, section 9.2
print(
    rk4(
        f = lambda x, y: 2*x*y,
        h = 0.1,
        x0 = 1,
        y0 = 1,
        xf = 1.5
    )
)

# # Approximation for e.
# print(
#     rk4(
#         f = lambda x, y: y,
#         h = 0.05,
#         x0 = 0,
#         y0 = 1,
#         xf = 1
#     )
# )