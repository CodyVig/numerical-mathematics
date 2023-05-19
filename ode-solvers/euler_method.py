"""
Euler's Method
"""

from typing import Callable


def euler_method(
    f: Callable[[float, float], float],
    x0: float,
    y0: float,
    xf: float,
    h: float = 0.1,
    verbose: bool = True,
) -> float:
    """
    Uses Euler's Method to approximate the solution y = y(x) to y' = f(x, y)
    at x = xf given the inital condition y(x0) = y0.
    """

    number_of_iterations = (xf - x0) / h
    if not number_of_iterations.is_integer():
        raise ValueError(f"h = {h} needs to divide xf - x0 = {xf - x0}.")
    # Floating point rounding is causing problems.
    # Round to number of digits in h:
    n = len(str(h).split(".")[1])

    x = x0
    y = y0

    while x != xf:
        y = y + h * f(x, y)
        x = round(x + h, n)
        if verbose:
            print(f"x = {x}")
            print(f"y = {y}\n")
    return y


# # Example 1 in Section 2.6 in Zill's ODE text, 10th edition
# print(
#     euler_method(
#         f = lambda x, y: 0.1*(y)**(1/2) + 0.4*(x)**2,
#         x0 = 2,
#         y0 = 4,
#         xf = 2.5,
#         h = 0.05
#     )
# )

# # A very bad approximation of e.
# print(
#     euler_method(
#         f = lambda x, y: y,
#         x0 = 0,
#         y0 = 1,
#         xf = 1,
#         h = 0.0005
#     )
# )
