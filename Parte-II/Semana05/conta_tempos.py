import time, random, ordenador, ordenador_melhorado

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        #o = ordenador.Ordenador()
        o = ordenador_melhorado.Ordenador()

        print("Comparando com listas aleatórias.")
        antes = time.time()
        #o.bubble_sort(lista1)
        o.bubble_short(lista1)
        depois = time.time()
        print('Bolha curta demorou ', depois - antes)

        antes = time.time()
        o.selecao_direta(lista1)
        depois = time.time()
        print('Seleção direta demorou ', depois - antes)

        print("\nComparando com listas quase ordenadas.")
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]
        antes = time.time()
        o.bubble_short(lista1)
        depois = time.time()
        print('Bolha curta demorou ', depois - antes)

        antes = time.time()
        o.selecao_direta(lista1)
        depois = time.time()
        print('Seleção direta demorou ', depois - antes)
