from functools import reduce

def get_digits(n: int) -> list[int]:
    digits = [n%10]
    k = 1
    while 10**k <= n:
        digits = [(n%10**(k+1) - n%10**k)//10**k] + digits
        k += 1
    return digits

def do_persistence(n: int) -> int:
    return reduce((lambda x, y: x * y), get_digits(n))

def persistence(n: int, verbose = False) -> int:
    """
    Returns the number of persistence iterations required
    to bring a number to a single digit
    """
    count = 0
    if verbose:
        print("Count", count, "| n =", n)
    while n >= 10:
        n = do_persistence(n)
        count += 1
        if verbose:
            print("Count", count, "| n =", n)
    return count

def most_persistent(n: int) -> dict:
    max_persistence = 0
    max_number = 0
    for k in range(1, n):
        potential_max = persistence(k)
        if potential_max > max_persistence:
            max_persistence = potential_max
            max_number = k
    return {max_number: max_persistence}

persistence(n=277777788888899, verbose=True)

# print(
#     most_persistent(10**7)
# )