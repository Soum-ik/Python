# Define a module named fibonacci.py
def fib(n):
    # Return the nth Fibonacci number
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

import fibonacci

# Generate the first 10 Fibonacci numbers
for i in range(10):
    print(fibonacci.fib(i))
