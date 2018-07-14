l = int(input("Digite a largura: "))
a = int(input("Digite a altura: "))
i = 0
j = 1

while i < a:
    while j < l:
        if i > 0 and i < a - 1 and j > 1 and j < l:
            print(" ", end="")
        else:
            print("#", end="")
        j += 1
    print("#")
    i += 1
    j = 1
