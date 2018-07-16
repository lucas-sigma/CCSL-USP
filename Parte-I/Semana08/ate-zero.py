i = -1
x = []
while i != 0:
    i = int(input("0 -> Para a aplicação | Digite um número inteiro: "))
    x.append(i)

x.pop()
n = len(x)
while n > 0:
    print(x[n - 1], end=", ")
    n -= 1