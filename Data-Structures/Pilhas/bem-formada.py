def main():
    # Teste:
    exp1 = '(([]))'
    exp2 = '([)]'

    print(exp1, ' resultado: ', bem_formada(exp1))
    print(exp2, ' resultado: ', bem_formada(exp1))
    
def bem_formada(s):
    # Empilhar:
    pilha = []
    for i in s:
        pilha.append(i)

    # Desempilhar:
    while len(pilha) > 0:
        topo = pilha.pop()
        if topo == ')':
            topo = pilha.pop()
            if topo == ']':
                topo = pilha.pop()
                if topo == '[':
                    topo = pilha.pop()
                    if topo == '(':
                        return True
            elif topo == '(':
                return True
                

main()
