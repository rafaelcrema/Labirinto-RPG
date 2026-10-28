import personagem,caminhos,random,funcoes

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
            funcoes.verificar_inventario()
            print()

        elif opcao == '3':
            for info, dados in personagem.dic_player.items():
                print(f'{info}: {dados}')
            print()
        

        elif opcao == '4':
            print('Você ignorou o Bau')
            break
