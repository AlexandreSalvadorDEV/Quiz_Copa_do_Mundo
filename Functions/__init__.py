def remove_caracteres_indesejaveis(cellvalue):
    # função que remove caracteres indesejaveis de uma celula do excel
    import re
    text = re.sub(r"[\r\n\t\x07\x0b]", "", cellvalue)
    return text


def mostrar_pergunta_respostas(sheet, limite_perg):
    import re
    for value in sheet['A']:
        if value.value == limite_perg:
            # após achar a pergunta, é agr mostrado na tela.
            pergunta = sheet.cell(row=limite_perg + 1, column=2)
            print(f'\033[1;33m{limite_perg}º) {pergunta.value}\033[m')
            alternativas = sheet.cell(row=limite_perg + 1, column=3)
            # retira os caracteres indesejáveis
            alternativas_alterada = remove_caracteres_indesejaveis(alternativas.value)
            # Formata as alternativas
            alternativas_lista = re.split('[/]', alternativas_alterada)
            for alt in alternativas_lista:
                print(f"\n   {alt.replace(':', ')')}")
            print('')

        else:
            continue


def verificar_resposta(sheet, num_perg, rep):
    # verifica a resposta do usuario com a resposta correta
    resposta_correta = sheet.cell(row=num_perg + 1, column=4)
    # Determinando a dificuldade da pergunta, sendo ela dificil(2) ou facil(1)
    dificuldade = 0
    if 2 <= (num_perg + 1) <= 10:
        # Pergunta dificil
        dificuldade += 2
    elif 13 < (num_perg + 1) <= 25:
        # Pergunta facil
        dificuldade += 1

    return dificuldade if resposta_correta.value == rep else 0


def cadastro(sheet):
    # cadastro de usuario
    usuario = []
    # coleta de dados
    while True:
        nome_valido = 0
        nome = input('Cadastro de usuario: ').capitalize().strip()
        # loop para verificar se o usuario já foi cadastrado

        for n in sheet['A']:
            if nome == n.value:
                print('usuario já registrado!')
                nome_valido += 1
                break

        if nome_valido > 0 or len(nome) < 3:
            # caso o usuario já foi cadastrado ou é muito curto
            continue
        else:
            usuario.append(nome)
            while True:
                # coleta da senha
                senha = input('Cadastro de senha: ').strip()
                if len(senha) < 6:
                    print('A senha deve conter no minimo 6 caracteres ')
                    continue
                else:
                    usuario.append(senha)
                    break
        break

    return usuario


def registro(sheet, usuario, book):
    sheet.append(usuario)
    book.save('C:\\Users\\asss1\\OneDrive\\Área de Trabalho\\Projeto do jogo\\Quiz_Copa_do_Mundo\\Pasta1.xlsx')
