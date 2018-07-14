def fatorial(n):
    return 1 if n == 0 else n * fatorial(n - 1)

def binomial(n, k):
    return fatorial(n) // (fatorial(k) * (fatorial(n - k)))
