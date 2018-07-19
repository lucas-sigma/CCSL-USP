class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.a = ladoA
        self.b = ladoB
        self.c = ladoC

    def perimetro(self):
        return (self.a + self.b + self.c)

    def tipo_lado(self):
        a, b, c = self.a, self.b, self.c
        doisIguais = (a == b and b != c and a != c) or (a == c and a != b and b != c) or (b == c and b != a and c != a)
        tdIgual = a == b and b == c and a == c
        tdDiferente = a != b and b != c and a != c
        if doisIguais:
            return 'isósceles'
        elif tdIgual:
            return 'equilátero'
        return 'escaleno'

def main():
    t = Triangulo(3,4,5)
    print(t.perimetro())
    print(t.a)
    print(t.b)
    print(t.c)
    print(t.tipo_lado())
    t = Triangulo(3,3,3)
    print(t.tipo_lado())
    t = Triangulo(5,8,5)
    print(t.tipo_lado())
    t = Triangulo(5,5,6)
    print(t.tipo_lado())

main()
