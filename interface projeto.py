from ast import Or
from locale import windows_locale
from PySimpleGUI import PySimpleGUI as sg

#TELA DE INTRODUÇÃO
def JanelaIntrod():
    sg.theme('DarkGreen7')
    layoutintrod = [
        [sg.Text('JOGO QUIZ COPA DO MUNDO')],
        [sg.Text()],
        [sg.Text('esse jogo...')],
        [sg.Text()],
        [sg.Button('Logar como Administrador'), sg.Button('Logar como Usuário')]
    ]
    return sg.Window('QUIZ COPA DO MUNDO', layout= layoutintrod, finalize=True, size=(600, 400))
def JanelaUsuario():
    sg.theme('DarkGreen7')
    layoutusuar = [
        [sg.Text('FAÇA O LOGIN')],
        [sg.Text()],
        [sg.Text('Login: '), sg.Input(key = 'loginusuar')],
        [sg.Text('Senha'), sg.Input(key = 'senhausuar', password_char= '*')],
        [sg.Button('Entrar')],
        [sg.Text()],
        [sg.Button('Cadastrar novo usuário')]
        ]
    return sg.Window('USUÁRIO(A)', layout = layoutusuar, finalize=True, size=(600, 400))
def JanelaAdm():
    sg.theme('DarkGreen7')
    layoutadm = [
        [sg.Text('FAÇA O LOGIN')],
        [sg.Text()],
        [sg.Text('Login: '), sg.Input(key = 'loginadm')],
        [sg.Text('Senha'), sg.Input(key = 'senhaadm', password_char= '*')],
        [sg.Button('Entrar')]
        ]
    return sg.Window('ADMINISTRADOR(A)', layout = layoutadm, finalize=True, size=(600, 400))
def JanelaCad():
    sg.theme('DarkGreen7')
    layoutcad = [
        [sg.Text('CADASTRO')],
        [sg.Text()],
        [sg.Text('Digite seu nome:'), sg.Input(key='nome')],
        [sg.Text('Crie um login: '), sg.Input(key = 'novologin')],
        [sg.Text('Crie uma senha:'), sg.Input(key = 'novasenha', password_char= '*')],
        [sg.Text()],
        [sg.Button('Cadastrar')]
        ]
    return sg.Window('CADASTRO', layout = layoutcad, finalize=True, size=(600, 400))
def JanelaPerg():
    sg.theme('DarkGreen5')
    layout = [
        [sg.Text ('Usuário: #login do usuario'), sg.Text('Score = #X')],
        [sg.Text('Pergunta: ', '#pergunta#')],
        [sg.Text('Alternativas:')],
        [sg.Text('\n')],
        [sg.Text('Qual a alternativa correta?')],
        [sg.Button('A'),sg.Button('B'),sg.Button('C'),sg.Button('D')],
        [sg.Button('Próxima pergunta')],
        [sg.Button('Finalizar')]
    ]
    return sg.Window('PERGUNTAS', layout, finalize=True, size=(600, 400))
def JanelaRanking():
    sg.theme('DarkGreen5')
    layoutranking = [
        [sg.Text('CLASSIFICAÇÃO DAS MELHORES PONTUAÇÕES')],
        [sg.Text('Ranking:')],
        [sg.Text('#ranking... 1º 2º 3º... 10º')]
    ]
    return sg.Window('RANKING', layout = layoutranking, finalize=True, size=(600, 400))

#JANELAS
janela1, janela2, janela3, janela4, janela5, janela6 = JanelaIntrod(), None, None, None, None, None

#EVENTOS
while True:
    window, evento, valores = sg.read_all_windows()
    #quando a janela for fechada
    if window == janela1 and evento == sg.WIN_CLOSED:
        break
    if window == janela2 and evento == sg.WIN_CLOSED:
        break
    if window == janela3 and evento == sg.WIN_CLOSED:
        break
    if window == janela4 and evento == sg.WIN_CLOSED:
        break
    if window == janela5 and evento == sg.WIN_CLOSED:
        break
    if window == janela6 and evento == sg.WIN_CLOSED:
        break

    #proxima janela
    if window == janela1 and evento == 'Entrar como Usuário':
        janela2 = JanelaUsuario()
        janela1.hide()
    if window == janela1 and evento == 'Entrar como Administrador':
        janela3 = JanelaAdm()
        janela1.hide()
    if window == janela2 and evento == 'Cadastrar novo usuário':
        janela4 = JanelaCad()
        janela2.hide()
    if window == janela3 and evento == 'Cadastrar novo usuário':
        janela4 = JanelaCad()
        janela3.hide()
    if window == janela2 and evento == 'Entrar':
        janela5 = JanelaPerg()
        janela2.hide()
    if window == janela3 and evento == 'Entrar':
        janela5 = JanelaPerg()
        janela2.hide()
    if window == janela5 and evento == 'Finalizar':
        janela6 = JanelaRanking()
        janela5.hide()