def fatorial(n):
    return 1 if n == 0 else n * fatorial(n - 1)

print("Digite 0 para parar.")
p = -1
while p != 0:
    p = int(input("n: "))
    print(fatorial(p))  
