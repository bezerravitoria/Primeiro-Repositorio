from tictactoe import Velha

tabela = [['   ', '   ', '   '], ['   ', '   ', '   '], ['   ', '   ', '   ']]
vencedor = False
jogadas = 0

jogo = Velha(tabela)
jogo.imprime_tela(tabela)

while not vencedor and jogadas <= 9:
    jogo.joga_x(tabela)
    jogo.imprime_tela(tabela)
    vencedor = jogo.verifica_horizontal(tabela)
    if not vencedor:
        vencedor = jogo.verifica_vertical(tabela)
        if not vencedor:
            vencedor = jogo.verifica_diagonal(tabela)
            if vencedor or jogadas > 9:
                break

    jogo.joga_o(tabela)
    jogo.imprime_tela(tabela)
    vencedor = jogo.verifica_horizontal(tabela)
    if not vencedor:
        vencedor = jogo.verifica_vertical(tabela)
        if not vencedor:
            vencedor = jogo.verifica_diagonal(tabela)

if not vencedor:
    print('Fim de Jogo. Velha')