n = int(input("Digite o valor de n: "))

if n < 0:
    print("Digite apenas números positivos!")
elif n == 2:
    print("Primo.")
elif n % 2 == 1:
    print("Primo.")
else:
    print("Não é primo.")
