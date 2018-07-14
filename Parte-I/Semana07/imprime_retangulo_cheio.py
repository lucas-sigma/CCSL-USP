l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
i = 0
j = 1

while i < a:
    while j < l:
        print("#", end="")
        j += 1
    print("#")
    i += 1
    j = 1
