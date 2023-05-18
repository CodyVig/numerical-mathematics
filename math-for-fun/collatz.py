"""
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

def collatz(n: int) -> int:
    """
    Runs the Collatz algorithm
    """
    return n//2 if n % 2 == 0 else 3 * n + 1

def collatz_stop_time(n: int) -> int:
    """
    Returns the number of iterations required to halt the Collatz sequence
    """

    iterations = 0
    while n > 1:
        n = collatz(n)
        iterations += 1
    return iterations

def find_max_collatz_sequence(n: int = 10**6) -> dict:
    """
    For 1 <= k <= n, this runs the collatz sequence and determines the largest
    such sequence and its starting number k.
    """

    largest_squence = 0
    largest_starting = 0
    for k in range(1, n):
        sequence_length = collatz_stop_time(k)
        if sequence_length > largest_squence:
            largest_squence = sequence_length
            largest_starting = k
    return {largest_starting:largest_squence}

print(find_max_collatz_sequence())