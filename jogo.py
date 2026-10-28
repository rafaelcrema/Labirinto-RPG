import personagem,itens_bau
import funcoes
import random
import caminhos

nv_labirinto = 0

print('=== CAVERNA DO DRAGÃO ==='.center(60))

while True:

    funcoes.verifica()

    print('======= MENU ======='.center(60))

    escolha = input('''
[1] Personagem
[2] Inventarios
[3] Iniciar
[4] Sair
''').strip()

#VERIFICA DADOS DO PERSONAGEM
    if escolha == '1':
        for info, dados in personagem.dic_player.items():
            print(f'{info}: {dados}')

#VERIFICA INVENTARIOS DO PERSONAGEM           
    if escolha == '2':
        funcoes.verificar_inventario()

    if escolha == '3':
        while True:
            print(f'======= LABIRINTO NIVEL {nv_labirinto} ======='.center(60))

            jogada = random.choice(caminhos.caminho)
            print(f'Você encontou: {jogada}')

            if jogada == 'Bau':
                itens_bau.bau()

            
            elif jogada == 'Batalha':

                print('[1] Batalhar')
                print('[2] Fugir')
                print('[3] Inventario')

                opcao = input('Oque vdeseja fazer?...')

                if opcao == '1':
                    funcoes.batalha()
                    
                elif opcao == '2':
                    print('fugir')
                elif opcao == '3':
                    funcoes.verificar_inventario()

            elif jogada == 'Loja':
                print('[1] Comprar Item')
                print('[2] Ignorar Loja')
                print('[3] Inventario')

                opcao = input('Oque vdeseja fazer?...')

                if opcao == '1':
                    print('Abrir loja')
                elif opcao == '2':
                    print('Ignorar loja')

            nv_labirinto += 1

            if nv_labirinto > 10:
                break

    
    if escolha == '4':
        break
    