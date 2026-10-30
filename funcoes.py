import personagem, random, time, caminhos


#VERIFICAÇÃO DE ITENS E DADOS
def verifica():
    for itens, dados in personagem.inventario.items():
        if isinstance(dados, dict):
            for nome_equipe, bonus in dados.items():
                if itens == 'Espada':
                    personagem.dic_player['Força'] += bonus

                if itens in ['Capacete', 'Peitoral', 'Calça', 'Bota', 'Escudo']:
                    personagem.dic_player['Armadura'] += bonus

#VERIFICA INVENTARIOS DO PERSONAGEM
def verificar_inventario():
    for item, dado in personagem.inventario.items():
        if isinstance (dado, dict):
            for descricao, poder in dado.items():
                print(f'{item}: {descricao} | Poder: {poder}')

#SISTEMA DE BAU
def bau():

    while True:
        print('[1] Abrir')
        print('[2] Inventario')
        print('[3] Personagem')
        print('[4] Ignorar')

        opcao = input('Oque vdeseja fazer?...')

        if opcao == '1':
            sortiado = random.choice(list(caminhos.bau_inicial.keys()))
            item = caminhos.bau_inicial[sortiado]
            print(f'Você encontrou: {sortiado}')

            if isinstance(item, dict):
                for descricao, poder in item.items():
                    print(f'{descricao} | Poder: {poder}')

            else:
                print(f'Valor: {item}')

            coletar = input('Deseka pegar o item?[S/N]\n>>').strip().upper()
            if coletar == 'S':

                #POÇÃO
                if sortiado == 'Poção de HP':
                    personagem.inventario['Poção de vida'].append(item)
                    print('Poção adicionada ao inventario!')

                elif sortiado == 'Moeda':
                    personagem.dic_player['Moeda'].append(item)
                    print('Modeda adicionada ao inventario.')

                #armaduras e armas
                else:
                    personagem.inventario[sortiado] = item
                    print(f'{sortiado} equipado!')

            break

        elif opcao == '2':
            verificar_inventario()
            print()

        elif opcao == '3':
            for info, dados in personagem.dic_player.items():
                print(f'{info}: {dados}')
            print()
        

        elif opcao == '4':
            print('Você ignorou o Bau')
            break


#O NOME DA FUNÇÃO JÁ DIZ TUDO KKKKK
def batalha():

    while True:
        print('Inimigo')
        for item, dado in personagem.dic_npc.items():
            print(f'{item}: {dado}')

        print()

        print('Seu personagem')
        for p_item, p_dado in personagem.dic_player.items():
            print(f'{p_item}: {p_dado}')

        print()

        #PORRADA DO PLAYER
        time.sleep(1)
        porrada_p = personagem.dic_player['Força'] * random.randint(1,20)
        personagem.dic_npc['Vida'] -= porrada_p

        print(f'Dano: {porrada_p}')
        print(f'Vida do inimigo: {personagem.dic_npc['Vida']}')
        time.sleep(1)

        #PORRADA DO NPC
        time.sleep(1)
        porrada_n = personagem.dic_npc['Força'] * random.randint(1,6)
        personagem.dic_player['Vida'] -= porrada_n

        print(f'Dano NPC: {porrada_n}')
        print(f'Vida do persongem: {personagem.dic_player['Vida']}')
        time.sleep(1)

        if personagem.dic_npc['Vida'] <= 0:
            print('Inimigo vencido')
            break
            
        elif personagem.dic_player['Vida'] <= 0:
            print('Game Over')
            break


#LOJA
def lojinha():
    print('======== LOJA ========')

    while True:
        for nome, dados in personagem.itens_loja.items():
            print(f'{nome} | Poder: {dados['Poder']} | Moedas: {dados['Moedas']}')

        print()
        escolha_loja = input('''Deseja comprar algum item?
'Espada longa'    [1]
'Machado duplo'   [2]
'Poção de vida M' [3]
'Poção de vida G' [4]
        ''')

        opcoes_loja = {
            '1': 'Espada longa',
            '2': 'Machado duplo',
            '3': 'Poção de vida M',
            '4': 'Poção de vida G'
        }

        if escolha_loja in opcoes_loja:
            item_escolhido = opcoes_loja[escolha_loja]
            print(f'\nVocê escolheu: {item_escolhido}')

            for dado, valor in personagem.itens_loja[item_escolhido].items():
                print(f'{dado}: {valor}') 

        comprar = input('Comprar? [S/N]').strip().upper()

        if comprar == 'S':
            if opcoes_loja in ['Poção de vida M', 'Poção de vida G']:
              poder = personagem.itens_loja[item_escolhido]['Poder']
              personagem.inventario['Poção de vida'].append(poder)

            elif item_escolhido in ['Espada longa', 'Machado duplo']:
                personagem.inventario['Arma'] = item_escolhido

        print(f'Você comprou o item: {opcoes_loja[escolha_loja]}')

        break