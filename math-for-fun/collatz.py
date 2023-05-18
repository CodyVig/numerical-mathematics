"""
(This is a comment.)

STEP 1:
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

STEP 2:
Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. 
Although it has not been proved yet (Collatz Problem), it is thought that all starting 
numbers finish at 1.

STEP 3:
Which starting number, under one million, produces the stopping time?

"""


# Step 1: Implement the Collatz algorithm
# Write a function.
def collatz(n):
    """
    (This is called a "doc string")
    Returns n/2 if n is even, else 3n+1
    """

    # x = 1     # An assignment
    # x == 1    # Checking if equality is true

    # Is n even?
    if n % 2 == 0:  # "n%2 == 0" means "is n divisible by 2?"
        # Do something
        # return n / 2 # This will return a FLOAT even if n is even.
        return n // 2  # This is INTEGER division and will always return an integer.
    else:
        # We know n is odd if it is not even.
        return 3 * n + 1


# Test the Collatz function
print("Collatz(13) =", collatz(13))


# Step 2: Keep applying the function until we get 1 as an output.
# Write a new function that does this for any input n.
def stopping_time(n):
    """
    This computes the stopping time for the Collatz sequence.
    """

    stop_time = 0  # Initialize "stop_time" for use later.

    # We could do this by hand...
    # if collatz(n) == 1:
    #     return stop_time
    # n = collatz(n)
    # stop_time = 1
    # if collatz(n) == 1:
    #     return stop_time
    # n = collatz(n)
    # stop_time = 2
    # if collatz(n) == 1:
    #     return stop_time

    # Instead, we'll use a loop.
    # If you know the end goal, use a while loop.
    # If you know the number of times you need to iterate, use a for loop.
    while n != 1:
        n = collatz(n)  # Run the algorithm once
        stop_time = stop_time + 1  # Increment the stop time.

    return stop_time


# Test stopping_time()
print("Stopping time =", stopping_time(13))

# Step 3: Find the largest stopping time
max_stop_time = 0  # Initialize "max_stop_time" for use later.
max_number = 0  # Use this to keep track of which number causes the max stop time.
# list_of_max_numbers = []

for n in range(1, 10**6):  # 10**6 means 10^6 = 1,000,000
    stop_time = stopping_time(n)
    if stop_time > max_stop_time:
        max_stop_time = stop_time
        max_number = n
        # list_of_max_numbers.append(n)

# Print the results!
print("The max stop time =", max_stop_time)
print("This was caused by the number", max_number)
