def carregando_ranking(sheet):
    lista_completa = []
    # limita a quantidade de linhas que queremos olhar na planilha
    for row in sheet.iter_rows(min_row=2, max_row=12):
        # e as coloca em uma lista para futuras alterações
        rank = []
        for cell in row:
            rank.append(cell.value)
        lista_completa.append(rank)

    return lista_completa


def caucular_rank(resposta_certas, perguntas_respondidas):
    # Caucula o rank baseado nas perguntas respondidas com as perguntas acertadas
    rank = (resposta_certas * 100) / perguntas_respondidas
    return round(rank)


def alterando_ranking(lista_rank, lista_usuario):
    # Verificando na lista, se o usuario possui um pontuação maior ou igual a de algum outro jogador
    for r in range(0, 11):
        # e se for, o usuario irá pegar o seu lugar no ranking
        if lista_rank[r][2] <= lista_usuario[1]:
            lista_usuario.insert(0, lista_rank[r][0])
            lista_rank.insert(r, lista_usuario)
            break
    organizando_ranking(lista_rank)


def organizando_ranking(rank):
    # simplesmente re organiza o ranking com as posiçoes alteradas
    for r in range(0, 11):
        rank[r][0] = f'{r + 1}º'


def alterando_ranking_planilha(sheet, lista_rank, book):
    # anda por todas as linhas importantes da planilha
    for r in range(2, 12):
        # serve para pegar as celulas de cada coluna
        for c in range(0, 3):
            # troca esse valores por novos
            cell = sheet.cell(row=r, column=c + 1)
            cell.value = lista_rank[r - 2][c]
    # após isso salva
    book.save('C:\\Users\\asss1\\OneDrive\\Área de Trabalho\\Projeto do jogo\\Quiz_Copa_do_Mundo\\Pasta1.xlsx')


def printando_ranking(rank):
    print(F'{"RANKING":>7} - {"NOME":^10} - {"PONTOS":^5}')
    cont = 0
    for r in rank:
        if cont != 10:
            print(f'{r[0]:>7} - {r[1]:^10} - {r[2]:^5}')
            cont += 1

        else:
            break
