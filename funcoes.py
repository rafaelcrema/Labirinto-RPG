import personagem, random, time


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
        personagem.dic_npc['Vida'] = personagem.dic_npc['Vida'] - porrada_p

        print(f'Dano: {porrada_p}')
        print(f'Vida do inimigo: {personagem.dic_npc['Vida']}')
        time.sleep(1)

        #PORRADA DO NPC
        time.sleep(1)
        porrada_n = personagem.dic_npc['Força'] * random.randint(1,6)
        personagem.dic_player['Vida'] = personagem.dic_player['Vida'] - porrada_n

        print(f'Dano NPC: {porrada_n}')
        print(f'Vida do persongem: {personagem.dic_player['Vida']}')
        time.sleep(1)

        if personagem.dic_npc['Vida'] <= 0:
                        print('Inimigo vencido')
                        break
            
        elif personagem.dic_player['Vida'] <= 0:
            print('Game Over')
            break
    