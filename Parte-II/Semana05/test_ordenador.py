import ordenador_melhorado, pytest, conta_tempos

class TestaOrdenador:

    @pytest.fixture
    def o(self):
        return ordenador_melhorado.Ordenador()

    @pytest.fixture
    def lista_quase(self):
        c = conta_tempos.ContaTempos()
        return c.lista_quase_ordenada(100)

    @pytest.fixture
    def l_aleat(self):
        c = conta_tempos.ContaTempos()
        return c.lista_aleatoria(100)

    def esta_ordenada(self, l):
        for i in range(len(l) - 1):
            if l[i] < l[i + 1]:
                return False
        return True

    def test_bubble_short_aleat(self, o, l_aleat):
        o.bubble_short(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selecao_direta_aleat(self, o, l_aleat):
        o.selecao_direta(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_bubble_short_quase(self, o, l_quase):
        o.bubble_short(l_aleat)
        assert self.esta_ordenada(l_aleat)

    def test_selecao_direta_quase(self, o, l_quase):
        o.bubble_short(l_quase)
        assert self.esta_ordenada(l_quase)

