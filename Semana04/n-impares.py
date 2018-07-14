n = int(input("Digite o valor de n: "))

def impar(n):
    i = 1
    while i <= n:
        if i % 2 == 1:
            print(i)
        else:
            n += 1
        i += 1
        
impar(n)
