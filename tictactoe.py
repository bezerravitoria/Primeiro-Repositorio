class Velha:

    def __init__(self, tabela):
        self.tabela = tabela


    def imprime_tela(self, tabela):
        print('  1    2    3')
        for i in range(3):
            print(i + 1, '|'.join(tabela[i]))
            if i < 2:
                print('  ___________')


    def joga_x(self, tabela):
        print('Vez de X')
        vez_de_x = True

        while vez_de_x:
            try:
                linha = int(input('Digite a linha:')) - 1
                coluna = int(input('Digite a coluna:')) - 1

                if tabela[linha][coluna] != ' X ' and tabela[linha][coluna] != ' O ':
                    tabela[linha][coluna] = ' X '
                    vez_de_x = False

                else:
                    print('Posição já preenchida')

            except:
                print('Posição inválida')


    def joga_o(self, tabela):
        print('Vez de O')
        vez_de_o = True

        while vez_de_o:
            try:
                linha = int(input('Digite a linha:')) - 1
                coluna = int(input('Digite a coluna:')) - 1

                if tabela[linha][coluna] != ' O ' and tabela[linha][coluna] != ' X ':
                    tabela[linha][coluna] = ' O '
                    vez_de_o = False

                else:
                    print('Posição já preenchida')

            except:
                print('Posição inválida')


    def verifica_horizontal(self, tabela):
        simbolos = [' X ', ' O ']

        for s in simbolos:
            for i in tabela:
                if i == [s, s, s]:
                    print('Fim de Jogo.', s, 'ganhou')
                    return True


    def verifica_vertical(self, tabela):

        simbolos = [' X ', ' O ']

        for s in simbolos:
            linha = coluna = 0
            soma = 0

            while linha < 3 and coluna < 3:
                if tabela[linha][coluna] == s:
                    soma += 1
                    linha += 1
                else:
                    linha = 0
                    coluna += 1
                    soma = 0

            if soma == 3:
                print('Fim de Jogo.', s, 'ganhou')
                return True


    def verifica_diagonal(self, tabela):
        simbolos = [' X ', ' O ']

        for s in simbolos:
            soma = 0

            for i in range(3):
                if tabela[i][i] == s:
                    soma += 1

            if soma == 3:
                print('Fim de Jogo.', s, 'ganhou')
                return True

            else:
                soma = 0

            j = 2
            for i in range(3):
                if tabela[i][j] == s:
                    soma += 1
                j -= 1

            if soma == 3:
                print('Fim de Jogo.', s, 'ganhou')
                return True
