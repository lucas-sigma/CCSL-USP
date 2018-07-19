def main():
    carro1 = Carro('Brasília', 1968, 'amarela', 80)
    carro2 = Carro('Fuscão', 1981, 'preto', 95)

    carro1.acelere(40)
    carro1.acelere(80)
    carro1.pare()

    carro2.acelere(50)
    carro2.acelere(100)


class Carro:
    # Construtor
    def __init__(self, modelo, ano, cor, velocidadeMaxima):
        self.modelo = modelo
        self.ano    = ano
        self.cor    = cor
        self.vel    = 0
        self.maxV   = velocidadeMaxima  # velocidade máxima

    # Outros Métodos
    def imprima(self):
        if self.vel == 0:  # parado da para ver o ano
            print('%s %s %d' %(self.modelo, self.cor, self.ano))
        elif self.vel < self.maxV:
            print('%s %s indo a %d Km/h' %(self.modelo, self.cor, self.vel))
        else:
            print('%s %s indo muito rápido!' %(self.modelo, self.cor))

    def acelere(self, velocidade):
        self.vel = velocidade
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()


main()
            
