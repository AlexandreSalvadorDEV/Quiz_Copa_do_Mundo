from Functions import cadastro, registro


def Menu(str, usuario):
    amarelo_negrito = "\033[1;33m"
    ciano_negrito = "\033[1;36m"
    fim = "\033[m"
    s = '-=' * 60
    # Printa um menu personalizado no terminal
    print(f'{amarelo_negrito}{s}{fim}')
    print(f'{amarelo_negrito}{f"!!BEM - VINDO {usuario.upper()}!!":^100}{fim}')
    print(f'{amarelo_negrito}{"À...":^100}{fim}')
    print(f'{ciano_negrito}{str:^100}{fim}')
    print(f'{amarelo_negrito}{s}{fim}')

    print(f'\n{amarelo_negrito}{"Agora resposta as perguntas a seguir..."}{fim}')
    print()


def Janela_principal(book, sheet_cadastro, sheet_admin):
    usuario = []
    admin = 0
    print('!!Bem-Vindo ao Quiz COPA DO MUNDO!!')
    # Tratamento de ERRO
    while True:
        try:
            forma_login = int(input('Como você desseja continuar??'
                                    '\n1 - ADMIN'
                                    '\n2 - JOGADOR'
                                    '\n>> '))
            if 1 > forma_login > 2:
                # Caso seja uma opção não válida
                print('[ERRO] Digite uma opção válida.')
                continue
        except ValueError:
            print('[ERRO] Digite uma opção válida.')
            continue

        else:
            break

    if forma_login == 1:
        usuario = login(sheet_admin)
        admin += 1

    elif forma_login == 2:
        while True:
            try:
                print('>> JANELA DE JOGADOR')
                forma_entrada = int(input('1 - JÀ CADASTRADO\n'
                                          '2 - NÃO CADASTRADO\n'
                                          '>> '))
                if 1 > forma_entrada > 2:
                    # Caso seja uma opção não válida
                    print('[ERRO] Digite uma opção válida.')
                    continue
                elif forma_entrada == 1:
                    usuario = login(sheet_cadastro)

                elif forma_entrada == 2:
                    usuario_cadastro = cadastro(sheet_cadastro)
                    registro(sheet_cadastro, usuario_cadastro, book)
                    continue

            except ValueError:
                print('[ERRO] Digite uma opção válida.')
                continue

            else:
                break

    if admin != 1:
        rank_inicial = 0
        usuario.append(rank_inicial)

    return usuario


def login(sheet):
    usuario = []
    while True:
        # linha para futuramente poder verificar a senha
        linha = 1
        nome_nao_encontrado = 0
        nome_usuario = input('Nome do Usuário(DIGITE TUDO MINUSCULO): ').strip().title()
        for nome in sheet['A']:
            if nome.value == nome_usuario:
                usuario.append(nome.value)
                # nome encontrado, resetando a variavel
                nome_nao_encontrado = 0
                break
            else:
                # nome não compativel
                nome_nao_encontrado += 1
            linha += 1

        if nome_nao_encontrado > 0:
            print('[ERRO] Usuário não encontrado.\n'
                  'Tente novamente.')
            continue
        else:
            senha_usuario = input('Senha do Usuário: ').strip()
            ver_senha_usuario = sheet.cell(row=linha, column=2)
            if ver_senha_usuario.value == senha_usuario:
                # Usuario existe
                break

    return usuario
