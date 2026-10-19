import personagem

print('=== CAVERNA DO DRAGÃO ==='.center(60))

while True:

#VERIFICAÇÃO DE ITENS E DADOS
    for itens, dados in personagem.inventario.items():
        if isinstance(dados, dict):
            for nome_equipe, bonus in dados.items():
                if itens == 'Espada':
                    personagem.dic_player['Força'] += bonus

                if itens in ['Capacete', 'Peitoral', 'Calça', 'Bota', 'Escudo']:
                    personagem.dic_player['Armadura'] += bonus




    print('======= MENU ======='.center(60))

    escolha = input('''
[1] Personagem
[2] Inventarios
[3] Avançar
[4] Sair
''').strip()


    if escolha == '1':
        for info, dados in personagem.dic_player.items():
            print(f'{info}: {dados}')
    
    if escolha == '4':
        break
    