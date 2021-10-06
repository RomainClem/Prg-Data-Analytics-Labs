import tools


# Fibonacci recursive
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


# Check if prime recursively
def prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    elif n % i == 0:
        return False
    elif i * i > n:
        return True

    return prime(n, i + 1)
