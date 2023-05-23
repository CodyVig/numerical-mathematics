"""
Numerical Integration
"""

from typing import Callable


def simpson(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Uses Simpson's rule to approximate the integral of f from a to b, using
    n approximating parabolic rectangles.
    """

    # Make sure n is even
    n = n if n % 2 == 0 else n + 1

    delta_x = (b - a) / n
    simpson = f(a) + f(b)

    # Floating point rounding is causing problems.
    # Round to number of digits in delta_x:
    decimal_length = len(str(delta_x).split(".")[1])

    for i in range(1, n):
        x = round(a + i * delta_x, decimal_length)
        simpson += 2 * f(x) if i % 2 == 0 else 4 * f(x)

    return simpson * delta_x / 3


# # Example 4 in Stewart, section 7.7
# print(
#     simpson(
#         f = lambda x: 1/x,
#         a = 1,
#         b = 2,
#         n = 10
#     )
# )
